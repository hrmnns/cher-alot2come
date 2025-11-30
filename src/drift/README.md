# 📄 **README – Drift-Testsystem**

Dieses Verzeichnis enthält alle Skripte und Komponenten zur automatisierten Durchführung und Analyse von Drift-Experimenten im Rahmen der ALOT2COME-Methode. Das System ermöglicht reproduzierbare LLM-Experimente, die Entstehung von Drift messbar machen und deren Auswirkungen objektiv bewerten.

# 1. Komponentenüberblick

```
src/drift/
├── drift_experiment_gemini.py       # Hauptskript: führt Drift-Experimente durch
├── drift_analysis_core.py           # Analysemodul: erkennt Driftarten & erzeugt Reports
├── drift_analysis.py                # optionales CLI für nachträgliche Analysen
├── drift_analysis_core_test.py      # Tests des Analysekerns
├── prompts/                         # Promptsets für Experimente
│   └── prompts.json
└── results/                         # Ergebnisse (.json + .md)
    └── .gitignore
```

# 2. drift_experiment_gemini.py – Experimentskript

Dieses Skript übernimmt die vollständige automatisierte Durchführung eines Drift-Experiments.

### Funktionen

* lädt eine Sequenz von Prompts aus einer JSON-Datei
* führt jeden Prompt sequenziell an ein Gemini-Modell aus
* speichert Antworten als JSON-Artefakt
* unterstützt CLI-Parameter (`--prompts`, `--model`, `--analyze`)
* kann optional automatisch einen Drift-Report erzeugen

### Beispiele

Minimal:

```
python drift_experiment_gemini.py
```

Mit Promptdatei:

```
python drift_experiment_gemini.py --prompts prompts/moduldrift.json
```

Mit Analyse:

```
python drift_experiment_gemini.py --analyze
```

# 3. drift_analysis_core.py – Analysemodul

Der **Analyse-Kern** ist unabhängig von allen anderen Skripten und bietet:

* Normalisierung von Texten
* Ähnlichkeitsanalyse (SequenceMatcher)
* Wortdifferenzen (Begriffsdrift)
* Strukturdrift (nummerierte Listen)
* automatische textliche Interpretation
* Erzeugung eines Markdown-Driftreports

Dieses Modul ist die Grundlage aller Driftanalysen und wird von mehreren Tools importiert.

# 4. drift_analysis.py – CLI-Analyse (optional)

Dieses Skript ermöglicht die **nachträgliche Analyse** einer Ergebnisdatei:

```
python drift_analysis.py results/gemini_drift_experiment_<timestamp>.json
```

→ erzeugt einen Markdown-Report im Ordner `results/`.

# 5. Promptsets (prompts/)

Alle Promptsequenzen liegen in diesem Ordner.
Sie steuern das Drift-Experiment vollständig, ohne dass das Skript selbst geändert werden muss.

Standarddatei:

```
prompts/prompts.json
```

Beispielinhalt:

```json
{
  "prompts": [
    "Definiere Modul.",
    "Bitte wiederhole die Definition.",
    "Welche Eigenschaften hat ein Modul?"
  ]
}
```

# 6. Ergebnisse (results/)

Alle Ergebnisse werden automatisch im Ordner `results/` gespeichert:

* `.json` → Rohdaten, Antworten je Prompt
* `.md` → Drift-Report (optional via `--analyze`)

Dieser Ordner wird nicht versioniert.

# 7. Voraussetzungen

* Python 3.10+
* Paket `google-generativeai`
* gesetzte Umgebungsvariable:

```
GEMINI_API_KEY=dein_api_key
```

# 8. Zweck des Drift-Testsystems

Das System dient dazu:

* Drift in LLM-Kollaborationen empirisch nachzuweisen
* Ergebnisse reproduzierbar zu machen
* Qualitätsmechanismen in ALOT2COME abzusichern
* das Verständnis von Driftarten (Begriffsdrift, Strukturdrift etc.) zu vertiefen
* methodische Entscheidungen messbar zu begründen

Die methodische Dokumentation befindet sich unter:

```
docs/quality/drift-experiments.md
```

# 9. Weitere Schritte

* Erweiterung auf mehrere LLMs (Claude, OpenAI, Mistral)
* Batch-Experimente und Vergleichsreihen
* automatisierte Driftchecks per GitHub Actions
* Visualisierung von Drifttrends über mehrere Experimente
