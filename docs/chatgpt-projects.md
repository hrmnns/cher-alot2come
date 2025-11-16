# Nutzung und Einrichtung von ChatGPT-Projekten

## 1. Zweck von ChatGPT-Projekten

ChatGPT-Projekte dienen dazu, komplexe Vorhaben über längere Zeit hinweg strukturiert zu bearbeiten.  
Sie bieten die Möglichkeit, einen dauerhaften Kontext zu schaffen, der über mehrere Chats hinweg erhalten bleibt.

Sie sind besonders hilfreich bei:
- umfangreichen technischen Projekten (z. B. cher-webapp-core)
- sich entwickelnden Methoden (wie dieses Repository)
- Compliance-Tools, Fragebögen, Framework-Designs
- begleitender Dokumentation über Wochen oder Monate

## 2. Funktionsweise

Ein Projekt definiert:
- einen **Namen**,  
- eine **Beschreibung**,  
- und eine **Projektanweisung**, die dauerhaft aktiv bleibt.

Die Projektanweisung:
- wirkt wie ein persistenter „Systemprompt“  
- ist in allen neuen Chats im Projekt aktiv  
- steuert Rollen, Formatvorgaben, Arbeitsweise und Ziele  
- wird selten geändert und muss stabil bleiben  

Wichtig:
- Projekte speichern **keine** Dateien automatisch.  
- Externe Informationen müssen sauber referenziert werden.  
- Der Kontext wird nicht automatisch aus vorherigen Chats rekonstruiert — die Projektanweisung steuert das Verhalten.

## 3. Einrichtung eines ChatGPT-Projekts

1. Neues Projekt anlegen  
2. Titel und kurze Beschreibung definieren  
3. Projektanweisung einfügen  
4. Erste Chats öffnen  
5. Externe Dokumentation (z. B. in GitHub) einpflegen  
6. Erkenntnisse aus Chats zurück in die Dokumentation schreiben

## 4. Aufbau einer guten Projektanweisung

Eine Projektanweisung muss:

- **kurz** sein  
- **präzise** formuliert sein  
- **stabil** bleiben  
- **rollenbasiertes Verhalten** definieren  
- **Ausgabeformate** festlegen (z. B. Markdown zuerst)  
- **Arbeitsweise** festlegen (z. B. iterative Schritte, Rückfragen bei Unklarheiten)  
- **Konsistenzregeln** enthalten

Beispielhafte Bestandteile:
- Projektziel  
- Rollen des Modells  
- Format- und Strukturvorgaben  
- Do / Don't-Regeln  
- Prinzipien (iteration, clarity, explicitness)

## 5. Was NICHT in eine Projektanweisung gehört

Nicht hinein gehören:
- lange Dokumentationen  
- komplette Methoden oder Leitfäden  
- Schritt-für-Schritt-Tutorials  
- sich ändernde Inhalte oder Work-in-Progress  

Diese Inhalte gehören in:
- Markdown-Dateien im Repository  
- Wiki-Seiten  
- externe Notizen  

## 6. Zusammenspiel mit GitHub-Dokumentation

Die Projektanweisung definiert **das Verhalten des Modells**.  
Die Dokumentation im Repository speichert **das Wissen des Projekts**.

Konsequenz:
- Projektanweisung: stabil, kurz  
- Markdown-Dateien: ausführlich, versionierbar, beliebig erweiterbar  
- Chats: nutzen beide Ressourcen aktiv

## 7. Beispiel für eine kompakte Projektanweisung

```
Projektziel:
Unterstütze mich bei der Entwicklung, Dokumentation und Verbesserung einer Methodik für strukturierte, komplexe Zusammenarbeit mit einem LLM.

Rollen:
Agieren als LLM-Methodiker, Prompt-Engineer, Strukturgeber und Reviewer.

Formatvorgaben:
Immer Markdown. Klare, strukturierte Antworten. Keine Ausschweifungen.

Arbeitsweise:
Iterativ. Rückfragen bei Unklarheit. Konsistenz mit Repository-Dokumentation.

Do:
– Vorschläge für Strukturen
– Konsistenzprüfungen
– saubere Begriffsführung

Don’t:
– lange Dokumente in die Projektanweisung integrieren
– Kontext aus alten Chats annehmen
```
Die in diesem Dokument beschriebene Methodik wird im Rahmen des Projekts „cher-llm-methodology“ selbst angewendet.  Dazu wurde ein dediziertes ChatGPT-Projekt mit einer kompakten Projektanweisung eingerichtet, das als stabiler konzeptioneller Rahmen für alle weiteren Chats dient.

## 8. Best Practices aus diesem Projekt

- Die Projektanweisung bildet die **Steuerlogik**, nicht die Wissensbasis.  
- Markdown-Dateien bilden die **Dokumentationsgrundlage**.  
- Ergebnisse müssen regelmäßig aus dem Chat zurückgeschrieben werden.  
- Große Themen werden in mehrere Chats aufgeteilt.  
- Ein Projekt = ein definierter thematischer Raum.

---

**Version: v0.1 — Erste Dokumentation zu ChatGPT-Projekten**
