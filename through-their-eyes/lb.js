// Through Their Eyes: connects the game and its casualty board to Firestore.
// Works only on the Firebase site (sams-history.web.app). Anywhere else it reports an error
// and the game plays normally without posting.
const SDK = 'https://www.gstatic.com/firebasejs/10.12.2/';
export const COLLECTION = 'throughTheirEyes';
export const TEACHERS = { sam: 'Mr. Sam', sondej: 'Mrs. Sondej' };
export const SOLDIERS = { rhodes: 'Rhodes', gooding: 'Gooding', watkins: 'Watkins', edmonds: 'Edmonds', ransom: 'Ransom', stanley: 'Stanley' };

let ready = null;
function connect() {
  if (ready) return ready;
  ready = (async () => {
    const res = await fetch('/__/firebase/init.json');
    if (!res.ok) throw new Error('This copy of the game is not on the Firebase site, so results cannot be posted.');
    const config = await res.json();
    const { initializeApp } = await import(SDK + 'firebase-app.js');
    const fs = await import(SDK + 'firebase-firestore.js');
    return { db: fs.getFirestore(initializeApp(config)), fs };
  })();
  return ready;
}

export const docId = p => `${p.teacher}_p${p.period}_${p.first.toLowerCase()}_${p.initial.toLowerCase()}`;

// Only each student's first finished game counts.
export async function postResult(p, rec) {
  const { db, fs } = await connect();
  const ref = fs.doc(db, COLLECTION, docId(p));
  const existing = await fs.getDoc(ref);
  if (existing.exists()) return { status: 'already', fate: existing.data().fate };
  await fs.setDoc(ref, {
    teacher: p.teacher, period: p.period, first: p.first, initial: p.initial,
    soldier: rec.soldier, side: rec.side, fate: rec.fate, where: rec.where,
    wounded: rec.wounded, captured: rec.captured, discharged: !!rec.discharged, released: !!rec.released,
    deserted: !!rec.deserted, wentHome: !!rec.wentHome, predicted: rec.predicted, chapters: rec.chapters,
    createdAt: fs.serverTimestamp(),
  });
  return { status: 'posted' };
}

// Calls onChange(rows) now and whenever a result is added or removed.
export async function watchResults(onChange, onError) {
  const { db, fs } = await connect();
  return fs.onSnapshot(fs.collection(db, COLLECTION), snap => {
    onChange(snap.docs.map(d => { const x = d.data(); return { ...x, id: d.id, t: x.createdAt ? x.createdAt.toMillis() : Date.now() }; }));
  }, onError);
}
