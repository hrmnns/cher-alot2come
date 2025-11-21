# Drift Management (Überarbeitete und erweiterte Fassung)

## 1. Zweck und Einordnung

Dieses Dokument beschreibt ein praktisches, alltagstaugliches Drift-Management für LLM-gestützte Projekte. „Drift“ bezeichnet jede ungewollte Veränderung von Begriffen, Strukturen, Rollen oder Kontexten, die dazu führt, dass das LLM schrittweise von der ursprünglichen Problemdefinition abweicht. Je länger ein Projekt läuft und je mehr Chats stattfinden, desto größer ist das Risiko, dass Inhalte verwässern oder sich in feinen, aber entscheidenden Details verändern.

Drift-Management verfolgt daher drei Kernziele:

1. **Früh erkennen**, wenn sich Abweichungen anbahnen.  
2. **Aktiv verhindern**, dass Abweichungen unkontrolliert wachsen.  
3. **Gezielt korrigieren**, um den Projektzustand stabil zu halten.

Es ergänzt die Persistenzmechanismen, sorgt für methodische Stabilität und ist integraler Bestandteil des Makroprozesses.

## 2. Arten von Drift

### 2.1 Begriffsdrift
Begriffe verlieren ihre definierte Bedeutung oder werden plötzlich in anderer Bedeutung verwendet.

**Beispiel:**  
„Methodologie-Baustein“ wird im Verlauf zu „Modul“, „Element“ oder „Arbeitskomponente“, obwohl im Glossar klar definiert ist, was ein Baustein ist und wie er sich abgrenzt.

### 2.2 Strukturdrift
Die Gliederung eines Dokuments oder eines Prozesses verändert sich unmerklich über Zeit.

**Beispiel:**  
Der Makroprozess umfasst sechs Kernphasen. Im Verlauf beginnt das LLM, Phase 3 in zwei Teilphasen zu zerlegen – ohne Beschluss.

### 2.3 Rollendrift
Rollen verlieren eindeutige Verantwortlichkeiten. Das LLM übernimmt Aufgaben anderer Rollen oder wechselt „inoffiziell“.

**Beispiel:**  
Der „Reviewer“ beginnt plötzlich, operative Inhalte zu erzeugen, obwohl seine Rolle auf die Qualitätsprüfung beschränkt ist.

### 2.4 Kontextdrift
Der thematische Rahmen verschiebt sich – oft unbewusst.

**Beispiel:**  
Das Projekt behandelt die Entwicklung einer LLM-Methodologie. Nach mehreren Chats antwortet das LLM plötzlich aus einer allgemeinen KI-Perspektive und vergisst, dass es sich um eine projektspezifische Methodik handelt.

### 2.5 Ergänzende Formen
- **Intent-Drift:** Die Zielsetzung verändert sich („Wir wollten eigentlich X, aber jetzt reden wir über Y“).
- **Wissensdrift:** Repository-Informationen werden zunehmend unpräzise wiedergegeben.
- **Dokumenten-Drift:** Inhalte verschiedener Dokumente werden vermischt oder überlagert.

## 3. Ursachen von Drift

### 3.1 Modellinterne Ursachen
LLMs erzeugen Antworten probabilistisch. Dadurch entstehen leichte Variationen, die sich kumulieren können. Dies tritt besonders häufig auf, wenn:

- der Chat lang ist,
- verschiedene Aufgaben vermischt werden,
- oder das Modell Rückschlüsse aus früheren Teilen des Gesprächs falsch gewichtet.

### 3.2 Prozessbezogene Ursachen
Drift entsteht besonders dann, wenn:

- keine regelmäßigen Konsistenzprüfungen stattfinden,
- lange ohne Bezug zum Repository gearbeitet wird,
- Kontext nicht explizit erneuert wird.

### 3.3 Interaktionsbedingte Ursachen
Drift wird häufig durch den Nutzer ausgelöst, etwa durch:

- implizite Themenwechsel,
- vage Promptformulierung,
- Nutzung von Synonymen für zentrale Begriffe.

### 3.4 Dokumentationslücken
Wenn nicht sauber persistiert wird, divergieren Chat-Inhalte und Repository-Versionen. Diese Lücke ist ein häufiger Auslöser für Drift im weiteren Verlauf.

## 4. Maßnahmenkatalog zur Drifterkennung

### 4.1 Frühindikatoren
Typische Frühzeichen, die ernst genommen werden sollten:

- Das LLM schlägt andere Begriffe vor, obwohl bereits definierte existieren.
- Rollen werden ohne Aktivierung gewechselt.
- Die Struktur weicht leicht ab (z. B. andere Überschriften).
- Antworten wirken weniger präzise oder stärker verallgemeinert.

### 4.2 Diagnosetechniken

**Glossar-Check:**  
Kurz prüfen, ob zentrale Begriffe noch exakt so verwendet werden wie definiert.

**Strukturabgleich:**  
Die aktuelle Antwort wird mit den korrespondierenden Repository-Dokumenten verglichen.

**Mini-Regressionstest:**  
Das LLM wird gebeten, die wichtigsten Regeln oder Begriffe kurz wiederzugeben.

### 4.3 Checkliste zur Drifterkennung
1. Stimmen die Begriffe mit dem Glossar überein?  
2. Entspricht die Struktur dem Makroprozess?  
3. Werden Rollen korrekt aktiviert und angewendet?  
4. Weicht die Antwort stilistisch oder inhaltlich von früheren Mustern ab?

### 4.4 Automatisierbare Methoden
- Kurzabfrage: „Welche zentralen Begriffe gelten hier?“  
- Kontextrekonstruktion: „Was ist der Zustand der Arbeitseinheit?“  
- Strukturvalidierung: „Bitte fasse die definierte Phasenstruktur zusammen.“

## 5. Regeln zur Driftvermeidung

### 5.1 Strukturregeln
- Prozessstrukturen dürfen nur nach expliziter Freigabe geändert werden.
- Dokumente müssen mit identischen Abschnittslogiken geführt werden.

### 5.2 Terminologieregeln
- Keine Synonyme für zentrale Begriffe.  
- Neue Begriffe nur nach expliziter Definition.

### 5.3 Prompting-Regeln
- Jede Arbeitseinheit beginnt mit einem eindeutigen Kontextabriss.  
- Rollen müssen explizit aktiviert werden.  
- Themenwechsel müssen angekündigt werden.

### 5.4 Dokumentationsregeln
- Ergebnisse zeitnah persistieren.  
- Änderungen müssen nachvollziehbar formuliert werden.  
- Redundante Inhalte vermeiden oder zentralisieren.

## 6. Routinen zur Konsistenzprüfung

### 6.1 Drift-Check beim Chat-Start

Ein effektiver Start-Check umfasst:

1. Ziel der Arbeitseinheit wiederholen  
2. Relevante Dokumente referenzieren  
3. Begriffe bestätigen  
4. Rollen aktivieren  
5. Offene Punkte prüfen  

**Beispiel:**  
„Wir starten mit der nächsten Iteration. Bitte bestätige die gültigen Begriffe für Drift und erläutere kurz den aktuellen Stand.“

### 6.2 Drift-Check während der Arbeit

Nach etwa 5–8 Nachrichten:

- Sind die Rollen noch korrekt?  
- Wurde der Zielrahmen eingehalten?  
- Stimmt die Struktur der Antwort?  

**Beispiel:**  
„Bitte bestätige, ob wir weiterhin entlang der definierten Drift-Arten arbeiten.“

### 6.3 Drift-Check vor Persistenz

Ein verpflichtender Schritt vor jeder Ablage:

- Terminologie gegen Glossar abgleichen  
- Struktur gegen Makroprozess prüfen  
- Offene Fragen markieren  

### 6.4 Integration in den Mikroprozess

Der Mikroprozess enthält zwei feste Driftpunkte:

- **Drift-Check vor der Iteration** – Stabilisierung vor dem Arbeiten  
- **Drift-Check nach dem Entwurf** – Prüfung vor Persistenz

## 7. Korrekturmechanismen bei Drift

### 7.1 Sofortmaßnahmen

- Drift explizit benennen  
- Klarstellung der betroffenen Stelle  
- Neuer Bezug zu Repository-Inhalten  

### 7.2 Wiederherstellung des Projektkontextes

- Projektanweisung neu laden  
- Glossar erneut referenzieren  
- Zielsetzung korrigieren  

**Beispiel:**  
„Wir haben eine leichte Strukturdrift. Bitte stelle die Phasennummerierung gemäß Makroprozess wieder her.“

### 7.3 Rekalibrierung

- Abgleich mit der zuletzt persistierten Version  
- Neuformulierung fehlerhafter Passagen  
- Klarere Strukturierung zur Stabilisierung

### 7.4 Reparatur-Workflow

1. Drift identifizieren  
2. Ursache benennen  
3. Alle betroffenen Stellen markieren  
4. Konsistente Neuformulierung  
5. Reviewer-Prüfung  
6. Persistenz und Commit  

## 8. Beispiel-Workflows

### 8.1 Drift-Check im operativen Ablauf

**Ablaufbeispiel:**

1. User startet neue Aufgabe  
2. LLM bestätigt Glossar + Struktur  
3. Kleine Abweichung wird bemerkt  
4. LLM korrigiert Terminologie  
5. Arbeit beginnt erst danach  

### 8.2 Drift-Korrektur im Mikroprozess

**Beispiel:**

Ein Dokument wird überarbeitet und das LLM schlägt plötzlich neue Rollen vor.  
Vorgehen:

- Rollendrift benennen  
- bestehende Rollen nachladen  
- Antwort neu erzeugen  
- Reviewer prüfen lassen  
- Persistieren  

### 8.3 Drift-Prüfung im Makroprozess

Phasenspezifische Driftpunkte:

- **Phase 1:** Begriffe stabilisieren  
- **Phase 2:** Strukturachsen fixieren  
- **Phase 3:** Iterative Driftkontrolle  
- **Phase 4:** Widerspruchsbereinigung  
- **Phase 5:** Drift-Schutz durch Persistenz  

## 9. Integration in Makro- und Mikroprozess

Drift-Management ist ein Querschnittsprinzip.  
Es sorgt dafür, dass die Methode stabil bleibt – unabhängig davon, wie lange ein Projekt dauert.

### Im Makroprozess
- schützt Phase 1 vor unklaren Definitionen,  
- stabilisiert Phase 3 gegen operative Drift,  
- sichert Phase 5 als endgültigen Drift-Schutz.

### Im Mikroprozess
- Driftchecks fixieren den Rahmen jeder Iteration,  
- Rollenwechsel werden kontrolliert,  
- Strukturabweichungen werden früh erkannt.

## 10. Weiterführende Dokumente
- persistence-mechanisms.md  
- process-macro.md  
- roles-llm.md  
- methodology-building-blocks.md  

