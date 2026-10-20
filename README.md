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

## Wichtig zu wissen

Die App wurde als Claude-Artifact gebaut. KI-Funktionen (Fragen, Lernpfade, Themenvorschläge) und das Speichern im Konto nutzen die Laufzeit von claude.ai (`window.claude`). Öffnet man `index.html` anderswo (z. B. lokal oder über GitHub Pages), speichert die App nur im Browser (localStorage) und die KI-Funktionen sind nicht verfügbar. Für eine eigenständige App braucht es ein eigenes Backend (Login, Datenbank, KI-API, YouTube Data API).
