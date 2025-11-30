"""
drift_experiment_gemini.py
--------------------------

Automatisierter Drift-Test-Runner für Gemini.
Unterstützt CLI-Parameter für Prompts, Modell und automatische Analyse.

Beispiele:
    python drift_experiment_gemini.py --prompts prompts/modul.json
    python drift_experiment_gemini.py --analyze
    python drift_experiment_gemini.py --model gemini-1.5-flash --analyze
"""

import google.generativeai as genai
import json
import sys
import os
import time
from datetime import datetime

# --------------------------------------------------------
# Hilfsfunktion: CLI-Argumente parsen
# --------------------------------------------------------
def get_arg(flag: str, default=None):
    """Liest einen Wert nach einem Flag, z. B. --prompts datei.json."""
    if flag in sys.argv:
        idx = sys.argv.index(flag)
        if idx + 1 < len(sys.argv):
            return sys.argv[idx + 1]
    return default


def has_flag(flag: str) -> bool:
    """Prüft, ob ein Flag vorhanden ist."""
    return flag in sys.argv


# --------------------------------------------------------
# 1. API-Key prüfen
# --------------------------------------------------------
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise SystemExit("❌ Fehler: GEMINI_API_KEY ist nicht gesetzt.")

genai.configure(api_key=API_KEY)

# --------------------------------------------------------
# 2. Ordner: results/ sicherstellen
# --------------------------------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTS_DIR = os.path.join(BASE_DIR, "results")
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")

os.makedirs(RESULTS_DIR, exist_ok=True)


# --------------------------------------------------------
# 3. Promptdatei bestimmen
# --------------------------------------------------------
prompts_path = get_arg("--prompts")

if prompts_path is None:
    # Standardpfad: prompts/prompts.json
    prompts_path = os.path.join(PROMPTS_DIR, "prompts.json")

# Absolutpfad erzeugen
prompts_path = os.path.abspath(prompts_path)

if not os.path.exists(prompts_path):
    raise SystemExit(f"❌ Promptdatei nicht gefunden: {prompts_path}")

print(f"📄 Verwende Promptdatei: {prompts_path}")


# --------------------------------------------------------
# 4. Modell bestimmen
# --------------------------------------------------------
model_name = get_arg("--model", "models/gemini-2.5-flash")
print(f"🧠 Verwende Modell: {model_name}")

model = genai.GenerativeModel(model_name)


# --------------------------------------------------------
# 5. Prompts laden
# --------------------------------------------------------
with open(prompts_path, "r", encoding="utf-8") as f:
    config = json.load(f)

prompts = config.get("prompts")
if not isinstance(prompts, list) or len(prompts) == 0:
    raise SystemExit("❌ Fehler: JSON enthält keine gültigen Prompts.")

print(f"📝 Anzahl Prompts: {len(prompts)}")


# --------------------------------------------------------
# 6. Experiment durchführen
# --------------------------------------------------------
print("\n🧪 Starte Drift-Experiment...\n")
results = []

for i, prompt in enumerate(prompts, start=1):
    print(f"\n=== Prompt {i} ===")
    print(prompt)

    try:
        response = model.generate_content(prompt)
        answer = response.text
    except Exception as e:
        answer = f"❌ Fehler: {e}"

    print(f"\nAntwort {i}:\n{answer}\n")

    results.append({
        "prompt_number": i,
        "prompt": prompt,
        "answer": answer
    })

    time.sleep(0.5)


# --------------------------------------------------------
# 7. Ergebnisse speichern
# --------------------------------------------------------
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
outfile_json = os.path.join(RESULTS_DIR, f"gemini_drift_experiment_{timestamp}.json")

with open(outfile_json, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\n💾 Ergebnisse gespeichert in:\n{outfile_json}")


# --------------------------------------------------------
# 8. Optional: Analyse durchführen
# --------------------------------------------------------
if has_flag("--analyze"):
    try:
        from drift_analysis_core import create_report
    except Exception as e:
        raise SystemExit(f"❌ Fehler beim Laden von drift_analysis_core: {e}")

    report = create_report(results)
    outfile_md = os.path.join(RESULTS_DIR, f"drift_report_{timestamp}.md")

    with open(outfile_md, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"📊 Analyse abgeschlossen: {outfile_md}")

print("\n🏁 Fertig.")
