# 📄 **Drift-Testsystem – Technische Dokumentation**

**Ort:** `docs/dev/drift-tests.md`
**Bereich:** Developer Documentation
**Zweck:** Technische Nutzung, Aufbau und Erweiterung der Skript-basierten Drift-Analyse

# 1. Überblick

Dieses Dokument beschreibt die **technische Implementierung, Nutzung und Struktur** des skriptbasierten Drift-Testsystems.
Ziel ist es, **Promptsequenzen automatisiert an ein LLM (Gemini)** zu senden, die Ergebnisse reproduzierbar zu speichern und anschließend automatisch auszuwerten.

Das System dient als Grundlage für:

* empirischen Drift-Nachweis
* Vergleichsexperimente
* Qualitätsanalyse im Kontext von ALOT2COME
* reproduzierbare LLM-Interaktionen

Die methodische Einordnung erfolgt separat unter
`docs/quality/drift-experiments.md`.

# 2. Verzeichnisstruktur

Die gesamte Drift-Test-Engine befindet sich unter:

```
src/drift/
├── drift_experiment_gemini.py       # Experiment-Runner
├── drift_analysis.py                # CLI Report Generator
├── drift_analysis_core.py           # Analysemodul
├── prompts/                         # Promptsets (JSON)
│   └── prompts.json
└── results/                         # Ausgabedateien (.json/.md)
    └── .gitignore
```

**Hinweise:**

* Der Ordner `results/` wird **nicht** versioniert (durch `.gitignore`).
* Alle Promptsets werden in `prompts/` versioniert.
* Die Analyse ist modular und unabhängig vom Experiment-Skript.

# 3. Promptsets (JSON)

Die Skripte erwarten eine JSON-Datei mit folgender Struktur:

```json
{
  "prompts": [
    "Wir definieren den Begriff Modul wie folgt...",
    "Welche Eigenschaften hat ein Modul?",
    "Bitte beschreibe ein Beispiel-Modul."
  ]
}
```

**Wichtige Merkmale:**

* Promptdateien sind **frei erweiterbar**, ohne Codeänderungen.
* Für jeden Testlauf kann eine eigene Datei verwendet werden.
* Die Dateien sind versionierbar und erlauben systematische Drift-Experimente.

# 4. Experiment-Skript: `drift_experiment_gemini.py`

Das Skript:

* lädt die Promptdatei
* führt jeden Prompt sequenziell an Gemini aus
* sammelt alle Antworten
* speichert sie als JSON
* nutzt das Gemini Free Tier
* enthält Fehlerbehandlung für fehlende Dateien und API-Keys

### **Ausführung**

Mit eigener Promptdatei:

```bash
python drift_experiment_gemini.py prompts/custom_prompts.json
```

Oder mit Standarddatei (`prompts.json`):

```bash
python drift_experiment_gemini.py
```

### **API-Key setzen**

Windows PowerShell:

```powershell
setx GEMINI_API_KEY "DEIN_API_KEY"
```

Dann neues PowerShell-Fenster öffnen.

Test:

```powershell
echo $Env:GEMINI_API_KEY
```

# 5. Ergebnisdateien (JSON)

Das Experiment erzeugt eine Datei im Ordner `src/drift/`:

```
gemini_drift_experiment_2025-01-05_12-33-12.json
```

Diese Datei enthält:

* alle Prompts
* alle Antworten in Reihenfolge
* vollständiges Drift-Testprotokoll

Sie dient als **Rohdatenbasis** für die Analyse.

# 6. Analyse-Engine: `drift_analysis_core.py`

Dieses Modul enthält alle wesentlichen Analysefunktionen:

* **Normalisierung** für Textvergleich
* **Ähnlichkeitsanalyse** (SequenceMatcher)
* **Wort-Differenzen** (added / removed words → Begriffsdrift)
* **Strukturprüfungen** (Listen → Strukturdrift)
* **automatische Textinterpretation**
* **Markdown-Report-Generator**

Das Modul wird sowohl vom

* CLI-Analyzer
* Experiment-Skript (optional)

verwendet.

# 7. CLI-Analyse: `drift_analysis.py`

Dieses Skript analysiert jede Ergebnis-JSON-Datei und erzeugt einen Markdown-Bericht.

### **Ausführung:**

```bash
python drift_analysis.py gemini_drift_experiment_2025-01-05_12-33-12.json
```

Ergebnis:

```
drift_report_2025-01-05_12-33-12.md
```

Der Bericht enthält:

* Vergleich Baseline ↔ Kontrollpunkt
* Ähnlichkeitswert (0–1)
* neu hinzugekommene Wörter
* entfernte Wörter
* Listenveränderungen
* automatische Interpretation
* Originalantworten

# 8. Optional: Auto-Analyse

Das Experiment-Skript unterstützt ein optionales `--analyze` Flag:

```bash
python drift_experiment_gemini.py prompts.json --analyze
```

Erzeugt:

* `gemini_drift_experiment_*.json`
* `drift_report_*.md`

Damit sind **Experiment und Analyse in einem Schritt** möglich.

# 9. Troubleshooting

### **„GEMINI_API_KEY ist nicht gesetzt.“**

→ API-Key als Umgebungsvariable setzen und Terminal neu starten.

### **„JSON-Datei nicht gefunden.“**

→ Pfad prüfen oder Promptdatei in `/prompts/` ablegen.

### **„Kein gültiges Prompts-Array.“**

→ JSON prüfen (Liste unter `prompts`).

### **„Fehler: Rate Limit“**

→ längeres Delay einbauen (z. B. `time.sleep(1)`).

# 10. Erweiterungsmöglichkeiten

* Multi-LLM-Unterstützung (Claude, OpenAI, Mistral)
* Batch-Experimente
* GitHub Actions für nächtliche Drift-Checks
* HTML-Reporting
* semantische Analyse per Embeddings
* Drift-Trendvisualisierungen

# 11. Bezug zur Methode ALOT2COME

Dieses Drift-Testsystem ist ein **technisches Werkzeug**, das folgende methodische Konzepte unterstützt:

* Drift-Management
* Persistenzmechanismen
* Qualitätskontrolle
* Reproduzierbarkeit
* evidenzbasierte Experimente

Die methodische Doku findest du unter:

```
docs/quality/drift-experiments.md
```

