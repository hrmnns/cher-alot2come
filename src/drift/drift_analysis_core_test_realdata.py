"""
drift_analysis_core_test_realdata.py
------------------------------------

Dieses Testskript lädt eine echte Ergebnisdatei aus dem results/-Verzeichnis
und führt den erweiterten Analyse-Core darauf aus.

Verwendung:
    python drift_analysis_core_test_realdata.py <pfad_zur_json_datei> [--report]
"""

import sys
import os
import json
from datetime import datetime

from drift_analysis_core import (
    compute_similarity_metrics,
    compute_word_drift,
    compute_structure_drift,
    analyze,
    create_report,
)


def load_json(path):
    if not os.path.exists(path):
        raise SystemExit(f"❌ Fehler: Datei nicht gefunden: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def main():

    if len(sys.argv) < 2:
        print("❌ Bitte gib eine Ergebnis-JSON-Datei an.")
        return

    input_path = sys.argv[1]
    print(f"📄 Lade Datei: {input_path}")

    results = load_json(input_path)

    if not isinstance(results, list):
        raise SystemExit("❌ Fehler: JSON muss eine Liste von Einträgen enthalten.")
    if "answer" not in results[0]:
        raise SystemExit("❌ Fehler: JSON hat nicht das erwartete Format ('answer' fehlt).")

    print("\n=== Analyse gestartet ===\n")

    # Similarity
    sim = compute_similarity_metrics(results)
    print("### Similarity")
    print(sim)

    # Wortdrift
    wd = compute_word_drift(results)
    print("\n### Wortdrift")
    print(wd)

    # Strukturdrift
    sd = compute_structure_drift(results)
    print("\n### Strukturdrift")
    print(sd)

    # Gesamtauswertung
    full = analyze(results)
    print("\n### Gesamtauswertung")
    print(full)

    # Optionaler Report
    if "--report" in sys.argv:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        out_path = f"results/drift_report_from_test_{timestamp}.md"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(create_report(results))
        print(f"\n📄 Markdown-Report gespeichert unter:\n{out_path}")

    print("\n=== Analyse abgeschlossen ===\n")


if __name__ == "__main__":
    main()
