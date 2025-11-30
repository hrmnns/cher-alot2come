# Drift-Metriken – Erklärung, Berechnung und methodische Bedeutung (GitHub-kompatible ASCII-Version)

Dieses Dokument beschreibt alle Metriken, die in der Driftanalyse des ALOT2COME-Frameworks eingesetzt werden – ohne LaTeX-Notation, vollständig kompatibel zu GitHub Markdown.

Alle Formeln sind in klarer ASCII-Schreibweise dargestellt.

# 1. Semantische Metriken (Similarity)

Diese Metriken messen, wie ähnlich spätere Antworten zur ursprünglichen Baseline-Antwort sind.

## 1.1 Similarity Score

Der Similarity Score basiert auf der Zeichenähnlichkeit zwischen zwei Texten.

**Formel (ASCII):**

```
Similarity(A, B) = (2 * M) / (len(A) + len(B))
```

- A = Baseline-Text
- B = späterer Text
- M = Anzahl übereinstimmender Zeichenfolgen (gemäß SequenceMatcher)

**Interpretation:**

| Wert | Bedeutung |
|------|-----------|
| 1.0  | identisch |
| >0.8 | kaum Drift |
| 0.6–0.8 | leichte Drift |
| 0.4–0.6 | deutliche Drift |
| <0.4 | starke Drift |

## 1.2 Similarity-Verlauf

Die Similarity pro Prompt ergibt eine Zeitreihe:

```
S = [s1, s2, ..., sn]
```

Analyse:
- Trend (fallend = zunehmender Drift)
- Ausreißer
- Stabilität

## 1.3 Similarity-Varianz

Misst, wie stark die Similarity schwankt.

**Formel (ASCII):**

```
Var(S) = (1/n) * sum( (si - mean(S))^2 )
```

Hohe Varianz → instabile Antworten → Drift.

# 2. Wortbasierte Metriken (Word Drift)

Diese Metriken untersuchen Veränderungen in der Wortmenge einer Antwort.

Alle Wörter werden extrahiert, bereinigt und verglichen:

```
Words(T) = tokenize(T) - stopwords
```

## 2.1 Added Words

Wörter, die neu hinzukommen:

```
Added_i = Words_i - Words_baseline
```

## 2.2 Removed Words

Wörter, die im Vergleich zur Baseline fehlen:

```
Removed_i = Words_baseline - Words_i
```

Diese Metrik zeigt insbesondere Definitionsverlust.

## 2.3 Word Drift Ratio

Gesamthöhe der Wortveränderung:

```
Drift_i = count(Added_i) + count(Removed_i)
```

Normiert:

```
DriftNorm_i = Drift_i / count(Words_baseline)
```

# 3. Strukturmetriken (Strukturdrift)

Diese Metriken messen Änderungen in Stil, Aufbau und Format der Antwort.

## 3.1 Format Classification

Antwort wird klassifiziert in:

- "text"
- "list-numbered"
- "list-bullet"
- "definition"
- "metaphor"
- "analogy"

Formal:

```
Format(T) = one of the types above
```

## 3.2 Strukturwechsel-Index

Zählt Strukturänderungen zwischen Prompts:

```
StructureDrift = sum over i=2..n of ( Format_i != Format_(i-1) )
```

## 3.3 Veränderung der Listenlängen

Wenn Listen vorkommen:

```
DeltaList_i = len(List_i) - len(List_baseline)
```

# 4. Rollen- und Kontextmetriken

Diese Metriken erkennen Wechsel der Perspektive oder Zielgruppe der Antwort.

## 4.1 Role Detection

Eine Rolle wird erkannt, wenn im Text Formulierungen auftreten wie:

- "Als Architekt..."
- "Aus Sicht eines Projektmanagers..."
- "Als UX-Designer..."

Formale Definition:

```
Role(T) = RoleName or None
```

## 4.2 Role Drift Index

Zählt Rollenwechsel:

```
RoleDrift = sum over i=2..n of ( Role_i != Role_(i-1) )
```

## 4.3 Domain Classification

Erkennt Domänenverschiebungen, z. B.:

- Software
- Maschinenbau
- Pädagogik
- Architektur

Definition:

```
Domain(T) = one of the known domains
```

## 4.4 Domain Drift Index

```
DomainDrift = sum over i=2..n of ( Domain_i != Domain_(i-1) )
```

# 5. Aggregierte Driftmetriken

Diese kombinieren mehrere Einzelmetriken zu transparenten Gesamtwerten.

## 5.1 Drift Intensity Score

Eine gewichtete Kombination mehrerer Driftindikatoren:

```
Intensity_i =
    w1 * (1 - Similarity_i)
  + w2 * DriftNorm_i
  + w3 * (Format_i != Format_1)
  + w4 * (Role_i != Role_1)
```

Empfohlene Gewichte:

```
w1 = 0.5
w2 = 0.2
w3 = 0.2
w4 = 0.1
```

## 5.2 Stability Score

Inverse der Driftintensität:

```
Stability_i = 1 - Intensity_i
```

## 5.3 Drift Reduction Score (Baseline vs Persistenz)

Misst die Wirksamkeit eines Persistenzmodus:

```
Reduction = 1 - (Intensity_persist / Intensity_baseline)
```

Interpretation:

| Wert | Bedeutung |
|------|-----------|
| 1.0 | Drift vollständig verhindert |
| 0.5 | Drift halbiert |
| 0.0 | keine Verbesserung |

# 6. Bedeutung für ALOT2COME

Diese Metriken ermöglichen eine vollständig nachvollziehbare Driftbewertung:

- objektiv messbar
- zwischen Quality-Modes vergleichbar
- wissenschaftlich methodisch
- geeignet für Analysen, Reports und Visualisierungen

Sie sind die Grundlage für:

- Driftdiagnose
- Persistenzprüfung
- Qualitätsmodi-Bewertung
- Langzeit-Langstreckenexperimente
- methodische Argumentation im Projekt ALOT2COME

# 7. Weiterführende Dokumente

- docs/dev/drift-tests.md
- docs/quality/drift_example_run.md
- docs/quality/drift-experiments.md
