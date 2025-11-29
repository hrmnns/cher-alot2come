"""
drift_analysis_core_test.py
---------------------------

Dieses Skript testet die Funktionalität des Moduls drift_analysis_core.py
und verifiziert:

- Importfunktionalität (auch bei komplexen Pfaden)
- Erstellung eines Markdown-Reports aus einer Ergebnis-JSON-Datei
- Robustheit gegenüber relativen Pfaden

Es kann aus jedem Verzeichnis gestartet werden.
"""

import os
import sys
import json

# --------------------------------------------------------
# 1. Sicherstellen, dass das Drift-Verzeichnis im Modulpfad ist
# --------------------------------------------------------

# Absoluter Pfad dieses Testskripts
TEST_FILE_DIR = os.path.dirname(os.path.abspath(__file__))

# Drift-Verzeichnis (wo drift_analysis_core.py liegt)
DRIFT_DIR = TEST_FILE_DIR  # liegt im selben Ordner

# Modulpfad an erste Stelle setzen
sys.path.insert(0, DRIFT_DIR)

# --------------------------------------------------------
# 2. Test: Modul importieren
# --------------------------------------------------------
try:
    from drift_analysis_core import create_report
    print("✔ Modul importiert: drift_analysis_core")
except Exception as e:
    print("❌ Fehler beim Import von drift_analysis_core:", e)
    sys.exit(1)

# --------------------------------------------------------
# 3. Test: JSON-Datei finden
# --------------------------------------------------------

RESULTS_DIR = os.path.join(TEST_FILE_DIR, "results")
TEST_JSON = os.path.join(RESULTS_DIR, "test_results.json")

if not os.path.exists(TEST_JSON):
    print(f"❌ Testdatei nicht gefunden: {TEST_JSON}")
    print("Bitte lege eine Datei 'test_results.json' im results/ Ordner an.")
    sys.exit(1)

print(f"✔ Testdatei gefunden: {TEST_JSON}")

# --------------------------------------------------------
# 4. JSON einlesen
# --------------------------------------------------------
try:
    with open(TEST_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    print("✔ Testdaten erfolgreich geladen.")
except Exception as e:
    print("❌ Fehler beim Lesen der JSON-Datei:", e)
    sys.exit(1)


# --------------------------------------------------------
# 5. Report erzeugen
# --------------------------------------------------------
try:
    report = create_report(data)
    print("✔ Drift-Report erfolgreich erzeugt.\n")
except Exception as e:
    print("❌ Fehler beim Erzeugen des Reports:", e)
    sys.exit(1)


# --------------------------------------------------------
# 6. Report anzeigen (Terminal-Ausgabe)
# --------------------------------------------------------
print("===== DRIFT REPORT (Ausschnitt) =====")
print(report[:1000])  # nur einen Teil ausgeben, falls sehr lang
print("===== ENDE =====")

print("\n✔ Test erfolgreich abgeschlossen!")
