# Lernflug

Lern-App für Studierende in der Schweiz: Vorlesungen und YouTube-Themen werden zu kurzen Clips, nach jedem Clip kommen zwei Verständnisfragen.

## Funktionen

- **Konto einrichten:** Vorname, Hochschule, Studiengang (229 Studiengänge von Universitäten, ETH, Fachhochschulen und PH, mit Suche), Abschluss und Semester.
- **Vorlesung als Clips:** Eigenes Video hochladen (bleibt auf dem Gerät), optional mit Untertiteln (.vtt/.srt) oder Transkript. Die Vorlesung wird in Clips von 45 s bis 2 min geteilt; die KI erstellt pro Clip zwei Fragen aus Transkript oder Folien.
- **YouTube-Thema:** Thema eingeben, die KI plant einen Lernpfad aus Unterthemen mit Kernpunkten, YouTube-Suche und Fragen. Vorschläge passend zum Studiengang.
- **Kalender:** Prüfungen, Abgaben, Lerneinheiten und Termine mit Erinnerungen in der App.
- **Motivation:** Tagesziel, Lernserie und kurze Motivationshinweise.

## Aufbau

Alles steckt in einer Datei: `index.html` (HTML, CSS und JavaScript, ohne Build-Schritt). Das Demo-Video ist als Data-URI eingebettet; `tools/make_demo_video.py` erzeugt die Folienbilder dafür (danach mit ffmpeg zu MP4 zusammensetzen).

## Website

Läuft auf GitHub Pages: https://toryn1.github.io/Lernflug/

- **Login:** Firebase Authentication (E-Mail/Passwort, Google, Passwort zurücksetzen). Projekt: `clipjaeger-be306`, das gleiche wie bei Clipjäger, ein Konto gilt also für beide Apps.
- **Daten:** Cloud Firestore unter `users/{uid}/lernflug/{profile|events|stats|seen}`. Ist Firestore nicht eingerichtet, speichert die Seite im Browser.
- **KI:** Gemini über Firebase AI Logic (Modell in `GEMINI_MODEL`).

### Einmalig in der Firebase-Konsole einrichten

1. **Firestore Database** erstellen (Standort z. B. `eur3` oder `europe-west6` Zürich) und diese Regeln setzen:

   ```
   rules_version = '2';
   service cloud.firestore {
     match /databases/{database}/documents {
       match /users/{uid}/{document=**} {
         allow read, write: if request.auth != null && request.auth.uid == uid;
       }
     }
   }
   ```
2. **AI Logic** aktivieren und die *Gemini Developer API* wählen.
3. Unter **Authentication → Einstellungen → Autorisierte Domains** muss `toryn1.github.io` stehen (ist für Clipjäger schon so).

## In der Claude-Ansicht

Als Claude-Artifact nutzt dieselbe Datei die Laufzeit von claude.ai (`window.claude`): Login über das Claude-Konto, Speichern und KI über Claude. Firebase wird dort nicht geladen.
