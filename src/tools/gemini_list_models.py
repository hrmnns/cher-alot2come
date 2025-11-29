"""
gemini_list_models.py
---------------------

Dieses Skript listet alle verfügbaren Gemini-Modelle über die 
Google-GenerativeAI-API auf. Es dient als kleines Hilfswerkzeug, um 
verfügbare Modellnamen, Versionen und Modelltypen zu identifizieren.

Zweck:
- Übersicht über alle nutzbaren Gemini-Modelle erhalten
- Auswahl eines Modells für Experimente oder Drift-Tests erleichtern
- Prüfung, ob bestimmte Modelle im Free Tier verfügbar sind
- Unterstützung bei der Konfiguration von Experimentskripten

Voraussetzungen:
- Umgebungsvariable GEMINI_API_KEY muss gesetzt sein
- Modul `google-generativeai` muss installiert sein

Nutzung:
    python gemini_list_models.py

Ausgabe:
    Eine formatierte Liste aller Modelle mit Basisinformationen.
"""

import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

models = genai.list_models()

for m in models:
    print(m.name)
