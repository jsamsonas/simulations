// Rope of Sand leaderboard: connects the game and the leaderboard page to Firestore.
// Works only on the Firebase site (sams-history.web.app). Anywhere else it reports "offline"
// and the game plays normally without posting scores.
const SDK = 'https://www.gstatic.com/firebasejs/10.12.2/';
export const COLLECTION = 'ropeOfSand';
export const TEACHERS = { sam: 'Mr. Sam', sondej: 'Mrs. Sondej' };
export const STATE_NAMES = { MA: 'Massachusetts', RI: 'Rhode Island', NY: 'New York', NJ: 'New Jersey', VA: 'Virginia' };

let ready = null;
function connect() {
  if (ready) return ready;
  ready = (async () => {
    const res = await fetch('/__/firebase/init.json');
    if (!res.ok) throw new Error('This copy of the game is not on the Firebase site, so scores cannot be posted.');
    const config = await res.json();
    const { initializeApp } = await import(SDK + 'firebase-app.js');
    const fs = await import(SDK + 'firebase-firestore.js');
    const db = fs.getFirestore(initializeApp(config));
    return { db, fs };
  })();
  return ready;
}

export const docId = p => `${p.teacher}_p${p.period}_${p.first.toLowerCase()}_${p.initial.toLowerCase()}`;

// Posts a finished game. Only the first finished game for each student name counts.
// Resolves to 'posted' or 'already'; throws with a plain-language message on failure.
export async function postScore(p, result) {
  const { db, fs } = await connect();
  const ref = fs.doc(db, COLLECTION, docId(p));
  const existing = await fs.getDoc(ref);
  if (existing.exists()) return { status: 'already', score: existing.data().score };
  await fs.setDoc(ref, {
    teacher: p.teacher, period: p.period, first: p.first, initial: p.initial,
    state: result.state, score: result.score, parts: result.parts,
    createdAt: fs.serverTimestamp(),
  });
  return { status: 'posted', score: result.score };
}

// Calls onChange(rows) now and again whenever a score is added or removed.
export async function watchScores(onChange, onError) {
  const { db, fs } = await connect();
  return fs.onSnapshot(fs.collection(db, COLLECTION), snap => {
    onChange(snap.docs.map(d => {
      const x = d.data();
      return { ...x, id: d.id, t: x.createdAt ? x.createdAt.toMillis() : Date.now() };
    }));
  }, onError);
}

// Highest score first; on a tie, whoever finished first.
export const rank = rows => [...rows].sort((a, b) => b.score - a.score || a.t - b.t);
