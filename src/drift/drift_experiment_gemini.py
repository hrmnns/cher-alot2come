"""
drift_experiment_gemini.py
--------------------------

Erweitertes Drift-Experiment-Skript mit optionalen Persistenzmechanismen.
Unterstützt Quality-Modes, die aus einer JSON-Datei geladen werden.

Features:
- lädt Promptsets (JSON)
- optional Qualitätsmodus (--quality)
- Persistenzblöcke aus persistence_modes.json
- Analyse optional (--analyze)
- speichert Ergebnisse + Reports
"""

import google.generativeai as genai
import json
import sys
import os
import time
from datetime import datetime

# ------------------------------
# CLI-Argument Hilfsmethoden
# ------------------------------
def get_arg(flag: str, default=None):
    if flag in sys.argv:
        idx = sys.argv.index(flag)
        if idx + 1 < len(sys.argv):
            return sys.argv[idx + 1]
    return default

def has_flag(flag: str) -> bool:
    return flag in sys.argv


# ------------------------------
# API-Key sicherstellen
# ------------------------------
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise SystemExit("❌ Fehler: GEMINI_API_KEY ist nicht gesetzt.")

genai.configure(api_key=API_KEY)


# ------------------------------
# Verzeichnisse
# ------------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROMPTS_DIR = os.path.join(BASE_DIR, "prompts")
RESULTS_DIR = os.path.join(BASE_DIR, "results")
os.makedirs(RESULTS_DIR, exist_ok=True)


# ------------------------------
# Promptdatei laden
# ------------------------------
prompts_path = get_arg("--prompts")

if prompts_path is None:
    prompts_path = os.path.join(PROMPTS_DIR, "prompts.json")

prompts_path = os.path.abspath(prompts_path)

if not os.path.exists(prompts_path):
    raise SystemExit(f"❌ Promptdatei nicht gefunden: {prompts_path}")

with open(prompts_path, "r", encoding="utf-8") as f:
    config = json.load(f)

prompts = config.get("prompts")
if not isinstance(prompts, list) or len(prompts) == 0:
    raise SystemExit("❌ Fehler: JSON enthält keine gültige 'prompts'-Liste.")

print(f"📄 Verwende Promptdatei: {prompts_path}")
print(f"📝 Anzahl Prompts: {len(prompts)}")


# ------------------------------
# Quality Mode laden
# ------------------------------
quality_mode = get_arg("--quality", "baseline")

persistence_prepend = ""
persistence_append = ""

if quality_mode != "baseline":
    modes_file = os.path.join(PROMPTS_DIR, "persistence_modes.json")

    if not os.path.exists(modes_file):
        raise SystemExit(f"❌ Quality-Mode verlangt Persistenzdatei, aber nicht gefunden:\n{modes_file}")

    with open(modes_file, "r", encoding="utf-8") as f:
        modes = json.load(f)

    if quality_mode not in modes:
        raise SystemExit(f"❌ Unbekannter Quality-Mode: {quality_mode}")

    persistence_prepend = modes[quality_mode].get("prepend", "")
    persistence_append = modes[quality_mode].get("append", "")

print(f"🎛 Qualitätsmodus: {quality_mode}")


# ------------------------------
# Modell laden
# ------------------------------
model_name = get_arg("--model", "models/gemini-2.5-flash")
print(f"🤖 Modell: {model_name}")

model = genai.GenerativeModel(model_name)


# ------------------------------
# Experiment durchführen
# ------------------------------
print("\n🧪 Starte Experiment...\n")
results = []

for i, prompt in enumerate(prompts, start=1):
    print(f"\n=== Prompt {i} ===")
    print(prompt)

    # Persistenzblöcke injizieren
    full_prompt = ""

    if persistence_prepend:
        full_prompt += persistence_prepend + "\n\n"

    full_prompt += prompt

    if persistence_append:
        full_prompt += "\n\n" + persistence_append

    try:
        response = model.generate_content(full_prompt)
        answer = response.text
    except Exception as e:
        answer = f"❌ Fehler: {e}"

    print(f"\nAntwort {i}:\n{answer}\n")

    results.append({
        "prompt_number": i,
        "prompt": full_prompt,
        "answer": answer
    })

    time.sleep(0.5)


# ------------------------------
# Ergebnisse speichern
# ------------------------------
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
outfile_json = os.path.join(RESULTS_DIR, f"gemini_{quality_mode}_experiment_{timestamp}.json")

with open(outfile_json, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"\n💾 Ergebnisse gespeichert in:\n{outfile_json}")


# ------------------------------
# Optional Analyse ausführen
# ------------------------------
if has_flag("--analyze"):
    try:
        from drift_analysis_core import create_report
    except Exception as e:
        raise SystemExit(f"❌ Fehler beim Laden des Analysemoduls: {e}")

    report = create_report(results)
    outfile_md = os.path.join(RESULTS_DIR, f"drift_report_{quality_mode}_{timestamp}.md")

    with open(outfile_md, "w", encoding="utf-8") as f:
        f.write(report)

    print(f"📊 Analyse abgeschlossen:\n{outfile_md}")

print("\n🏁 Fertig.")
