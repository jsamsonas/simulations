# Moving the simulations to Firebase Hosting

These files are new in the top folder of the repository:

- `index.html` — a home page that lists every simulation, so students need only one link
- `firebase.json` — tells Firebase which files to publish and to always serve your newest edits
- `FIREBASE-SETUP.md` — these steps

None of the simulations themselves change. The Python games keep `mini-coi.js`; it works on Firebase the same way it does on GitHub Pages.

## 1. Create the Firebase project (5 minutes)

1. Go to https://console.firebase.google.com and click **Create a project**.
2. Name it something short. The name becomes your web address, e.g. `samsonas-history` → `https://samsonas-history.web.app`. Pick it carefully; it can't be changed later.
3. Turn **off** Google Analytics (not needed). Stay on the free **Spark** plan.

If your school Google account won't let you create a project, the district has turned off Google Cloud for staff. Use a personal Gmail account, or ask IT to allow Firebase.

## 2. Install the Firebase tool on your computer (one time)

1. Install Node.js (the "LTS" version) from https://nodejs.org.
2. Open Terminal (Mac) or Command Prompt (Windows) and run:

   ```
   npm install -g firebase-tools
   ```

   On a Mac, if that fails with a permissions error, put `sudo ` in front of it.

## 3. Get the repository folder onto your computer

Use GitHub Desktop (File → Clone repository → `jsamsonas/simulations`), or on github.com click **Code → Download ZIP** and unzip it. Copy the three new files into the top folder, next to `mill-town`, `confederation`, and the others.

## 4. Publish

In Terminal, go into that folder (type `cd `, a space, then drag the folder onto the window and press Enter). Then run these one at a time:

```
firebase login
firebase use --add
firebase deploy --only hosting
```

- `firebase login` opens a browser. Sign in with the account you used in step 1.
- `firebase use --add` lists your projects. Pick the new one, and type `default` when it asks for an alias.
- `firebase deploy` uploads everything and prints your address, e.g. `https://samsonas-history.web.app`.

To publish changes later, run `firebase deploy --only hosting` again from the same folder.

## 5. (Optional) Publish automatically whenever GitHub changes

If you want to keep adding simulations to GitHub as you do now and have Firebase update itself:

```
firebase init hosting:github
```

Answers: repository `jsamsonas/simulations`; run a build script → **No**; deploy when a PR is merged → **Yes**; live branch → `main`. Then push the new files (including `.firebaserc` and the new `.github` folder) to GitHub. From then on, every change on GitHub goes live on Firebase within a couple of minutes.

## 6. Before you give students the link

- Open the address on a student Chromebook while logged in as a student. Some school web filters block new `web.app` addresses; if yours does, ask IT to allow it.
- Post the home page link in Canvas. A single game can be linked directly, e.g. `https://samsonas-history.web.app/mill-town/`.
- Saved progress does not carry over from the GitHub address to the new one, so switch a class between simulations, not in the middle of one. The GitHub Pages links keep working until you turn Pages off.
