# Drift Compare Module  
## Baseline–Persistenz-Vergleich für methodisch stabile LLM-Kollaboration

Dieses Dokument beschreibt das Compare-Modul für ALOT2COME.  
Es ermöglicht einen vollständigen, nachvollziehbaren Vergleich zweier Driftanalysen — typischerweise:

- **Baseline (ohne Schutzmechanismen)**  
- **Persistenzmodus (persist-soft / persist-hard)**  

Das Modul ist zentral, um die Wirksamkeit der Qualitätsmodi methodisch nachzuweisen.

# 1. Zielsetzung

Das Compare-Modul beantwortet folgende Kernfragen:

- *Wie viel Drift entsteht ohne Persistenzsicherung?*  
- *Wie stark reduzieren Persistenzmechanismen den Drift?*  
- *Welche Driftarten werden wirksam verhindert?*  
- *Welche bleiben bestehen?*  
- *Wie unterscheiden sich Modelle, Modi oder Testsets?*  

Damit liefert das Modul eine **wissenschaftlich belastbare Grundlage** für Aussagen wie:

> „Persist Hard reduziert die Driftintensität um 77 % gegenüber der Baseline.“

# 2. Eingaben

Das Modul benötigt zwei Ergebnisdateien aus dem Experiment-Modul:

```
results/<experiment_1>.json
results/<experiment_2>.json
```

Typischerweise:

- `baseline.json`
- `persist-hard.json`

Beide Dateien müssen in der ALOT2COME-typischen Formatstruktur vorliegen:

```json
[
  {
    "prompt_number": 1,
    "prompt": "...",
    "answer": "..."
  },
  ...
]
```

# 3. Architektur

Die Datei `drift_analysis_compare.py` implementiert:

### 3.1 Analyse-Pipeline

1. **Beide Dateien laden**
2. **Für beide Läufe drift_analysis_core.analyze() aufrufen**
3. **Ergebnisse vergleichen**
4. **Differenzen & Driftreduktion berechnen**
5. **Markdown- oder JSON-Report erzeugen**

### 3.2 Vergleichsmetriken

- Similarity Mean (Durchschnitt)
- Drift Ratio Mean (Wortdrift)
- Strukturwechsel gesamt
- Rollenwechsel
- Domänenwechsel
- aggregierte Drift-Intensität
- Driftreduktion (in %)

# 4. Zentrale Vergleichsmetrik

Die Driftreduktion ist die zentrale Kennzahl:

```
Reduction = 1 - (Intensity_persist / Intensity_baseline)
```

Interpretation:

| Wert | Bedeutung |
|------|-----------|
| 1.0  | Drift vollständig verhindert |
| 0.75 | Drift um 75% reduziert |
| 0.50 | Drift halbiert |
| 0.0  | keine Verbesserung |
| < 0  | Persistenzmodus schlechter als Baseline |

# 5. CLI-Nutzung

Beispiel:

```bash
python src/drift/drift_analysis_compare.py   results/baseline.json   results/persist-hard.json   --out-md   --out-json
```

### Optionen:

- `--out-md`  
  erzeugt einen vollständigen Markdown-Report

- `--out-json`  
  erzeugt eine JSON-Datei mit allen Vergleichsmetriken

# 6. Beispielausgabe (Kurzform)

Vergleichsmatrix (Beispiel):

```json
{
  "similarity_mean_baseline": 0.742,
  "similarity_mean_other": 0.905,
  "word_drift_mean_baseline": 0.38,
  "word_drift_mean_other": 0.09,
  "structure_changes_baseline": 4,
  "structure_changes_other": 0,
  "intensity_baseline": 0.421,
  "intensity_other": 0.095,
  "drift_reduction": 0.774
}
```

Interpretation:

- Persist Hard reduziert die Gesamt-Drift um **77,4 %**
- Similarity steigt signifikant (0.74 → 0.90)
- Wortdrift fällt um 76 %
- Strukturdrift wird vollständig eliminiert
- Rollen- und Kontextdrift verschwinden vollständig

# 7. Markdown-Report

Das Compare-Modul erzeugt Berichte nach folgendem Muster:

```
# Driftvergleich – Baseline vs. Persistenzmodus

## Similarity (Durchschnitt)
| Lauf      | Mean |
|----------|------|
| baseline | 0.742 |
| persist  | 0.905 |

## Wortdrift
| Lauf      | Drift Ratio |
|-----------|-------------|
| baseline  | 0.38        |
| persist   | 0.09        |

## Strukturdrift
| Lauf      | Strukturwechsel |
|-----------|------------------|
| baseline  | 4                |
| persist   | 0                |

## Gesamtintensität
baseline: 0.421  
persist:  0.095  
**Reduktion: 77,4 %**
```

Alle Werte werden automatisch berechnet.

# 8. Integration in ALOT2COME

Das Compare-Modul ist Teil der Qualitäts-Toolchain:

```
Experiment → Analyse → Qualitative Analyse → Compare → Dokumentation
```

Es ist konzipiert für:

- empirische Forschung  
- methodische Nachweise  
- Schulung & Reporting  
- Modellvergleiche  
- Langzeit-Studien  

Es bildet damit die Basis für wissenschaftliche Argumentationen zur Stabilität und Driftresistenz.

# 9. Weiterführende Dokumente

- `docs/dev/drift-metrics.md`
- `docs/dev/drift-tests.md`
- `docs/quality/drift-experiments.md`
- Experimentmodul: `drift_experiment_gemini.py`
- Analysemodul: `drift_analysis_core.py`

# 10. Status

Das Compare-Modul ist **vollständig funktionsbereit** und in den Workflow integriert.  
Weitere Erweiterungen (optional):

- Visualisierungen  
- Multi-Modell-Vergleiche  
- Benchmarking  
- Persistenzprofil-Dashboard  
