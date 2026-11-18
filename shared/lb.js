// Shared leaderboard code for the town games (Mill Town, Cotton Town).
// Talks to Firestore only on the Firebase site; anywhere else it reports an error and the game plays normally.
const SDK = 'https://www.gstatic.com/firebasejs/10.12.2/';

let ready = null;
function connect() {
  if (ready) return ready;
  ready = (async () => {
    const res = await fetch('/__/firebase/init.json');
    if (!res.ok) throw new Error('This copy of the game is not on the Firebase site, so scores cannot be posted.');
    const config = await res.json();
    const { initializeApp } = await import(SDK + 'firebase-app.js');
    const fs = await import(SDK + 'firebase-firestore.js');
    return { db: fs.getFirestore(initializeApp(config)), fs };
  })();
  return ready;
}

export const docId = p => `${p.teacher}_p${p.period}_${p.first.toLowerCase()}_${p.initial.toLowerCase()}`;

// Only the first finished game for each student name counts.
export async function postScore(collection, p, result) {
  const { db, fs } = await connect();
  const ref = fs.doc(db, collection, docId(p));
  const existing = await fs.getDoc(ref);
  if (existing.exists()) return { status: 'already', score: existing.data().score };
  await fs.setDoc(ref, {
    teacher: p.teacher, period: p.period, first: p.first, initial: p.initial,
    score: result.score, parts: result.parts, createdAt: fs.serverTimestamp(),
  });
  return { status: 'posted', score: result.score };
}

export async function watchScores(collection, onChange, onError) {
  const { db, fs } = await connect();
  return fs.onSnapshot(fs.collection(db, collection), snap => {
    onChange(snap.docs.map(d => { const x = d.data(); return { ...x, id: d.id, t: x.createdAt ? x.createdAt.toMillis() : Date.now() }; }));
  }, onError);
}

// Highest score first; on a tie, whoever finished first.
export const rank = rows => [...rows].sort((a, b) => b.score - a.score || a.t - b.t);

const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
const nm = r => `${esc(r.first)} ${esc(r.initial)}.`;
const fmt = n => (Math.round(n * 10) / 10).toFixed(1);

const finished = n => `${n} finished`;
// The last few students to finish, newest first (names only, no scores).
function ticker(rows, teachers, one) {
  const recent = [...rows].sort((a, b) => b.t - a.t).slice(0, 6);
  const fresh = Date.now() - 10 * 60 * 1000;
  return `<div class="ticker"><span class="lbl">Just finished</span>${recent.map(r => `<span class="n${r.t > fresh ? ' new' : ''}">${nm(r)} <span class="count">${one ? '' : esc(teachers[r.teacher]) + ', '}P${r.period}</span></span>`).join('')}</div>`;
}
function periodCards(rows) {
  const periods = [...new Set(rows.map(r => r.period))].sort((a, b) => a - b);
  return `<div class="periods">${periods.map(p => `<div class="period"><h3>Period ${p} <span class="count">${finished(rows.filter(r => r.period === p).length)}</span></h3><ol>${rows.filter(r => r.period === p).slice(0, 3)
    .map((r, i) => `<li><span class="m m${i + 1}">${i + 1}</span><span>${nm(r)}</span><span class="score">${fmt(r.score)}</span></li>`).join('')}</ol></div>`).join('')}</div>`;
}

// Fills the leaderboard page. cfg = { collection, teachers: { key: 'Name' }, scope: 'all history classes' }
export function startBoard(cfg) {
  const board = document.getElementById('board'); const live = document.getElementById('live');
  const one = Object.keys(cfg.teachers).length === 1;
  const render = rows => {
    if (!rows.length) { board.innerHTML = '<p class="msg">No finished games yet. Scores appear here the moment a student finishes.</p>'; return; }
    const all = rank(rows); const top = all[0];
    let html = `<section class="champ"><div class="lbl">Overall champion · ${esc(cfg.scope)} · ${finished(all.length)}</div><div class="who">${nm(top)}</div>
      <div class="meta">${one ? '' : esc(cfg.teachers[top.teacher]) + ', '}period ${top.period} · <span class="score">${fmt(top.score)}</span></div></section>` + ticker(all, cfg.teachers, one);
    if (one) { board.innerHTML = html + periodCards(all); return; }
    html += '<div class="teachers">';
    for (const [tk, tname] of Object.entries(cfg.teachers)) {
      const mine = all.filter(r => r.teacher === tk);
      html += `<section><h2>${esc(tname)} <span class="count">· ${finished(mine.length)}</span></h2>`;
      html += mine.length ? `<div class="tchamp"><div class="lbl">Top in ${esc(tname)}’s classes</div><div class="who">${nm(mine[0])} <span class="score">${fmt(mine[0].score)}</span></div><div class="st">Period ${mine[0].period}</div></div>${periodCards(mine)}` : '<p class="empty">No finished games yet.</p>';
      html += '</section>';
    }
    board.innerHTML = html + '</div>';
  };
  const fail = e => { live.textContent = 'Not connected'; live.classList.add('off'); board.innerHTML = `<p class="msg">The leaderboard couldn’t load. ${esc(e && e.message ? e.message : '')}</p>`; };
  watchScores(cfg.collection, rows => { live.textContent = 'Live'; live.classList.remove('off'); render(rows); }, fail).catch(fail);
}
