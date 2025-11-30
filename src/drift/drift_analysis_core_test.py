"""
drift_analysis_core_test_realdata.py
------------------------------------

Dieses Testskript lädt eine echte Ergebnisdatei aus dem results/-Verzeichnis
(also z. B. ein Ergebnis eines Gemini-Experiments) und führt den erweiterten
Analyse-Core darauf aus.

Verwendung:
    python drift_analysis_core_test_realdata.py <pfad_zur_json_datei>

Beispiel:
    python drift_analysis_core_test_realdata.py results/gemini_baseline_experiment_2025-01-01_12-00-00.json

Funktionen:
- lädt echte Daten
- validiert Struktur des JSON
- ruft alle Analysefunktionen auf
- zeigt Ergebnisse in der Konsole
- erstellt optional einen Markdown-Report im results/-Verzeichnis
"""

import sys
import os
import json
from datetime import datetime

# Analyse-Core importieren
from drift_analysis_core import (
    compute_similarity_metrics,
    compute_word_drift,
    compute_structure_drift,
    analyze,
    create_report
)

# ---------------------------------------------------------
# Hauptlogik
# ---------------------------------------------------------

def load_json(path):
    if not os.path.exists(path):
        raise SystemExit(f"❌ Fehler: Datei nicht gefunden: {path}")

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():

    if len(sys.argv) < 2:
        print("❌ Bitte gib eine Ergebnis-JSON-Datei an.")
        print("Beispiel:")
        print("  python drift_analysis_core_test_realdata.py results/gemini_baseline_experiment_xxxx.json")
        return

    input_path = sys.argv[1]
    print(f"📄 Lade Datei: {input_path}")

    results = load_json(input_path)

    # Minimalvalidierung
    if not isinstance(results, list):
        raise SystemExit("❌ Fehler: JSON muss eine Liste von Einträgen enthalten.")
    if "answer" not in results[0]:
        raise SystemExit("❌ Fehler: JSON hat nicht das erwartete Format ('answer' fehlt).")

    print("\n=== Echte Daten geladen – starte Analyse ===\n")

    # --- Similarity ---
    sim = compute_similarity_metrics(results)
    print("### Similarity")
    print(sim)

    # --- Wortdrift ---
    wd = compute_word_drift(results)
    print("\n### Wortdrift")
    print(wd)

    # --- Strukturdrift ---
    sd = compute_structure_drift(results)
    print("\n### Strukturdrift")
    print(sd)

    # --- Vollanalyse ---
    full = analyze(results)
    print("\n### Gesamtauswertung")
    print(full)

    # ---------------------------------------------------------
    # Optional: Markdown-Report erzeugen
    # ---------------------------------------------------------

    create_report_flag = "--report" in sys.argv

    if create_report_flag:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        out_path = f"results/drift_report_from_test_{timestamp}.md"

        md = create_report(results)

        with open(out_path, "w", encoding="utf-8") as f:
            f.write(md)

        print(f"\n📄 Markdown-Report gespeichert unter:\n{out_path}")

    print("\n=== Analyse abgeschlossen ===\n")


if __name__ == "__main__":
    main()
