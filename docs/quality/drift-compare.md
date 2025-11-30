# Driftvergleich (Compare Module)  
## Qualitätsbewertung von LLM-Stabilität unter ALOT2COME

Das Compare-Modul ist ein Kernelement der Qualitätsarchitektur von ALOT2COME.  
Es ermöglicht, zwei Driftanalysen — typischerweise:

- eine **Baseline ohne Schutz**, und  
- eine **Persistenz- oder Qualitätsmodus-Variante**

direkt miteinander zu vergleichen.

Damit liefert es die Grundlage, um die Wirksamkeit von Qualitätsmaßnahmen **messbar, nachvollziehbar und reproduzierbar** darzustellen.

# 1. Zielsetzung

Der Driftvergleich verfolgt folgende Qualitätsziele:

- **Messbarkeit:** Wie stark verändert sich die Drift unter verschiedenen Bedingungen?  
- **Reproduzierbarkeit:** Kann ein Ergebnisstabilitätsgewinn zuverlässig nachgewiesen werden?  
- **Qualitätsbewertung:** Wie wirksam sind Persistenzmodi wie _persist-soft_ oder _persist-hard_?  
- **Modellvergleich:** Unterscheiden sich LLMs in Bezug auf Driftanfälligkeit?  
- **Methodische Absicherung:** Können Argumente und Ergebnisse wissenschaftlich sauber belegt werden?

Das Compare-Modul ist damit ein **zentrales Instrument**, um die Qualität von LLM-Kollaboration über längere Sequenzen zu sichern.

# 2. Eingangsdaten

Der Vergleich erfolgt zwischen zwei vollständigen Driftanalyse-Ergebnisdateien:

- `results/<baseline>.json`
- `results/<comparison>.json`

Diese werden zuvor durch die Experiment-Skripte erzeugt.

# 3. Bewertete Driftarten

Der Vergleich bewertet u. a.:

- **Semantische Drift**  
- **Wortdrift / Begriffsdrift**  
- **Strukturdrift**  
- **Rollendrift**  
- **Kontext- / Domänendrift**  
- **Aggregierte Driftintensität**

Zusätzlich wird eine **Driftreduktion** berechnet:

```
Drift Reduction = 1 - (Intensity_persist / Intensity_baseline)
```

Dies ist der wichtigste Qualitätsindikator des gesamten Moduls.

# 4. Zentrale Vergleichsmetriken

Das Compare-Modul berechnet:

| Kategorie               | Metriken |
|------------------------|----------|
| **Semantik**           | Similarity Mean, Trend |
| **Wortdrift**          | Drift Ratio Mean, Veränderungsmuster |
| **Struktur**           | Anzahl Strukturwechsel |
| **Rollenverhalten**    | Rollenwechsel gesamt |
| **Kontextstabilität**  | Domänenwechsel |
| **Gesamtintensität**   | Aggregierter Drift-Intensitäts-Score |
| **Qualitätswirkung**   | Driftreduktion (%) |

Diese Kennzahlen ermöglichen eine fundierte Qualitätsbewertung.

# 5. Interpretation (Beispiel)

Ein typisches Ergebnis:

- Similarity steigt deutlich  
- Wortdrift sinkt drastisch  
- Strukturdrift verschwindet nahezu vollständig  
- Rollen- und Kontextwechsel treten nicht mehr auf  
- Driftintensität sinkt von 0.42 auf 0.095  
- Driftreduktion = **77 %**

Interpretation:

> Persist Hard stabilisiert die LLM-Ausgaben signifikant und verhindert mehr als drei Viertel aller Driftarten.  
> Dies führt zu deutlich konsistenterer, reproduzierbarer und präziser LLM-Kollaboration.

# 6. Rolle im ALOT2COME-Prozess

Das Compare-Modul wird im Qualitätsprozess eingesetzt nach:

1. Experiment (Baseline)  
2. Experiment (Persistenzmodus)  
3. Analyse  
4. Qualitative Analyse  
5. **Vergleichsanalyse (dieses Modul)**  
6. Dokumentation  

Damit bildet es den **methodischen Abschluss der Driftbewertung** und liefert die Grundlage für:

- empirische Studien  
- Qualitätsberichte  
- Prozessoptimierungen  
- Modell- und Moduswahl  
- Trainings der Anwender  

# 7. Weiterführende Module

- `docs/dev/compare-module.md` — technische Implementierungsdetails  
- `docs/dev/drift-metrics.md` — Metriken und Kennzahlen  
- `docs/quality/drift-experiments.md` — Drift-Testmethodik  
- Experimentmodul: `drift_experiment_gemini.py`  
- Analysemodul: `drift_analysis_core.py`

# 8. Status

Das Compare-Modul ist vollständig in den ALOT2COME Qualitätsprozess integriert  
und bietet eine robuste, wiederholbare Methode zur Beurteilung und Dokumentation von LLM-Stabilität.

