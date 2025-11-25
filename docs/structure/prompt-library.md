# Prompt Library  
Version: v0.1  
Zweck: Stabiler, getesteter Prompt-Baukasten für alle Phasen des Makro- und Mikroprozesses.
*ENTWURF*

# 1. Start-Prompts (Chat-Start / Mikroprozess Phase A)

## 1.1 Standard-Start-Prompt
„Bitte agiere als LLM-Methodiker.  
Wir starten eine neue Arbeitseinheit.  
Hier ist der Kontext: <Kurzkontext>.  
Ziel dieses Chats: <konkretes Ziel>.  
Arbeitsmodus: <Modus>.  
Relevante Artefakte: <Dateien, Issues>.  
Bitte bestätige den Start-Prompt.“

## 1.2 Start-Prompt für Issue-Bearbeitung
„Neuer Chat zur Bearbeitung von Issue <Nummer>.  
Bitte als Methodiker arbeiten.  
Kontext aus dem Issue: <Kurzfassung>.  
Ziel: <Ziel des Issues>.  
Bitte bestätige Rollen, Ziel und Vorgehen.“

## 1.3 Start-Prompt für Dokumentüberarbeitung
„Bitte agiere als Strukturgeber.  
Wir überarbeiten Abschnitt <Name> aus <Dokument>.  
Ziel: Struktur verbessern, ohne Inhalte zu verändern.  
Rollen: Strukturgeber.  
Arbeitsmodus: Strukturierung.“

# 2. Drift-Korrektur-Prompts  
(basierend auf Drift-Management: :contentReference[oaicite:3]{index=3})

## 2.1 Sofortkorrekturen
- „Wir haben eine Begriffsdrift: Der definierte Begriff ist ›<Begriff>‹. Bitte korrigiere alle driften Stellen.“
- „Bitte stelle die Struktur gemäß Repository-Version wieder her (Datei: <Pfad>).“

## 2.2 Kontextrekalibrierung
- „Bitte lade die Projektanweisung neu und bestätige die gültigen Begriffe aus dem Glossar.“
- „Wir haben eine leichte Strukturdrift. Bitte stelle die Phasennummerierung gemäß Makroprozess wieder her.“

## 2.3 Vergleich mit Repository
- „Vergleiche deine letzte Antwort mit der Version aus <Dokument>. Liste alle Abweichungen.“
- „Bitte formuliere den Abschnitt neu, strikt entlang der persistierten Struktur aus <Dokument>.“

## 2.4 Reparatur-Workflow
- „Bitte markiere alle Passagen, die von der persistierten Version abweichen.“
- „Aktiviere Reviewer. Prüfe die Überarbeitung auf Konsistenz und Driftfreiheit.“

# 3. Persistenz-Prompts  
(basierend auf Persistenzmechanismen: :contentReference[oaicite:4]{index=4})

## 3.1 Repository-Übergabe vorbereiten
„Bitte liefere den Ergebnisblock als sauberen, getrennten Block.  
Ohne Meta-Text.  
Status: ›final für Repository‹.“

## 3.2 Persistenz-Check
„Bitte prüfe dieses Ergebnis gegen bestehende Dokumente auf:  
– Begriffe  
– Struktur  
– Konsistenz  
– Versionen.“

## 3.3 Auswahl der Zielorte
„Welcher Abschnitt und welche Datei sind gemäß Informationsarchitektur korrekt für dieses Ergebnis?“

## 3.4 Übergabeformat
„Bitte gib mir eine Repository-fertige Fassung des Ergebnisblocks gemäß Formatregeln (Markdown, klare Struktur, keine Meta-Erläuterungen).“

# 4. Rollenaktivierungs-Prompts  
(basiert auf Rollenmodell: :contentReference[oaicite:5]{index=5})

## 4.1 LLM-Methodiker
„Bitte agiere als LLM-Methodiker.  
Prüfe Struktur, Vorgehen, Konsistenz und Zielklarheit dieses Abschnitts.“

## 4.2 Strukturgeber
„Bitte agiere als Strukturgeber.  
Erstelle eine präzise Gliederung für <Thema>. Kein Fließtext.“

## 4.3 Reviewer
„Bitte agiere als Reviewer.  
Prüfe diesen Text ausschließlich auf:  
– Logik  
– Konsistenz  
– Terminologie  
– Struktur (ohne neue Inhalte).“

## 4.4 Prompt-Engineer
„Bitte agiere als Prompt-Engineer.  
Optimiere diesen Prompt für Ambiguitätsresistenz und Rollenstabilität.“

## 4.5 Domänenexperte
„Bitte agiere als Domänenexperte für <Domäne>.  
Erkläre <Begriff> und gib ein kurzes Beispiel.“

# 5. Handover-Prompts  
(kompatibel mit `handover-and-closure.md` :contentReference[oaicite:6]{index=6})

## 5.1 Übergabe an neuen Chat
„Bitte erstelle einen Handover-Block mit:  
– Kontext  
– bisherigen Ergebnissen  
– offenen Punkten  
– nächstem Schritt.“

## 5.2 Übergabe an Issue
„Bitte erstelle einen Handover-Block zur Erstellung eines Issues für folgende Aufgabe: <Beschreibung>.  
Mit: Thema, Stand, Offenes, Benötigte Rolle, Betroffene Dateien.“

## 5.3 Übergabe zur Persistenz
„Bitte erstelle den Handover-Block zur Persistenz mit:  
– Inhalte zur Übertragung  
– Quelle  
– Zielort  
– Hinweise/Versionierung.“

## 5.4 Abschluss eines Chats
„Bitte stelle einen Abschlussblock bereit mit:  
– Zusammenfassung  
– Offene Punkte  
– Repository-Übergaben  
– Nächste Schritte.“

# 6. Mini-Checks (kompatibel mit Mikroprozess & Drift-Management)

## 6.1 Drift-Check
„Bitte bestätige Terminologie, Struktur und Zielrahmen dieser Arbeitseinheit.“

## 6.2 Rollen-Check
„In welcher Rolle arbeitest du gerade?“

## 6.3 Struktur-Check
„Bitte gib die gültige Prozess- oder Dokumentstruktur aus <Dokument> wieder.“

# 7. Quick-Prompts (häufig genutzte Shortcuts)

- „Bitte zurück zum Fokus.“  
- „Bitte bestätige den aktuellen Zielrahmen.“  
- „Bitte gib drei Strukturvarianten.“  
- „Bitte gib eine stabile Version als Ergebnisblock.“  
- „Bitte Liste aller offenen Punkte aus diesem Chat.“

# 8. Weiterführende Dokumente (Backlinks)
- Drift-Management (docs/quality/drift-management.md)  
- Persistenzmechanismen (docs/quality/persistence-mechanisms.md)  
- Mikroprozess (docs/processes/process-micro-chat.md)  
- Rollenmodell (docs/structure/roles-llm.md)
