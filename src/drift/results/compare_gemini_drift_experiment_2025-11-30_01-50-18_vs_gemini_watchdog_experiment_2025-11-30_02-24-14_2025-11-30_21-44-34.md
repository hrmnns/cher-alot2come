# Driftvergleich – Baseline vs. Alternativlauf

## Überblick

- Baseline: **gemini_drift_experiment_2025-11-30_01-50-18**
- Vergleichslauf: **gemini_watchdog_experiment_2025-11-30_02-24-14**

## Similarity (Durchschnitt)

| Lauf | Similarity Ø |
|------|--------------|
| gemini_drift_experiment_2025-11-30_01-50-18  | 0.066 |
| gemini_watchdog_experiment_2025-11-30_02-24-14 | 0.086 |

- Differenz (Andere - Baseline): **0.020**

## Wortdrift (Drift Ratio Ø)

| Lauf | Drift Ratio Ø |
|------|---------------|
| gemini_drift_experiment_2025-11-30_01-50-18  | 20.857 |
| gemini_watchdog_experiment_2025-11-30_02-24-14 | 4.974 |

- Differenz (Andere - Baseline): **-15.883**

## Strukturdrift (Strukturwechsel gesamt)

| Lauf | Strukturwechsel |
|------|-----------------|
| gemini_drift_experiment_2025-11-30_01-50-18  | 28 |
| gemini_watchdog_experiment_2025-11-30_02-24-14 | 27 |

- Differenz (Andere - Baseline): **-1**

## Rollendrift

| Lauf | Rollenwechsel |
|------|---------------|
| gemini_drift_experiment_2025-11-30_01-50-18  | 2 |
| gemini_watchdog_experiment_2025-11-30_02-24-14 | 0 |

- Differenz (Andere - Baseline): **-2**

## Kontext-/Domänendrift

| Lauf | Domänenwechsel |
|------|----------------|
| gemini_drift_experiment_2025-11-30_01-50-18  | 25 |
| gemini_watchdog_experiment_2025-11-30_02-24-14 | 5 |

- Differenz (Andere - Baseline): **-20**

## Aggregierte Driftintensität

| Lauf | Drift-Intensität |
|------|------------------|
| gemini_drift_experiment_2025-11-30_01-50-18  | 4.802 |
| gemini_watchdog_experiment_2025-11-30_02-24-14 | 1.574 |

- Driftreduktion (1 - Intensität_Andere / Intensität_Baseline): **67.2%**

---

## Interpretation (Hinweise)

- In Bezug auf semantische Ähnlichkeit sind beide Läufe relativ ähnlich.
- Der Vergleichslauf (**gemini_watchdog_experiment_2025-11-30_02-24-14**) reduziert Wortdrift gegenüber der Baseline spürbar.
- gemini_watchdog_experiment_2025-11-30_02-24-14 zeigt stabilere Antwortstrukturen als gemini_drift_experiment_2025-11-30_01-50-18.
- Der Vergleichslauf reduziert Rollendrift gegenüber der Baseline.
- Der Vergleichslauf reduziert Kontext-/Domänendrift gegenüber der Baseline.
- Insgesamt reduziert gemini_watchdog_experiment_2025-11-30_02-24-14 die Drift deutlich gegenüber gemini_drift_experiment_2025-11-30_01-50-18.