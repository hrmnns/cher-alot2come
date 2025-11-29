# --------------------------------------------------------
# Doku: docs/dev/drift-tests.md
# --------------------------------------------------------

import google.generativeai as genai
import json
import sys
import os
import time
from datetime import datetime

# --------------------------------------------------------
# 1. API Key laden
# --------------------------------------------------------
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY:
    raise SystemExit("❌ Fehler: GEMINI_API_KEY ist nicht gesetzt.")

genai.configure(api_key=API_KEY)


# --------------------------------------------------------
# 2. JSON-Promptdatei laden
# --------------------------------------------------------
def load_prompts_file():
    """Lädt die Prompts-Datei aus den CLI-Argumenten oder sucht prompts.json."""
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        if not os.path.exists(file_path):
            raise SystemExit(f"❌ Fehler: Die Datei '{file_path}' existiert nicht.")
        return file_path

    default_file = "prompts.json"
    if os.path.exists(default_file):
        return default_file

    raise SystemExit("❌ Keine JSON-Datei angegeben und 'prompts.json' wurde nicht gefunden.")


prompts_file = load_prompts_file()

# JSON öffnen
with open(prompts_file, "r", encoding="utf-8") as f:
    config = json.load(f)

prompts = config.get("prompts")
if not prompts or not isinstance(prompts, list):
    raise SystemExit("❌ Fehler: Die JSON-Datei enthält keine gültige 'prompts'-Liste.")


# --------------------------------------------------------
# 3. Modell initialisieren
# --------------------------------------------------------
model_name = "gemini-1.5-pro"
model = genai.GenerativeModel(model_name)


# --------------------------------------------------------
# 4. Drift-Experiment ausführen
# --------------------------------------------------------
print(f"\n🧪 Starte Drift-Experiment mit Gemini ({model_name}) …\n")
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

    time.sleep(0.5)  # minimiert Rate-Limit-Risiko


# --------------------------------------------------------
# 5. Ergebnisse speichern
# --------------------------------------------------------
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
output_file = f"gemini_drift_experiment_{timestamp}.json"

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)

print(f"🏁 Experiment abgeschlossen. Ergebnisse gespeichert in:\n{output_file}\n")
