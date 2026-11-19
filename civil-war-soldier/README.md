# The Soldier's Odds

Card-based Civil War soldier simulation with real casualty odds and a live class casualty board.

- `index.html`: the game
- `lb.js`: saves each student's first finished war to Firestore (collection `civilWarSoldier`)
- `leaderboard/index.html`: the casualty board (by teacher, period, and side, plus name lists)

## Firestore rule to add

In the Firebase console (Firestore Database > Rules), add this inside `match /databases/{database}/documents { ... }`, next to the rules for the other games:

```
match /civilWarSoldier/{id} {
  allow read: if true;
  allow create: if request.resource.data.side in ['Union', 'Confederate']
                && request.resource.data.fate in ['home', 'killed', 'wounds', 'disease', 'prison'];
  allow update, delete: if false;
}
```

To clear a class's results, delete documents in the Firebase console.
