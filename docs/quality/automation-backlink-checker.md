# Backlink-Checker – Konzept und technische Spezifikation

## 1. Zweck und Einordnung
Der Backlink-Checker ist ein erster Baustein innerhalb einer Reihe von Mini-Automationen, die die langfristige Qualität, Konsistenz und Navigierbarkeit der Dokumentation im cher-alot2come-Projekt sicherstellen sollen.
Er ergänzt die bestehenden Mechanismen zu Persistenz, Drift-Management und Informationsarchitektur durch eine **automatisierte Prüfung struktureller Integrität**.

Backlinks dienen innerhalb der Methodik als verbindendes Element zwischen Dokumenten. Sie sichern:
- klare Orientierung,
- bidirektionale Navigation,
- strukturelle Konsistenz entlang der Informationsarchitektur.

Der Backlink-Checker stellt sicher, dass diese Verknüpfungsmechanismen überall korrekt umgesetzt werden.

## 2. Zielsetzung des Backlink-Checkers
Der Backlink-Checker soll automatisiert prüfen, ob alle relevanten Dokumente:
1. eine definierte Backlink-Sektion besitzen (z. B. „Weiterführende Dokumente“),
2. ausschließlich auf existierende, valide Dateien verlinken,
3. der Repository-Struktur folgen (Ordner, Dateinamen),
4. im zentralen Einstiegspunkt `docs/README.md` korrekt referenziert werden.

Das Ziel ist ein **automatisierbarer Qualitätsstandard**, der sicherstellt, dass die gesamte Dokumentation konsistent verknüpft bleibt und der Navigationsfluss nicht durch fehlende oder fehlerhafte Links gestört wird.

## 3. Regeln & Anforderungen

### 3.1 Grundregeln
- Jedes Dokument im Ordner `docs/` muss eine Backlink-Sektion enthalten.
- Die Standardbezeichnung der Sektion lautet:  
  **„Weiterführende Dokumente“**
- Die Sektion muss mindestens einen Link enthalten.
- Links müssen auf existierende Dateien im Projekt zeigen.
- Die Struktur der Links muss der Informationsarchitektur entsprechen.

### 3.2 Zu prüfende Elemente

| Prüfelement | Beschreibung |
|------------|--------------|
| **Existenz der Backlink-Sektion** | Ist die Sektion vorhanden? Ist sie korrekt benannt? |
| **Link-Validität** | Zeigt jeder Markdown-Link auf eine existierende Datei? |
| **Broken-Links** | Erkennung nicht vorhandener Dateien oder Tippfehler. |
| **Strukturkonformität** | Stimmen Pfade und Ordnung mit der Informationsarchitektur überein? |
| **Integration in `docs/README.md`** | Jede Datei muss im zentralen Inhaltsverzeichnis gelistet sein. |

### 3.3 Dokumenttypen (Scope)
**Im Scope:**
- alle Markdown-Dateien unter `docs/` inklusive Unterordner

**Out-of-Scope:**
- Dateien im Wiki
- Dateien außerhalb von `docs/` (z. B. `/planning`, `/media` etc.)

## 4. Technisches Konzept

### 4.1 Technologie
- Sprache: **Python** oder **Node.js** (beide geeignet; Python vorgeschlagen)
- Script-Pfad: `tools/check_backlinks.py` oder `scripts/check_backlinks.js`

### 4.2 Funktionsprinzip
1. Traversiere rekursiv `docs/`
2. Öffne jede Markdown-Datei
3. Finde die Backlink-Sektion per Überschrift `## Weiterführende Dokumente`
4. Extrahiere alle Markdown-Links (`[Text](pfad.md)`)
5. Prüfe:
   - Existenz der Backlink-Sektion  
   - Existenz jeder Ziel-Datei  
   - Konsistenz zu Verzeichnisstruktur  
6. Erzeuge Report:
   - Zusammenfassung + Fehlerliste
   - Exit-Code ≠ 0 bei Fehlern

### 4.3 Ausgabeformate
- **CLI-Summary**
- **Markdown-Report** unter `reports/backlink-check.md`
- Exit-Codes:  
  - `0` → keine Fehler  
  - `1` → Fehler gefunden  
  - `2` → kritischer Fehler (Parsing-Fehler o. ä.)

## 5. Prototyp-Spezifikation

### 5.1 Minimalumfang (DoD-relevant)
Der erste funktionale Prototyp umfasst:
- Traversieren des `docs/`-Ordners
- Erkennen der Backlink-Sektion
- Erkennen von Links in dieser Sektion
- Prüfen, ob die verlinkten Dateien existieren
- Ausgabe eines strukturierten Fehlerreports

### 5.2 CLI-Aufruf
```
python tools/check_backlinks.py
```
oder
```
node scripts/check_backlinks.js
```

### 5.3 Fehlerkategorien
- **ERROR**: fehlende Sektion, Broken Link, falscher Pfad  
- **WARNING**: ungewöhnlich kurze Backlink-Liste  
- **INFO**: strukturell unauffälliges Dokument

### 5.4 Beispielausgabe
```
Scanning docs/ ...

[ERROR] docs/processes/process-macro.md
  - Backlink-Sektion fehlt

[ERROR] docs/quality/drift-management.md
  - Broken Link: '../meta/unknown-file.md'

[OK] docs/meta/information-architecture.md

Summary:
  2 Dateien mit Fehlern
  1 Datei OK
Exit-Code: 1
```

## 6. Erweiterbarkeit & Roadmap

### Stufe 1 (jetzt)
- Backlink-Checker (dieses Dokument)

### Stufe 2 (nächste Schritte)
- Glossar-Checker
  - Findet unerwünschte Synonyme
  - Prüft Kernbegriffe

### Stufe 3 (erweiterte Konsistenzchecks)
- Prüfung der Metadatenblöcke
- Kategorie-Validierung (`category:` vs. Ordnerstruktur)
- Prüfung der decision-Logs
- Vollständigkeitschecks für Persistenz-Mechanismen

### Optionale Konfigurationsdatei
`checker.config.json`  
(z. B. für erlaubte Abweichungen, Blacklist, Whitelist)

## 7. Integration in GitHub Actions (optional vorbereitet)

### Beispiel-Workflow (noch nicht aktiv)
```yaml
name: Documentation Quality Checks

on:
  pull_request:
  push:
    branches: [ main ]

jobs:
  backlink-check:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'
      - name: Run Backlink Checker
        run: |
          python tools/check_backlinks.py
```

### Trigger-Empfehlung
- PRs in `main`
- optional: nightly run

## 8. Referenzen
- Informationsarchitektur  
- Document Types & Storage  
- Persistenz-Mechanismen  
- Drift-Management  
- Glossar  
