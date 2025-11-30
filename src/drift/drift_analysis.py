"""
drift_analysis.py
------------------

CLI-Werkzeug zur nachträglichen Analyse einer Ergebnis-JSON-Datei
aus einem Drift-Experiment. Dieses Skript arbeitet vollständig offline
und nutzt das Analysemodul `drift_analysis_core.py`.

Aufruf:
    python drift_analysis.py <pfad_zur_json_datei>

Beispiel:
    python drift_analysis.py results/gemini_drift_experiment_2025-02-03_19-33-22.json
"""

import os
import sys
import json
from datetime import datetime

# --------------------------------------------------------
# 1. Analyse-Core importieren
# --------------------------------------------------------
try:
    from drift_analysis_core import create_report
except Exception as e:
    raise SystemExit(f"❌ Fehler: Analysemodul konnte nicht geladen werden: {e}")


# --------------------------------------------------------
# 2. CLI-Argument prüfen
# --------------------------------------------------------
if len(sys.argv) < 2:
    raise SystemExit(
        "❌ Fehler: Keine Eingabedatei angegeben.\n\n"
        "Aufruf:\n"
        "    python drift_analysis.py <pfad_zur_json_datei>\n"
    )

input_file = sys.argv[1]

if not os.path.exists(input_file):
    raise SystemExit(f"❌ Fehler: Datei existiert nicht:\n{input_file}")


# --------------------------------------------------------
# 3. Ergebnisse laden
# --------------------------------------------------------
try:
    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)
except Exception as e:
    raise SystemExit(f"❌ Fehler beim Lesen der JSON-Datei: {e}")


if not isinstance(data, list) or len(data) == 0:
    raise SystemExit("❌ Fehler: JSON-Datei enthält kein gültiges Ergebnisformat.")


# --------------------------------------------------------
# 4. Ergebnisse analysieren
# --------------------------------------------------------
try:
    report_md = create_report(data)
except Exception as e:
    raise SystemExit(f"❌ Fehler bei der Analyse: {e}")


# --------------------------------------------------------
# 5. Report speichern
# --------------------------------------------------------
base_dir = os.path.dirname(os.path.abspath(__file__))
results_dir = os.path.join(base_dir, "results")
os.makedirs(results_dir, exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_path = os.path.join(results_dir, f"drift_report_{timestamp}.md")

try:
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(report_md)
except Exception as e:
    raise SystemExit(f"❌ Fehler beim Schreiben der Reportdatei: {e}")

print(f"📊 Analyse abgeschlossen.")
print(f"💾 Report gespeichert unter:\n{output_path}")
