
"""
drift_analysis_core.py
----------------------

Zentrale Analyse-Engine für Drift-Experimente.
Dieses Modul ist vollständig unabhängig vom Experimentcode und bildet die
methodische Grundlage zur Bewertung von Drift in LLM-Antworten.

Funktionen:
- Normalisierung von Texten
- Ähnlichkeitsanalyse (SequenceMatcher)
- Erkennung von hinzugekommenen / entfernten Wörtern
- Strukturdrift (Nummerierte Listen)
- Automatische Driftinterpretation
- Erzeugung eines formatierungssicheren Markdown-Reports

Kann von:
- drift_analysis.py
- drift_experiment_gemini.py (bei Nutzung von --analyze)
- zukünftigen Multi-LLM-Tools
verwendet werden.
"""

import re
from difflib import SequenceMatcher
from collections import Counter


# --------------------------------------------------------
# Normalisierung
# --------------------------------------------------------
def normalize(text: str) -> str:
    """Bereitet Text für Vergleichsanalysen vor (kleine Schrift, reduzierte Zeichen)."""
    text = text.lower()
    text = re.sub(r"[^a-zA-ZäöüÄÖÜ0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# --------------------------------------------------------
# Ähnlichkeitsanalyse
# --------------------------------------------------------
def similarity(a: str, b: str) -> float:
    """Gibt eine Similarität zwischen 0 und 1 zurück."""
    return SequenceMatcher(None, a, b).ratio()


# --------------------------------------------------------
# Wortdifferenzen (Begriffsdrift)
# --------------------------------------------------------
def word_diff(a: str, b: str):
    """
    Liefert hinzugekommene und entfernte Wörter.
    Grundlage zur Erkennung von Begriffsdrift.
    """
    words_a = Counter(a.split())
    words_b = Counter(b.split())

    added = list((words_b - words_a).elements())
    removed = list((words_a - words_b).elements())

    return added, removed


# --------------------------------------------------------
# Strukturdrift-Erkennung (Listen)
# --------------------------------------------------------
def detect_structure_changes(a: str, b: str):
    """
    Prüft auf nummerierte Listen 1., 2., 3. ...
    und gibt Unterschiede zurück.
    """
    pattern = r"(\d+\.\s+[^\n]+)"

    list_a = re.findall(pattern, a)
    list_b = re.findall(pattern, b)

    return list_a, list_b


# --------------------------------------------------------
# Automatische Interpretation
# --------------------------------------------------------
def interpret_similarity(score: float) -> str:
    """Textliche Einschätzung der Driftstärke."""
    if score > 0.90:
        return "Kaum Drift erkennbar."
    if score > 0.75:
        return "Leichte Drift – Definition wurde verändert oder erweitert."
    if score > 0.50:
        return "Deutliche Drift – semantische Verschiebung oder neue Synonyme."
    return "Starke Drift – Definition ist inhaltlich wesentlich verändert."


# --------------------------------------------------------
# Markdown-Report erzeugen
# --------------------------------------------------------
def create_report(data, baseline_index=0, control_index=-1) -> str:
    """
    Erzeugt einen vollständigen Markdown-Driftbericht.
    data: Liste von Prompt/Antwort-Dictionaries aus einem Experiment.
    """

    baseline = data[baseline_index]["answer"]
    control = data[control_index]["answer"]

    base_norm = normalize(baseline)
    ctrl_norm = normalize(control)

    sim = similarity(base_norm, ctrl_norm)
    added_words, removed_words = word_diff(base_norm, ctrl_norm)
    list_a, list_b = detect_structure_changes(baseline, control)
    interpretation = interpret_similarity(sim)

    report = f"""
# 🧪 Drift-Analyse Bericht

## Vergleich
- Baseline: Antwort {baseline_index + 1}
- Kontrollpunkt: Antwort {control_index + 1}
- Ähnlichkeitswert: **{sim:.2f}**

---

## 🔍 Originalantworten

### Baseline
```
{baseline}
```

### Kontrollantwort
```
{control}
```

---

## 📘 Begriffliche Drift

### Neu hinzugekommene Wörter:
{added_words if added_words else "Keine"}

### Entfernte Wörter:
{removed_words if removed_words else "Keine"}

---

## 📐 Strukturdrift

### Liste in Baseline:
{list_a if list_a else "Keine nummerierte Liste"}

### Liste in Kontrollantwort:
{list_b if list_b else "Keine nummerierte Liste"}

---

## 🧩 Interpretation
**{interpretation}**

---

_Ende des Berichts._
"""

    return report
