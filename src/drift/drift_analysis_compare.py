"""
drift_analysis_compare.py
-------------------------

Vergleicht zwei Drift-Analysen (z. B. Baseline vs. Persistenzmodus)
auf Basis der Analyse-Ergebnisse aus drift_analysis_core.analyze().

Funktionen:

- Lädt zwei Ergebnis-JSON-Dateien (Experimente)
- Führt die Analyse für beide Läufe durch
- Berechnet Vergleichsmetriken (Similarity, Wortdrift, Struktur, Rolle, Kontext)
- Berechnet einen aggregierten Drift-Intensitäts-Score je Lauf
- Ermittelt eine Drift-Reduktion
- Erzeugt einen Markdown-Vergleichsreport

Verwendung (aus dem Projekt-Root oder src-Verzeichnis):

    python drift_analysis_compare.py baseline.json persist.json --out-md --out-json

Beispiele:

    python src/drift/drift_analysis_compare.py results/gemini_baseline_experiment.json results/gemini_persist-hard_experiment.json --out-md

"""

import sys
import os
import json
from datetime import datetime
from typing import Any, Dict

from drift_analysis_core import analyze


# ---------------------------------------------------------
# Hilfsfunktionen
# ---------------------------------------------------------

def load_results(path: str):
    """Lädt eine Ergebnis-JSON-Datei mit Prompt/Antwort-Struktur."""
    if not os.path.exists(path):
        raise SystemExit(f"❌ Fehler: Datei nicht gefunden: {path}")
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise SystemExit("❌ Fehler: JSON muss eine Liste von Einträgen enthalten.")
    if not data:
        raise SystemExit("❌ Fehler: JSON-Liste ist leer.")
    if "answer" not in data[0]:
        raise SystemExit("❌ Fehler: JSON hat nicht das erwartete Format ('answer' fehlt).")

    return data


def compute_overall_intensity(analysis: Dict[str, Any]) -> float:
    """
    Berechnet einen aggregierten Drift-Intensitäts-Score für einen Lauf.

    Verwendet die in der Dokumentation beschriebenen Gewichte:

        Intensity_i =
            w1 * (1 - Similarity_i)
          + w2 * DriftNorm_i
          + w3 * (Format_i != Format_1)
          + w4 * (Role_i != Role_1)

    und mittelt über alle Prompts.
    """
    w1 = 0.5
    w2 = 0.2
    w3 = 0.2
    w4 = 0.1

    similarities = analysis["similarity"]["similarities"]
    drift_ratios = analysis["word_drift"]["drift_ratio"]
    formats = analysis["structure"]["formats"]
    role_info = analysis["qualitative"]["role"]

    baseline_fmt = formats[0]
    baseline_role = role_info["baseline_role"]
    roles = role_info["roles"]

    n = len(similarities)
    if n == 0:
        return 0.0

    intensities = []
    for i in range(n):
        sim = similarities[i]
        drift_norm = drift_ratios[i] if i < len(drift_ratios) else 0.0

        fmt_diff = 1.0 if formats[i] != baseline_fmt else 0.0

        r = roles[i]
        role_diff = 0.0
        if baseline_role is not None:
            # Vergleich zur Ausgangsrolle
            role_diff = 1.0 if (r is not None and r != baseline_role) else 0.0
        else:
            # keine Ausgangsrolle definiert, aber aktuelle Rolle vorhanden
            role_diff = 1.0 if r is not None else 0.0

        intensity_i = (
            w1 * (1.0 - sim)
            + w2 * drift_norm
            + w3 * fmt_diff
            + w4 * role_diff
        )
        intensities.append(intensity_i)

    return sum(intensities) / len(intensities)


def compare_analyses(base_name: str, base_analysis: Dict[str, Any],
                     other_name: str, other_analysis: Dict[str, Any]) -> Dict[str, Any]:
    """
    Vergleicht zwei Analysen und berechnet Differenzen & Driftreduktion.
    """
    # Convenience-Referenzen
    b_sim = base_analysis["similarity"]
    o_sim = other_analysis["similarity"]

    b_word = base_analysis["word_drift"]
    o_word = other_analysis["word_drift"]

    b_struct = base_analysis["structure"]
    o_struct = other_analysis["structure"]

    b_role = base_analysis["qualitative"]["role"]
    o_role = other_analysis["qualitative"]["role"]

    b_context = base_analysis["qualitative"]["context"]
    o_context = other_analysis["qualitative"]["context"]

    # Intensitäten
    b_intensity = compute_overall_intensity(base_analysis)
    o_intensity = compute_overall_intensity(other_analysis)

    drift_reduction = None
    if b_intensity > 0:
        drift_reduction = 1.0 - (o_intensity / b_intensity)

    # Mittelwerte Wortdrift
    b_avg_word_drift = sum(b_word["drift_ratio"]) / len(b_word["drift_ratio"]) if b_word["drift_ratio"] else 0.0
    o_avg_word_drift = sum(o_word["drift_ratio"]) / len(o_word["drift_ratio"]) if o_word["drift_ratio"] else 0.0

    comparison = {
        "baseline_name": base_name,
        "other_name": other_name,
        "similarity_mean_baseline": b_sim["mean"],
        "similarity_mean_other": o_sim["mean"],
        "similarity_mean_diff": o_sim["mean"] - b_sim["mean"],
        "word_drift_mean_baseline": b_avg_word_drift,
        "word_drift_mean_other": o_avg_word_drift,
        "word_drift_mean_diff": o_avg_word_drift - b_avg_word_drift,
        "structure_changes_baseline": b_struct["structure_changes"],
        "structure_changes_other": o_struct["structure_changes"],
        "structure_changes_diff": o_struct["structure_changes"] - b_struct["structure_changes"],
        "role_changes_baseline": b_role["changes"],
        "role_changes_other": o_role["changes"],
        "role_changes_diff": o_role["changes"] - b_role["changes"],
        "context_changes_baseline": b_context["changes"],
        "context_changes_other": o_context["changes"],
        "context_changes_diff": o_context["changes"] - b_context["changes"],
        "intensity_baseline": b_intensity,
        "intensity_other": o_intensity,
        "drift_reduction": drift_reduction,
    }

    return comparison


def format_percentage(value: float) -> str:
    """Hilfsfunktion: formatiert Prozentwerte schön."""
    return f"{value * 100:.1f}%"


def create_compare_report(base_name: str, base_analysis: Dict[str, Any],
                          other_name: str, other_analysis: Dict[str, Any],
                          comparison: Dict[str, Any]) -> str:
    """
    Erzeugt einen Markdown-Vergleichsreport für zwei Läufe.
    """
    md = []
    md.append("# Driftvergleich – Baseline vs. Alternativlauf\n")

    md.append("## Überblick\n")
    md.append(f"- Baseline: **{base_name}**")
    md.append(f"- Vergleichslauf: **{other_name}**\n")

    # Similarity
    md.append("## Similarity (Durchschnitt)\n")
    md.append("| Lauf | Similarity Ø |")
    md.append("|------|--------------|")
    md.append(f"| {base_name}  | {comparison['similarity_mean_baseline']:.3f} |")
    md.append(f"| {other_name} | {comparison['similarity_mean_other']:.3f} |")
    md.append("")
    md.append(f"- Differenz (Andere - Baseline): **{comparison['similarity_mean_diff']:.3f}**\n")

    # Wortdrift
    md.append("## Wortdrift (Drift Ratio Ø)\n")
    md.append("| Lauf | Drift Ratio Ø |")
    md.append("|------|---------------|")
    md.append(f"| {base_name}  | {comparison['word_drift_mean_baseline']:.3f} |")
    md.append(f"| {other_name} | {comparison['word_drift_mean_other']:.3f} |")
    md.append("")
    md.append(f"- Differenz (Andere - Baseline): **{comparison['word_drift_mean_diff']:.3f}**\n")

    # Strukturdrift
    md.append("## Strukturdrift (Strukturwechsel gesamt)\n")
    md.append("| Lauf | Strukturwechsel |")
    md.append("|------|-----------------|")
    md.append(f"| {base_name}  | {comparison['structure_changes_baseline']} |")
    md.append(f"| {other_name} | {comparison['structure_changes_other']} |")
    md.append("")
    md.append(f"- Differenz (Andere - Baseline): **{comparison['structure_changes_diff']}**\n")

    # Rollen- und Kontextdrift
    md.append("## Rollendrift\n")
    md.append("| Lauf | Rollenwechsel |")
    md.append("|------|---------------|")
    md.append(f"| {base_name}  | {comparison['role_changes_baseline']} |")
    md.append(f"| {other_name} | {comparison['role_changes_other']} |")
    md.append("")
    md.append(f"- Differenz (Andere - Baseline): **{comparison['role_changes_diff']}**\n")

    md.append("## Kontext-/Domänendrift\n")
    md.append("| Lauf | Domänenwechsel |")
    md.append("|------|----------------|")
    md.append(f"| {base_name}  | {comparison['context_changes_baseline']} |")
    md.append(f"| {other_name} | {comparison['context_changes_other']} |")
    md.append("")
    md.append(f"- Differenz (Andere - Baseline): **{comparison['context_changes_diff']}**\n")

    # Intensität & Driftreduktion
    md.append("## Aggregierte Driftintensität\n")
    md.append("| Lauf | Drift-Intensität |")
    md.append("|------|------------------|")
    md.append(f"| {base_name}  | {comparison['intensity_baseline']:.3f} |")
    md.append(f"| {other_name} | {comparison['intensity_other']:.3f} |")
    md.append("")

    if comparison["drift_reduction"] is not None:
        md.append(
            f"- Driftreduktion (1 - Intensität_Andere / Intensität_Baseline): "
            f"**{format_percentage(comparison['drift_reduction'])}**"
        )
    else:
        md.append("- Driftreduktion konnte nicht berechnet werden (Baseline-Intensität = 0).")

    md.append("\n---\n")
    md.append("## Interpretation (Hinweise)\n")

    # einfache Heuristik für Textinterpretation
    interp_lines = []

    # Similarity
    if comparison["similarity_mean_diff"] > 0.05:
        interp_lines.append(
            f"- Der Vergleichslauf (**{other_name}**) hat deutlich höhere semantische Stabilität als die Baseline."
        )
    elif comparison["similarity_mean_diff"] < -0.05:
        interp_lines.append(
            f"- Die Baseline (**{base_name}**) ist semantisch stabiler als der Vergleichslauf."
        )
    else:
        interp_lines.append(
            "- In Bezug auf semantische Ähnlichkeit sind beide Läufe relativ ähnlich."
        )

    # Wortdrift
    if comparison["word_drift_mean_diff"] < -0.05:
        interp_lines.append(
            f"- Der Vergleichslauf (**{other_name}**) reduziert Wortdrift gegenüber der Baseline spürbar."
        )
    elif comparison["word_drift_mean_diff"] > 0.05:
        interp_lines.append(
            f"- Die Wortdrift ist im Vergleichslauf (**{other_name}**) höher als in der Baseline."
        )

    # Strukturdrift
    if comparison["structure_changes_diff"] < 0:
        interp_lines.append(
            f"- {other_name} zeigt stabilere Antwortstrukturen als {base_name}."
        )
    elif comparison["structure_changes_diff"] > 0:
        interp_lines.append(
            f"- Die Struktur der Antworten ist in {other_name} volatiler als in {base_name}."
        )

    # Rollen-/Kontextdrift
    if comparison["role_changes_diff"] < 0:
        interp_lines.append(
            f"- Der Vergleichslauf reduziert Rollendrift gegenüber der Baseline."
        )
    if comparison["context_changes_diff"] < 0:
        interp_lines.append(
            f"- Der Vergleichslauf reduziert Kontext-/Domänendrift gegenüber der Baseline."
        )

    if comparison["drift_reduction"] is not None:
        if comparison["drift_reduction"] > 0.2:
            interp_lines.append(
                f"- Insgesamt reduziert {other_name} die Drift deutlich gegenüber {base_name}."
            )
        elif comparison["drift_reduction"] > 0.05:
            interp_lines.append(
                f"- Insgesamt reduziert {other_name} die Drift leicht gegenüber {base_name}."
            )
        elif comparison["drift_reduction"] < -0.05:
            interp_lines.append(
                f"- Insgesamt erhöht {other_name} die Drift im Vergleich zur Baseline."
            )

    if not interp_lines:
        interp_lines.append("- Die Unterschiede zwischen den Läufen sind insgesamt gering.")

    md.extend(interp_lines)

    return "\n".join(md)


# ---------------------------------------------------------
# CLI
# ---------------------------------------------------------

def main():
    if len(sys.argv) < 3:
        print("Verwendung:")
        print("  python drift_analysis_compare.py BASELINE.json OTHER.json [--out-md] [--out-json]")
        sys.exit(1)

    baseline_path = sys.argv[1]
    other_path = sys.argv[2]

    out_md = "--out-md" in sys.argv
    out_json = "--out-json" in sys.argv

    print(f"📄 Lade Baseline-Datei: {baseline_path}")
    baseline_results = load_results(baseline_path)

    print(f"📄 Lade Vergleichs-Datei: {other_path}")
    other_results = load_results(other_path)

    print("\n🔍 Führe Analyse für Baseline aus…")
    baseline_analysis = analyze(baseline_results)

    print("🔍 Führe Analyse für Vergleichslauf aus…")
    other_analysis = analyze(other_results)

    # Namen aus Dateinamen ableiten
    base_name = os.path.splitext(os.path.basename(baseline_path))[0]
    other_name = os.path.splitext(os.path.basename(other_path))[0]

    print("\n⚖️ Vergleiche Analysen…")
    comparison = compare_analyses(base_name, baseline_analysis, other_name, other_analysis)

    print("\n=== Vergleichsmatrix ===")
    print(json.dumps(comparison, indent=2, ensure_ascii=False))

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    if out_json:
        out_json_path = f"results/compare_{base_name}_vs_{other_name}_{timestamp}.json"
        os.makedirs(os.path.dirname(out_json_path), exist_ok=True)
        with open(out_json_path, "w", encoding="utf-8") as f:
            json.dump(
                {
                    "baseline": baseline_analysis,
                    "other": other_analysis,
                    "comparison": comparison,
                },
                f,
                indent=2,
                ensure_ascii=False,
            )
        print(f"\n💾 Vergleichs-JSON gespeichert unter:\n{out_json_path}")

    if out_md:
        out_md_path = f"results/compare_{base_name}_vs_{other_name}_{timestamp}.md"
        os.makedirs(os.path.dirname(out_md_path), exist_ok=True)
        report = create_compare_report(base_name, baseline_analysis, other_name, other_analysis, comparison)
        with open(out_md_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"\n📝 Vergleichs-Report gespeichert unter:\n{out_md_path}")

    print("\n✅ Vergleich abgeschlossen.\n")


if __name__ == "__main__":
    main()
