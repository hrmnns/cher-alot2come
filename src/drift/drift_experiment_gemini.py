"""
drift_analysis_core_test.py
---------------------------

Ein einfacher manueller Test für das Analyse-Core-Modul (Phase 2a).

Prüft:
- Similarity-Metriken
- Wortbasierte Driftmetriken
- Strukturdrift
- Gesamtauswertung
- Markdown-Report

Kann direkt ausgeführt werden:
    python drift_analysis_core_test.py
"""

from drift_analysis_core import (
    compute_similarity_metrics,
    compute_word_drift,
    compute_structure_drift,
    analyze,
    create_report
)

# ---------------------------------------------------------
# Testdaten (künstlich, minimal und kontrolliert)
# ---------------------------------------------------------

results = [
    {
        "prompt_number": 1,
        "prompt": "Definiere Modul",
        "answer": "Ein Modul ist ein klar abgegrenzter Bestandteil einer WebApp."
    },
    {
        "prompt_number": 2,
        "prompt": "Erkläre das Modul erneut",
        "answer": "Ein Modul ist ein abgegrenzter Teil einer WebApp, der bestimmte Funktionen bereitstellt."
    },
    {
        "prompt_number": 3,
        "prompt": "Beschreibe das Modul erneut",
        "answer": "- Ein Modul ist eine Komponente\n- Es stellt Funktionen bereit"
    }
]

# ---------------------------------------------------------
# Tests
# ---------------------------------------------------------

print("\n=== Starte Tests für drift_analysis_core.py ===\n")

# 1. Similarity
sim = compute_similarity_metrics(results)
print("Similarity:", sim)

# 2. Wortdrift
words = compute_word_drift(results)
print("\nWord Drift:", words)

# 3. Strukturdrift
struct = compute_structure_drift(results)
print("\nStructure Drift:", struct)

# 4. Gesamtauswertung
analysis = analyze(results)
print("\nFull Analysis:", analysis)

# 5. Markdown-Report
report = create_report(results)
print("\nMarkdown-Report:\n")
print(report)

print("\n=== Tests abgeschlossen ===\n")
