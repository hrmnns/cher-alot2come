"""
drift_analysis_core.py
----------------------

Erweiterter Analyse-Core für Driftmessungen.
Implementiert quantitative Metriken (Phase 2a):

- Similarity Metriken
- Wortbasierte Driftmetriken
- Strukturklassifikation
- Strukturdrift
- Analyse-Metadaten
"""

from difflib import SequenceMatcher
import re
import statistics

# ------------------------------------------------------------
# Hilfsfunktionen
# ------------------------------------------------------------

def tokenize(text: str):
    """Einfache Tokenisierung: Wörter extrahieren, klein schreiben."""
    return re.findall(r"\b\w+\b", text.lower())


def classify_format(text: str):
    """
    Klassifiziert den Strukturtyp eines Textes.
    Rückgabe:
        'list-numbered', 'list-bullet', 'definition', 'text'
    """
    lines = [l.strip() for l in text.split("\n") if l.strip()]

    if any(re.match(r"^\d+\.", l) for l in lines):
        return "list-numbered"
    if any(l.startswith("- ") or l.startswith("* ") for l in lines):
        return "list-bullet"
    if "ist" in text.lower() and "ein" in text.lower() and text.lower().strip().endswith("."):
        return "definition"
    return "text"


# ------------------------------------------------------------
# Similarity Analyse
# ------------------------------------------------------------

def compute_similarity_metrics(results):
    """
    Berechnet Similarity pro Prompt, Mittelwert, Varianz und Trend.
    """
    baseline = results[0]["answer"]
    similarities = []

    for entry in results:
        s = SequenceMatcher(None, baseline, entry["answer"]).ratio()
        similarities.append(s)

    mean_val = statistics.mean(similarities)
    var_val = statistics.pvariance(similarities) if len(similarities) > 1 else 0.0

    # Trend: Differenz Zwischen letztem und erstem Wert
    trend = similarities[-1] - similarities[0]

    return {
        "similarities": similarities,
        "mean": mean_val,
        "variance": var_val,
        "trend": trend
    }


# ------------------------------------------------------------
# Wortbasierte Driftmetriken
# ------------------------------------------------------------

def compute_word_drift(results):
    """
    Berechnet Added Words, Removed Words und Drift Ratios.
    """
    baseline_tokens = set(tokenize(results[0]["answer"]))

    added_list = []
    removed_list = []
    drift_ratios = []

    baseline_len = max(1, len(baseline_tokens))

    for entry in results:
        tokens = set(tokenize(entry["answer"]))

        added = tokens - baseline_tokens
        removed = baseline_tokens - tokens

        added_list.append(list(added))
        removed_list.append(list(removed))

        drift_ratio = (len(added) + len(removed)) / baseline_len
        drift_ratios.append(drift_ratio)

    return {
        "added_words": added_list,
        "removed_words": removed_list,
        "drift_ratio": drift_ratios
    }


# ------------------------------------------------------------
# Strukturdrift
# ------------------------------------------------------------

def compute_structure_drift(results):
    """
    Klassifiziert Format pro Antwort und zählt Strukturwechsel.
    """
    formats = []
    for entry in results:
        fmt = classify_format(entry["answer"])
        formats.append(fmt)

    structure_changes = sum(1 for i in range(1, len(formats)) if formats[i] != formats[i-1])

    return {
        "formats": formats,
        "structure_changes": structure_changes
    }


# ------------------------------------------------------------
# Gesamtauswertung & Report
# ------------------------------------------------------------

def analyze(results):
    """
    Führt alle quantitativen Analysen durch und gibt Metadaten zurück.
    """
    similarity = compute_similarity_metrics(results)
    word_drift = compute_word_drift(results)
    structure = compute_structure_drift(results)

    return {
        "similarity": similarity,
        "word_drift": word_drift,
        "structure": structure
    }


def create_report(results):
    """
    Erzeugt einen Markdown-Report basierend auf den quantitativen Metriken.
    """
    analysis = analyze(results)

    sim = analysis["similarity"]
    drift = analysis["word_drift"]
    struct = analysis["structure"]

    md = []
    md.append("# Driftanalyse – Quantitative Ergebnisse\n")

    # Similarity
    md.append("## Similarity\n")
    md.append(f"- Mittelwert: {sim['mean']:.3f}")
    md.append(f"- Varianz: {sim['variance']:.4f}")
    md.append(f"- Trend: {sim['trend']:.3f}")
    md.append("\n### Similarity pro Prompt:")
    for i, val in enumerate(sim["similarities"], 1):
        md.append(f"- Prompt {i}: {val:.3f}")

    # Wortdrift
    md.append("\n\n## Wortbasierte Drift\n")
    for i, ratio in enumerate(drift["drift_ratio"], 1):
        md.append(f"- Prompt {i}: Drift Ratio = {ratio:.3f}")

    # Strukturdrift
    md.append("\n\n## Strukturdrift\n")
    md.append(f"- Strukturwechsel: {struct['structure_changes']}")
    md.append("\n### Formate:")
    for i, fmt in enumerate(struct["formats"], 1):
        md.append(f"- Prompt {i}: {fmt}")

    return "\n".join(md)
