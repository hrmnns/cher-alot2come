"""
drift_visualization.py
----------------------

Minimalistische Visualisierungen für Driftanalysen.
Erzeugt funktionale, wissenschaftlich neutrale Diagramme.

Unterstützt:
- Similarity-Verlauf
- Wortdrift (Drift Ratio)
- Strukturdrift
- vollständige Analyse-Plots
- Vergleichsplots (Baseline vs Persistenz)

Verwendung (Analyse):
    python drift_visualization.py results/baseline.json --analysis

Verwendung (Compare):
    python drift_visualization.py results/compare_baseline_vs_persist.json --compare
"""

import sys
import os
import json
import matplotlib.pyplot as plt
from datetime import datetime

from drift_analysis_core import analyze


# ---------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------

def load_json(path: str):
    if not os.path.exists(path):
        raise SystemExit(f"❌ Datei nicht gefunden: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def ensure_plot_dir():
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    folder = f"results/plots/{timestamp}"
    os.makedirs(folder, exist_ok=True)
    return folder


def save_plot(path: str):
    plt.tight_layout()
    plt.savefig(path, dpi=120)
    plt.close()


# ---------------------------------------------------------
# Plot-Funktionen für Einzelanalyse
# ---------------------------------------------------------

def plot_similarity(similarities, out_path):
    x = list(range(1, len(similarities) + 1))

    plt.figure()
    plt.plot(x, similarities, marker="o", linewidth=1)
    plt.title("Similarity-Verlauf")
    plt.xlabel("Prompt")
    plt.ylabel("Similarity")
    plt.grid(True, linewidth=0.3)
    save_plot(out_path)


def plot_word_drift(drift_ratios, out_path):
    x = list(range(1, len(drift_ratios) + 1))

    plt.figure()
    plt.plot(x, drift_ratios, marker="o", linewidth=1)
    plt.title("Wortdrift (Drift Ratio)")
    plt.xlabel("Prompt")
    plt.ylabel("Drift Ratio")
    plt.grid(True, linewidth=0.3)
    save_plot(out_path)


def plot_structure(formats, out_path):
    x = list(range(1, len(formats) + 1))
    y = list(range(len(formats)))

    # Struktur in numerische Werte überführen
    fmt_map = {fmt: i for i, fmt in enumerate(sorted(set(formats)))}
    y_numeric = [fmt_map[f] for f in formats]

    plt.figure()
    plt.plot(x, y_numeric, marker="o", linewidth=1)
    plt.title("Strukturdrift (Formatänderungen)")
    plt.xlabel("Prompt")
    plt.ylabel("Strukturtyp (numerisch)")
    plt.grid(True, linewidth=0.3)
    save_plot(out_path)


def plot_drift_heatmap(drift_types, out_path):
    """
    Drift-Arten-Heatmap:
    Zeigt für jeden Prompt (x) die Driftarten (y).
    """
    # Driftarten definieren
    all_types = ["semantic", "word", "structure", "role", "context"]

    # Matrix generieren
    matrix = []
    for t in all_types:
        row = []
        for prompt_types in drift_types:
            row.append(1 if t in prompt_types else 0)
        matrix.append(row)

    plt.figure()
    plt.imshow(matrix, cmap="Greys", aspect="auto")
    plt.yticks(range(len(all_types)), all_types)
    plt.xlabel("Prompt")
    plt.title("Drift-Heatmap")
    save_plot(out_path)


# ---------------------------------------------------------
# Vergleichsplots
# ---------------------------------------------------------

def plot_intensity_compare(baseline_intensity, other_intensity, labels, out_path):
    plt.figure()
    plt.bar([0, 1], [baseline_intensity, other_intensity])
    plt.xticks([0, 1], labels)
    plt.ylabel("Driftintensität")
    plt.title("Driftintensität: Baseline vs Vergleich")
    save_plot(out_path)


# ---------------------------------------------------------
# Hauptfunktionen
# ---------------------------------------------------------

def generate_analysis_plots(results_json_path):
    results = load_json(results_json_path)
    analysis = analyze(results)

    folder = ensure_plot_dir()

    sim = analysis["similarity"]["similarities"]
    drift = analysis["word_drift"]["drift_ratio"]
    struct = analysis["structure"]["formats"]
    drift_types = analysis["qualitative"]["drift_types"]

    plot_similarity(sim, f"{folder}/similarity.png")
    plot_word_drift(drift, f"{folder}/word_drift.png")
    plot_structure(struct, f"{folder}/structure.png")
    plot_drift_heatmap(drift_types, f"{folder}/heatmap.png")

    print(f"📊 Plots gespeichert unter: {folder}")


def generate_compare_plots(compare_json_path):
    data = load_json(compare_json_path)
    comparison = data["comparison"]

    folder = ensure_plot_dir()

    baseline_intensity = comparison["intensity_baseline"]
    other_intensity = comparison["intensity_other"]
    labels = ["Baseline", "Andere"]

    plot_intensity_compare(
        baseline_intensity,
        other_intensity,
        labels,
        f"{folder}/compare_intensity.png"
    )

    print(f"📊 Vergleichsplots gespeichert unter: {folder}")


# ---------------------------------------------------------
# CLI
# ---------------------------------------------------------

def main():
    if len(sys.argv) < 3:
        print("Verwendung:")
        print("  python drift_visualization.py FILE.json --analysis")
        print("  python drift_visualization.py FILE.json --compare")
        sys.exit(1)

    path = sys.argv[1]

    if "--analysis" in sys.argv:
        generate_analysis_plots(path)
    elif "--compare" in sys.argv:
        generate_compare_plots(path)
    else:
        print("❌ Bitte --analysis oder --compare angeben.")


if __name__ == "__main__":
    main()
