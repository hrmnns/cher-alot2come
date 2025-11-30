# Drift-Testsystem – Technische Dokumentation
**Ort:** `docs/dev/drift-tests.md`  
**Bereich:** Developer Documentation  
**Zweck:** Nutzung, Aufbau und Erweiterung der automatisierten Drift-Test-Engine

# 1. Überblick

Dieses Dokument beschreibt die technische Funktionsweise des Drift-Testsystems.  
Ziel ist es, Promptsequenzen automatisiert an Gemini zu senden, Ergebnisse nachvollziehbar zu speichern und anschließend eine Drift-Analyse durchzuführen.

Das System besteht aus drei Kernelementen:

- **Experimentskript:** `drift_experiment_gemini.py`
- **Analysemodul:** `drift_analysis_core.py`
- **CLI-Analyse:** `drift_analysis.py` (optional)

Die methodische Einbettung erfolgt in `docs/quality/drift-experiments.md`.

# 2. Verzeichnisstruktur

Die Drift-Testumgebung liegt vollständig unter:

```
src/drift/
├── drift_experiment_gemini.py       # Experiment-Runner (CLI)
├── drift_analysis.py                # Optionales Analyse-CLI
├── drift_analysis_core.py           # Analysemodul
├── prompts/                         # Promptsets (JSON)
│   └── prompts.json
└── results/                         # Ergebnisse (.json/.md)
    └── .gitignore
```

### Hinweise

- `results/` wird automatisch erstellt und nicht versioniert.
- Promptdateien liegen ausschließlich unter `prompts/`.

# 3. Promptsets (JSON)

Promptdateien steuern das Drift-Experiment.  
Struktur:

```json
{
  "prompts": [
    "Wir definieren den Begriff Modul wie folgt...",
    "Welche Eigenschaften hat ein Modul?",
    "Bitte wiederhole die Definition."
  ]
}
```

### Eigenschaften

- Beliebig erweiterbar.
- JSON liegt in `src/drift/prompts/`.
- Wenn keine Datei angegeben wird, lädt das Skript automatisch:

```
prompts/prompts.json
```

# 4. Experimentskript: drift_experiment_gemini.py

Das Skript:

- führt Prompts sequenziell an ein Gemini-Modell aus,
- speichert Antworten als JSON,
- unterstützt CLI-Argumente für flexiblen Betrieb,
- kann optional die Analyse direkt im Anschluss ausführen.

## 4.1 CLI-Parameter

### `--prompts <datei>`
Verwendet eine bestimmte JSON-Promptdatei:

```
python drift_experiment_gemini.py --prompts prompts/moduldrift.json
```

Ohne Angabe wird `prompts/prompts.json` geladen.

### `--model <modellname>`
Setzt das gewünschte Gemini-Modell:

```
python drift_experiment_gemini.py --model models/gemini-2.5-flash
```

Standardmodell:

```
models/gemini-2.5-flash
```

### `--analyze`
Erzeugt nach dem Experiment automatisch einen Markdown-Driftreport:

```
python drift_experiment_gemini.py --analyze
```

## 4.2 Ausführung (Beispiele)

Minimal:

```
python drift_experiment_gemini.py
```

Mit spezifischer Promptdatei:

```
python drift_experiment_gemini.py --prompts prompts/experiment1.json
```

Mit Modellwahl:

```
python drift_experiment_gemini.py --model models/gemini-2.5-flash
```

Experiment + Analyse:

```
python drift_experiment_gemini.py --prompts prompts/moduldrift.json --analyze
```

# 5. Ergebnisdateien (JSON)

Jedes Experiment erzeugt eine Datei wie:

```
results/gemini_drift_experiment_2025-02-03_19-33-22.json
```

Inhalt:

- Promptnummer
- Prompttext
- LLM-Antwort

Diese Datei dient als Grundlage für die Driftanalyse.

# 6. Analysemodul: drift_analysis_core.py

Dieses Modul ist unabhängig vom Experimentskript.

### Funktionen

- Normalisierung von Texten
- Ähnlichkeitsanalyse (SequenceMatcher)
- Wortdifferenzen (Begriffsdrift)
- Strukturdrift (nummerierte Listen)
- automatische Driftinterpretation
- Markdown-Report-Generator

Das Modul wird sowohl vom Analyse-CLI als auch optional vom Experimentskript genutzt.

# 7. Analyse-CLI: drift_analysis.py

Optionales Tool zur nachträglichen Analyse einer Ergebnisdatei:

```
python drift_analysis.py results/gemini_drift_experiment_<timestamp>.json
```

→ erzeugt:

```
results/drift_report_<timestamp>.md
```

# 8. Optional: Auto-Analyse per CLI-Flag

Das Experimentskript kann die Analyse direkt ausführen:

```
python drift_experiment_gemini.py --analyze
```

Erzeugt:

- `.json` Datei (Ergebnisse)
- `.md` Datei (Driftreport)

# 9. Troubleshooting

### „GEMINI_API_KEY ist nicht gesetzt“
→ API-Key als Umgebungsvariable setzen.

### „Promptdatei nicht gefunden“
→ Existenz der Datei prüfen oder `--prompts` verwenden.

### „JSON enthält keine gültige prompts-Liste“
→ JSON-Struktur prüfen.

### „Rate Limit“
→ längeres Delay einbauen (`time.sleep(1)`).

# 10. Erweiterungsideen

- Multi-LLM-Unterstützung (Claude, Mistral, OpenAI)
- GitHub Actions für automatische Driftchecks
- Visualisierung der Drift über mehrere Experimente
- HTML-/PDF-Reports

# 11. Verbindung zur Methode ALOT2COME

Das Drift-Testsystem ist ein technischer Baustein zur Sicherung:

- von Kontextstabilität,
- von Persistenz,
- von Qualitätsmanagement,
- von Reproduzierbarkeit langer LLM-Kollaborationen.

Methodische Einordnung in:  
`docs/quality/drift-experiments.md`
