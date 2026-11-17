// Leaderboard pieces the town games use on their start and end screens.
// Each game sets window.LB_GAME = { collection, teachers: { key: 'Name' } } before loading this file.
window.LBKit = (() => {
  const cfg = window.LB_GAME;
  const keys = Object.keys(cfg.teachers);
  const esc = s => String(s).replace(/[&<>"']/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
  const p = { teacher: keys.length === 1 ? keys[0] : '', period: '', first: '', initial: '', err: '' };

  function playerPanel() {
    return `<div class="panel" style="display:flex;flex-direction:column;gap:10px">
      <span class="lbl">Who is playing?</span>
      ${keys.length > 1 ? `<div class="row" style="flex-wrap:wrap;gap:8px">${keys.map(k => `<button class="btn ${p.teacher === k ? '' : 'ghost'} small" data-lbteacher="${k}" aria-pressed="${p.teacher === k}">${esc(cfg.teachers[k])}</button>`).join('')}</div>` : ''}
      <div class="row" style="flex-wrap:wrap;gap:12px;align-items:flex-end">
        <label class="small">Class period<br><select id="lbPeriod" style="font:inherit;padding:6px 8px"><option value="">Choose…</option>${[1, 2, 3, 4, 5, 6, 7, 8].map(n => `<option value="${n}" ${String(p.period) === String(n) ? 'selected' : ''}>Period ${n}</option>`).join('')}</select></label>
        <label class="small">First name<br><input type="text" id="lbFirst" maxlength="15" autocomplete="off" value="${esc(p.first)}" style="width:11em"></label>
        <label class="small">Last initial<br><input type="text" id="lbInitial" maxlength="1" autocomplete="off" value="${esc(p.initial)}" style="width:3em;text-transform:uppercase"></label>
      </div>
      <p class="small muted" style="margin:0">Your first name, last initial, and score appear on the <a href="leaderboard/" target="_blank">class leaderboard</a>. Only your first finished game counts.</p>
      ${p.err ? `<p class="small neg" role="alert" style="margin:0"><b>${esc(p.err)}</b></p>` : ''}
    </div>`;
  }

  // Returns the player, or an error message (and remembers it for the panel).
  function readPlayer() {
    const first = p.first.trim().replace(/\s+/g, ''); const initial = p.initial.trim().toUpperCase();
    p.err = !p.teacher ? 'Choose your teacher.' : !p.period ? 'Choose your class period.'
      : !/^[A-Za-z][A-Za-z'-]{0,14}$/.test(first) ? 'Type your first name using letters only.'
      : !/^[A-Z]$/.test(initial) ? 'Type the first letter of your last name.' : '';
    if (p.err) return p.err;
    return { teacher: p.teacher, period: +p.period, first: first[0].toUpperCase() + first.slice(1).toLowerCase(), initial };
  }

  // Wires the inputs; returns true when the event belonged to the panel.
  function handleClick(b, rerender) {
    if (b.dataset.lbteacher) { p.teacher = b.dataset.lbteacher; p.err = ''; rerender(); return true; }
    return false;
  }
  function handleInput(t) {
    const k = { lbPeriod: 'period', lbFirst: 'first', lbInitial: 'initial' }[t.id];
    if (k) { p[k] = t.value; return true; }
    return false;
  }

  function endPanel(G, result) {
    const pl = G.player; const st = G.posted; let status;
    if (!pl) status = 'This game was started before the leaderboard existed, so it can’t be posted. Start a new game to get on the board.';
    else if (G.desk) status = 'Games played with the teacher’s desk don’t count for the leaderboard.';
    else if (!st || st.status === 'sending') status = 'Posting your score…';
    else if (st.status === 'posted') status = `Posted for <b>${esc(pl.first)} ${esc(pl.initial)}.</b>, ${esc(cfg.teachers[pl.teacher])}, period ${pl.period}.`;
    else if (st.status === 'already') status = `${esc(pl.first)} ${esc(pl.initial)}. already has a score on the board (${st.score}). Only your first finished game counts.`;
    else status = `Your score couldn’t be posted: ${esc(st.msg)} <button class="btn ghost small" id="lbRetry">Try again</button>`;
    return `<div class="panel"><h2>Leaderboard score: ${result.score}</h2>
      <table><thead><tr><th>Category</th><th style="text-align:right">Points</th></tr></thead><tbody>
      ${result.parts.map(([k, v]) => `<tr><td>${esc(k)}</td><td style="text-align:right" class="num">${v}</td></tr>`).join('')}</tbody></table>
      <p class="small" style="margin-top:10px">${status}</p>
      <p class="small"><a href="leaderboard/" target="_blank">See the leaderboard</a></p></div>`;
  }

  async function post(G, result, save, refresh) {
    if (!G.player || G.desk || (G.posted && ['posted', 'already', 'sending'].includes(G.posted.status))) return;
    G.posted = { status: 'sending' };
    try {
      const lb = await import('./lb.js');
      G.posted = await lb.postScore(cfg.collection, G.player, { score: result.score, parts: result.parts.map(x => x[1]) });
    } catch (e) { G.posted = { status: 'error', msg: e && e.message ? e.message : 'no connection' }; }
    save(); refresh();
  }

  // Points line up with letter grades: A = 90s, B = 80s, C = 70s, D = 60s, F below 60.
  function points(v, cuts, floor, top) {
    const pts = [[floor, 0], [cuts[3], 60], [cuts[2], 70], [cuts[1], 80], [cuts[0], 90], [top, 100]];
    if (v <= pts[0][0]) return 0;
    for (let i = 1; i < pts.length; i++) if (v <= pts[i][0]) { const [x0, y0] = pts[i - 1], [x1, y1] = pts[i]; return y0 + (y1 - y0) * (v - x0) / (x1 - x0); }
    return 100;
  }
  const electionPoints = won => [0, 22.5, 45, 65, 75, 85, 100][Math.max(0, Math.min(6, won))];
  // parts: [[name, points], ...] equally weighted
  function score(parts) {
    const r = parts.map(([k, v]) => [k, Math.round(v * 10) / 10]);
    return { score: Math.round(r.reduce((s, x) => s + x[1], 0) / r.length * 10) / 10, parts: r };
  }

  return { playerPanel, readPlayer, handleClick, handleInput, endPanel, post, points, electionPoints, score };
})();
