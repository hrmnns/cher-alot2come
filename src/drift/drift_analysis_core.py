"""
drift_analysis_core.py
----------------------

Erweiterter Analyse-Core für Driftmessungen.

Implementiert:
- Quantitative Metriken (Similarity, Wortdrift, Strukturdrift)
- Qualitative Analyse (Driftarten, Rollen-/Kontextdrift, Zusammenfassung)
"""

from difflib import SequenceMatcher
import re
import statistics
from typing import List, Dict, Any


# ------------------------------------------------------------
# Hilfsfunktionen
# ------------------------------------------------------------

def tokenize(text: str) -> List[str]:
    """Einfache Tokenisierung: Wörter extrahieren, klein schreiben."""
    return re.findall(r"\b\w+\b", text.lower())


def classify_format(text: str) -> str:
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
    # sehr einfache Heuristik für Definitionssätze
    if " ist " in text.lower() and text.strip().endswith("."):
        return "definition"
    return "text"


# ------------------------------------------------------------
# Quantitative Analysis
# ------------------------------------------------------------

def compute_similarity_metrics(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Berechnet Similarity pro Prompt, Mittelwert, Varianz und Trend.
    """
    baseline = results[0]["answer"]
    similarities: List[float] = []

    for entry in results:
        s = SequenceMatcher(None, baseline, entry["answer"]).ratio()
        similarities.append(s)

    mean_val = statistics.mean(similarities)
    var_val = statistics.pvariance(similarities) if len(similarities) > 1 else 0.0
    trend = similarities[-1] - similarities[0]

    return {
        "similarities": similarities,
        "mean": mean_val,
        "variance": var_val,
        "trend": trend,
    }


def compute_word_drift(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Berechnet Added Words, Removed Words und Drift Ratios.
    """
    baseline_tokens = set(tokenize(results[0]["answer"]))

    added_list: List[List[str]] = []
    removed_list: List[List[str]] = []
    drift_ratios: List[float] = []

    baseline_len = max(1, len(baseline_tokens))

    for entry in results:
        tokens = set(tokenize(entry["answer"]))

        added = tokens - baseline_tokens
        removed = baseline_tokens - tokens

        added_list.append(sorted(added))
        removed_list.append(sorted(removed))

        drift_ratio = (len(added) + len(removed)) / baseline_len
        drift_ratios.append(drift_ratio)

    return {
        "added_words": added_list,
        "removed_words": removed_list,
        "drift_ratio": drift_ratios,
        "baseline_tokens": sorted(baseline_tokens),
    }


def compute_structure_drift(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Klassifiziert Format pro Antwort und zählt Strukturwechsel.
    """
    formats: List[str] = []
    for entry in results:
        fmt = classify_format(entry["answer"])
        formats.append(fmt)

    structure_changes = sum(
        1 for i in range(1, len(formats)) if formats[i] != formats[i - 1]
    )

    return {
        "formats": formats,
        "structure_changes": structure_changes,
    }


# ------------------------------------------------------------
# Qualitative Analysis
# ------------------------------------------------------------

def detect_semantic_drift(similarities: List[float]) -> Dict[str, Any]:
    """
    Ermittelt semantische Driftbereiche anhand der Similarity-Werte.
    Moderat sensibel:
    - Drift-Hinweis, wenn Similarity < 0.8
    - Starker Drift, wenn Similarity < 0.6
    """
    flags = []
    strong_flags = []
    for s in similarities:
        flags.append(s < 0.8)
        strong_flags.append(s < 0.6)

    segments = []
    current_start = None
    for i, flag in enumerate(flags):
        if flag and current_start is None:
            current_start = i
        elif not flag and current_start is not None:
            segments.append((current_start, i - 1))
            current_start = None
    if current_start is not None:
        segments.append((current_start, len(flags) - 1))

    severity = "low"
    mean_sim = statistics.mean(similarities)
    if mean_sim < 0.8:
        severity = "medium"
    if mean_sim < 0.6:
        severity = "high"

    return {
        "flags": flags,
        "strong_flags": strong_flags,
        "segments": segments,
        "severity": severity,
        "mean_similarity": mean_sim,
    }


def detect_word_drift_qualitative(word_drift: Dict[str, Any]) -> Dict[str, Any]:
    """
    Interpretiert Wortdrift qualitativ auf Basis der Drift Ratios.
    """
    ratios = word_drift["drift_ratio"]
    added_words = word_drift["added_words"]
    removed_words = word_drift["removed_words"]

    flags = [r > 0.1 for r in ratios]   # moderater Schwellenwert
    strong_flags = [r > 0.3 for r in ratios]

    severity = "low"
    avg_ratio = statistics.mean(ratios) if ratios else 0.0
    if avg_ratio > 0.1:
        severity = "medium"
    if avg_ratio > 0.3:
        severity = "high"

    loss_counts = [len(r) for r in removed_words]
    max_loss = max(loss_counts) if loss_counts else 0

    return {
        "flags": flags,
        "strong_flags": strong_flags,
        "severity": severity,
        "avg_ratio": avg_ratio,
        "max_loss": max_loss,
    }


def detect_structure_drift_qualitative(structure: Dict[str, Any]) -> Dict[str, Any]:
    """
    Interpretiert Strukturdrift qualitativ.
    """
    formats = structure["formats"]
    changes = structure["structure_changes"]

    severity = "low"
    if changes >= 2:
        severity = "medium"
    if changes >= 4:
        severity = "high"

    return {
        "severity": severity,
        "changes": changes,
        "formats": formats,
    }


ROLE_PATTERNS = [
    r"^als\s+\w+",
    r"aus sicht",
    r"in der rolle",
    r"du agierst",
]


def detect_role_drift(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Ermittelt einfache Rollendrift anhand von Rollenphrasen.
    """
    roles: List[str] = []
    for entry in results:
        text = entry["answer"].lower()
        role = None
        for pattern in ROLE_PATTERNS:
            m = re.search(pattern, text)
            if m:
                role = m.group(0)
                break
        roles.append(role)

    baseline_role = roles[0]
    flags = []
    for r in roles:
        flags.append(r is not None and r != baseline_role)

    changes = sum(1 for f in flags if f)

    severity = "none"
    if changes > 0:
        severity = "low"
    if changes > 2:
        severity = "medium"

    return {
        "roles": roles,
        "baseline_role": baseline_role,
        "flags": flags,
        "changes": changes,
        "severity": severity,
    }


DOMAIN_KEYWORDS = {
    "softwarearchitektur": [
        "modul",
        "komponente",
        "schnittstelle",
        "api",
        "microservice",
        "architektur",
    ],
    "webapp-struktur": [
        "webapp",
        "frontend",
        "ui",
        "ux",
        "layout",
        "komposition",
        "anzeige",
    ],
    "prompt-engineering": [
        "prompt",
        "kontext",
        "rolle",
        "drift",
        "persistenz",
        "anweisung",
        "modell",
        "llm",
    ],
    "methodologie-prozess": [
        "methode",
        "framework",
        "prozess",
        "macroprozess",
        "mikroprozess",
        "workflow",
        "handover",
        "qualität",
    ],
    "kollaboration-wissen": [
        "kommunikation",
        "zusammenarbeit",
        "team",
        "stakeholder",
        "wissensarbeit",
        "übergabe",
    ],
    "it-management": [
        "system",
        "infrastruktur",
        "deployment",
        "governance",
        "tooling",
    ],
}


def detect_context_drift(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Ermittelt Kontext-/Domänendrift anhand einfacher Stichwörter.
    Nutzt das projektspezifische Domainschema.
    """
    domains: List[str] = []
    for entry in results:
        text = entry["answer"].lower()
        best_domain = "unknown"
        best_score = 0
        for domain, keywords in DOMAIN_KEYWORDS.items():
            score = sum(1 for kw in keywords if kw in text)
            if score > best_score:
                best_score = score
                best_domain = domain
        domains.append(best_domain)

    baseline_domain = domains[0]
    flags = [d != baseline_domain for d in domains]

    changes = sum(1 for f in flags if f and baseline_domain != "unknown")

    severity = "none"
    if changes > 0:
        severity = "low"
    if changes > 2:
        severity = "medium"

    return {
        "domains": domains,
        "baseline_domain": baseline_domain,
        "flags": flags,
        "changes": changes,
        "severity": severity,
    }


def classify_drift_types(
    similarities: List[float],
    word_drift: Dict[str, Any],
    structure: Dict[str, Any],
    role_info: Dict[str, Any],
    context_info: Dict[str, Any],
) -> List[List[str]]:
    """
    Ordnet jedem Prompt eine Liste von Drift-Typen zu.
    Mögliche Typen:
    - semantic
    - word
    - structure
    - role
    - context
    """
    n = len(similarities)
    drift_types: List[List[str]] = [[] for _ in range(n)]

    # semantische Drift
    for i, s in enumerate(similarities):
        if s < 0.8:
            drift_types[i].append("semantic")

    # Wortdrift
    for i, ratio in enumerate(word_drift["drift_ratio"]):
        if ratio > 0.1:
            drift_types[i].append("word")

    # Strukturdrift
    formats = structure["formats"]
    baseline_fmt = formats[0]
    for i, fmt in enumerate(formats):
        if fmt != baseline_fmt:
            drift_types[i].append("structure")

    # Rollendrift
    for i, flag in enumerate(role_info["flags"]):
        if flag:
            drift_types[i].append("role")

    # Kontextdrift
    for i, flag in enumerate(context_info["flags"]):
        if flag and context_info["baseline_domain"] != "unknown":
            drift_types[i].append("context")

    return drift_types


def summarize_drift(
    similarities: List[float],
    word_drift: Dict[str, Any],
    structure: Dict[str, Any],
    role_info: Dict[str, Any],
    context_info: Dict[str, Any],
    drift_types: List[List[str]],
) -> Dict[str, Any]:
    """
    Erzeugt eine narrative Zusammenfassung der wichtigsten Driftaspekte.
    """
    # Dominante Driftarten zählen
    type_counts = {"semantic": 0, "word": 0, "structure": 0, "role": 0, "context": 0}
    for types in drift_types:
        for t in types:
            if t in type_counts:
                type_counts[t] += 1

    max_count = max(type_counts.values()) if type_counts else 0
    dominant = [t for t, c in type_counts.items() if c == max_count and c > 0]

    # stärkster semantischer Driftpunkt (kleinste Similarity)
    min_sim = min(similarities)
    min_index = similarities.index(min_sim)  # 0-basiert

    # stärkste Wortdrift
    ratios = word_drift["drift_ratio"]
    max_ratio = max(ratios) if ratios else 0.0
    max_ratio_index = ratios.index(max_ratio) if ratios else 0

    summary_lines = []

    if dominant:
        summary_lines.append("Dominante Driftarten: " + ", ".join(dominant))
    else:
        summary_lines.append("Es wurden keine dominanten Driftarten erkannt.")

    summary_lines.append(
        f"Stärkste semantische Abweichung bei Prompt {min_index + 1} (Similarity = {min_sim:.3f})."
    )
    summary_lines.append(
        f"Stärkste Wortdrift bei Prompt {max_ratio_index + 1} (Drift Ratio = {max_ratio:.3f})."
    )

    if structure["structure_changes"] > 0:
        summary_lines.append(
            f"Es wurden {structure['structure_changes']} Strukturwechsel erkannt (z. B. Wechsel zwischen Text und Listenform)."
        )

    if role_info["changes"] > 0:
        summary_lines.append(
            f"Rollendrift: {role_info['changes']} Rollenwechsel relativ zur Ausgangsrolle."
        )

    if context_info["changes"] > 0 and context_info["baseline_domain"] != "unknown":
        summary_lines.append(
            f"Kontextdrift: {context_info['changes']} Domänenwechsel gegenüber der Ausgangsdomäne '{context_info['baseline_domain']}'."
        )

    summary_text = "\n".join(summary_lines)

    return {
        "dominant_types": dominant,
        "type_counts": type_counts,
        "strongest_semantic_prompt": min_index + 1,
        "strongest_word_prompt": max_ratio_index + 1,
        "text": summary_text,
    }


# ------------------------------------------------------------
# Gesamtauswertung & Report
# ------------------------------------------------------------

def analyze(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Führt quantitative UND qualitative Analysen durch
    und gibt eine strukturierte Metadatenstruktur zurück.
    """
    similarity = compute_similarity_metrics(results)
    word_drift = compute_word_drift(results)
    structure = compute_structure_drift(results)

    # qualitative Auswertung
    semantic_info = detect_semantic_drift(similarity["similarities"])
    word_info = detect_word_drift_qualitative(word_drift)
    structure_info = detect_structure_drift_qualitative(structure)
    role_info = detect_role_drift(results)
    context_info = detect_context_drift(results)

    drift_types = classify_drift_types(
        similarity["similarities"], word_drift, structure, role_info, context_info
    )
    drift_summary = summarize_drift(
        similarity["similarities"],
        word_drift,
        structure,
        role_info,
        context_info,
        drift_types,
    )

    return {
        "similarity": similarity,
        "word_drift": word_drift,
        "structure": structure,
        "qualitative": {
            "semantic": semantic_info,
            "word": word_info,
            "structure": structure_info,
            "role": role_info,
            "context": context_info,
            "drift_types": drift_types,
            "summary": drift_summary,
        },
    }


def create_report(results: List[Dict[str, Any]]) -> str:
    """
    Erzeugt einen Markdown-Report basierend auf den quantitativen und
    qualitativen Metriken.
    """
    analysis = analyze(results)

    sim = analysis["similarity"]
    drift = analysis["word_drift"]
    struct = analysis["structure"]
    qual = analysis["qualitative"]

    md: List[str] = []
    md.append("# Driftanalyse – Ergebnisse\n")

    # --------------------------------------------------------
    # Quantitative Ergebnisse
    # --------------------------------------------------------
    md.append("## Quantitative Metriken\n")

    # Similarity
    md.append("### Similarity")
    md.append(f"- Mittelwert: {sim['mean']:.3f}")
    md.append(f"- Varianz: {sim['variance']:.4f}")
    md.append(f"- Trend: {sim['trend']:.3f}")
    md.append("\n#### Similarity pro Prompt:")
    for i, val in enumerate(sim["similarities"], 1):
        md.append(f"- Prompt {i}: {val:.3f}")

    # Wortdrift
    md.append("\n\n### Wortbasierte Drift")
    for i, ratio in enumerate(drift["drift_ratio"], 1):
        md.append(f"- Prompt {i}: Drift Ratio = {ratio:.3f}")

    # Strukturdrift
    md.append("\n\n### Strukturdrift")
    md.append(f"- Strukturwechsel gesamt: {struct['structure_changes']}")
    md.append("\n#### Formate pro Prompt:")
    for i, fmt in enumerate(struct["formats"], 1):
        md.append(f"- Prompt {i}: {fmt}")

    # --------------------------------------------------------
    # Qualitative Ergebnisse
    # --------------------------------------------------------
    md.append("\n\n## Qualitative Driftanalyse")

    summary_text = qual["summary"]["text"]
    md.append("\n### Zusammenfassung")
    md.append(summary_text)

    # Dominante Driftarten im Detail
    md.append("\n\n### Dominante Driftarten (Verteilung)")
    for t, c in qual["summary"]["type_counts"].items():
        md.append(f"- {t}: {c} betroffene Prompts")

    # Kontext- und Rollendrift kurz darstellen
    role_info = qual["role"]
    context_info = qual["context"]

    md.append("\n\n### Rollendrift")
    md.append(f"- Ausgangsrolle: {role_info['baseline_role']}")
    md.append(f"- Rollenwechsel: {role_info['changes']}")
    md.append(f"- Einschätzung: {role_info['severity']}")

    md.append("\n\n### Kontext-/Domänendrift")
    md.append(f"- Ausgangsdomäne: {context_info['baseline_domain']}")
    md.append(f"- Domänenwechsel: {context_info['changes']}")
    md.append(f"- Einschätzung: {context_info['severity']}")

    return "\n".join(md)
