# 📘 Beispielprojekt: Prompt-Generator (V1)

Dieses Kapitel beschreibt das vollständige Beispielprojekt **„Prompt-Generator“**, das die Anwendung der ALOT2COME-Methodik exemplarisch demonstriert. Der Prompt-Generator ist ein kleines, rein clientseitiges WebTool, mit dem strukturierte Prompts auf Basis der Methodik erzeugt werden können.

Die **technische Umsetzung** befindet sich im separaten Repository:

👉 **[https://github.com/hrmnns/cher-prompt-generator](https://github.com/hrmnns/cher-prompt-generator)**  
👉 **[https://github.com/hrmnns/cher-prompt-generator/src/index.html](https://github.com/hrmnns/cher-prompt-generator/src/index.html)**

Dieses Kapitel konzentriert sich ausschließlich auf die **methodische Durchführung**.

# 1. Projektsteckbrief

Das Beispielprojekt ist bewusst kompakt gehalten. Es eignet sich ideal, um das Zusammenspiel von Makroprozess, Mikroprozess, Rollenmodell, Persistenz und Drift-Management an einem greifbaren Artefakt zu demonstrieren.

- Titel: Prompt-Generator WebApp
- Projektart: Beispielprojekt / Demonstrator
- Technologie: HTML, Tailwind CSS, Vanilla JavaScript
- Ziel: Praxisbeispiel für die Anwendung von ALOT2COME über alle relevanten Phasen hinweg
- Ergebnis: Eine funktionale WebApp inkl. Release-Bundle und veröffentlichter Version

# 2. Zweck des Beispielprojekts

Das Beispielprojekt dient dazu zu demonstrieren:

* wie man ein Thema **methodisch sauber** von Phase 1–6 durchführt,
* wie man **Drift-Kontrolle**, **Persistenz**, **Rollenmodell** und **Startprompts** nutzt,
* wie man zwei [parallele Chats](../processes/parallel-chat-coordination.md) (Meta/Projekt) koordiniert,
* wie man Ergebnisse sauber ins Repo überführt,
* und wie aus einem abstrakten Problem eine strukturierte Lösung entsteht.

Das Projekt ist bewusst **klein, überschaubar und vollständig dokumentiert**, um als Lern- und Referenzbeispiel zu dienen.

# 3. Vorgehen gemäß Makroprozess

Die Durchführung folgt eng den Makrophasen von ALOT2COME. Jede Phase erzeugt klar benannte Zwischenstände, die teilweise direkt ins Repo übertragen werden.

## **Phase 1 – Vorbereitung**

Zu Beginn wurde definiert, was der Prompt-Generator leisten soll und welchen Rahmen das Projekt hat. Kontext, Ziele und Nicht-Ziele wurden präzisiert, ebenso wie die grundlegende Arbeitsweise im Projektchat und das Format des Startprompts. In dieser Phase entsteht außerdem die Projektanweisung für den Meta-Chat.

Ergebnis: ein sauber abgegrenzter Projektstart, der später Drift verhindert.

## **Phase 2 – Problemrahmen definieren**

In dieser Phase wurden alle notwendigen Begriffe, Modelle und Strukturen erarbeitet:
- Definition der fünf Prompt-Typen
- Festlegung der Felder pro Typ
- Datentypen für die generierenden Elemente
- UI-Abläufe und Wizard-Logik
- Rollen und Auswahlwerte für die spätere Nutzung

Diese Phase stellt sicher, dass das Projekt fachlich sauber fundamentiert ist und dass spätere Entscheidungen auf einer stabilen Basis aufsetzen.

**Ergebnis:** vollständige funktionale Spezifikation.

## **Phase 3 – Operative Bearbeitung**

Anschließend wurde die technische Basis der WebApp aufgebaut. Der Chat diente dabei als Ort für Iterationen über Struktur, Komponenten, Datenfluss und Architektur. Die Ergebnisse dieser Phase waren:
- ein HTML-Grundgerüst
- klare Projektstruktur im Repository
- dynamische Formfelder und erste Vorschaukomponenten

Hier zeigt sich der Mikroprozess besonders deutlich: jeder Arbeitsschritt beginnt mit Fokus-Setzung, Rollenaktivierung und kleinschrittigen Iterationen.

**Ergebnis:** funktionierendes Grundgerüst.

## **Phase 4 – Konsolidierung**
In dieser Phase wurde die technische Logik stabilisiert:
- Event-Handling vereinheitlicht
- State-Management geklärt
- Markdown-Generator integriert
- Prompt-Templates konsolidiert

Die Konsolidierung ist ein wiederkehrender Mechanismus im Makroprozess: hier werden Strukturen vereinheitlicht und driftanfällige Stellen bereinigt.

**Ergebnis:** voll funktionsfähige Kernlogik.

## **Phase 5 – Feinschliff & Optimierung**

Diese Phase war notwendig, da es sich um ein Softwareprojekt handelt. Sie entspricht einer operativen Vertiefung zwischen Phase 3 und 4 des Makroprozesses:

- UI-Optimierung
- Responsivität / Responsive Design
- Validierung
- bessere Bedienbarkeit

Dies ist ein gutes Beispiel dafür, wie ALOT2COME flexibel mit projektspezifischen Ergänzungen umgehen kann, ohne die Prozesslogik zu verwässern.

**Ergebnis:** benutzerfreundliche, stabile App.

**Hinweis:** Die Phase 5 des Beispielprojekts („Feinschliff & Optimierung“) unterscheidet sich funktional von Phase 5 des Makroprozesses („Persistenz“). Da das Beispielprojekt ein technisches Softwareprojekt ist, fügt es eine projektspezifische Feinschliffphase zwischen Konsolidierung und Abschluss ein. Persistenz und Projektabschluss entsprechen im Beispielprojekt der Phase 6. Damit ergibt sich folgende Zuordnung:
- Beispiel Phasen 1–4 ↔ Makroprozess Phasen 1–4
- Beispiel Phase 5 ↔ operative/konsolidierende Vertiefung (Phase 3/4)
- Beispiel Phase 6 ↔ Makroprozess Phase 5–6

## **Phase 6 – Abschluss & Übergabe**
Zum Ende wurden:
- finale Templates konsolidiert
- ein Release-Bundle erzeugt
- UI- und Funktionsprüfung durchgeführt
- Version 1.0.0 bereitgestellt
- in strukturierter Handover erstellt

Dies entspricht den Phasen 5 & 6 des Makroprozesses: Persistenz + Abschluss.

**Ergebnis:** Projekt abgeschlossen & release-ready.

# 4. Drift-Management im Beispielprojekt

Während des Projekts wurden mehrere Formen von Drift aktiv identifiziert und korrigiert, u. a.:

### **Begriffliche Drift**

Frühe Entwürfe verwendeten unterschiedliche Bezeichnungen für Prompt-Typen. Durch Abgleich mit dem Datenmodell (Phase 2) wurde dies korrigiert.

### **Strukturdrift**

UI-Abläufe wurden während der Iterationen unterschiedlich interpretiert. Durch eine bewusste Entscheidung (Single-Page statt Wizard-Zwang) wurde die Struktur stabilisiert.

### **Rollen-/Zieldrift**

Der Implementierungs-Chat schlug gelegentlich zusätzliche Features vor. Durch Mini-Drift-Checks und klar formulierte Fokusbegrenzungen wurde die Zielausrichtung wiederhergestellt. Das Projekt zeigt damit, wie Drift-Erkennung, Drift-Check und Drift-Korrektur praktisch funktionieren.

Das Projekt demonstriert damit aktiv **Erkennung & Reparatur von Drift**, ein zentraler Bestandteil von cher-alot2come.

# 5. Persistenzmechanismen im Beispielprojekt

Das Projekt zeigt exemplarisch, wie Persistenz funktioniert:

* Jede abgeschlossene Phase wurde **in einem Ergebnisblock** festgehalten.
* Diese Ergebnisblöcke wurden in Markdown-Dateien übernommen.
* Alle technischen Artefakte liegen im separaten Repository.
* Die methodischen Teile liegen ausschließlich in diesem Methoden-Repo.
* Keine Vermischung → klare Trennung zwischen *Methode* und *Beispielprojekt*.

# 6. Lessons Learned

Das Beispielprojekt hat mehrere wichtige Erkenntnisse geliefert:

### **1. Zwei parallele Chats funktionieren hervorragend**

* Meta-Chat = Struktur, Methode, Review
* Projekt-Chat = Implementierung
  → Eliminierung von Drift & Scope-Creep.

### **2. Klare Startprompts sind entscheidend**

Die Qualität eines Arbeitsschritts ist stark abhängig vom Startblock.

### **3. Modulare Ergebnisblöcke beschleunigen Persistenz**

Jede Phase hatte ein klares Output-Artefakt → hoher Wiederverwendungswert.

### **4. Kleine Tools eignen sich ideal als Demonstratoren**

Die Methode wird am besten an überschaubaren, aber vollständigen Projekten erklärt.

### **5. Datenmodell + UI-Struktur früh festlegen**

Dies verhindert die häufigste Driftform in Softwareprojekten: strukturelle Drift.

# 7. Fazit

Das Beispielprojekt „Prompt-Generator“ demonstriert die cher-alot2come-Methodik **end-to-end**:

* klare Phasen
* saubere Ergebnisblöcke
* Driftkontrolle
* konsistente Persistenz
* parallele Arbeitskontexte
* Release-Fähigkeit

Damit dient es als **vollständiges Referenzprojekt** für alle Anwender, die verstehen wollen, wie die Methode in der Praxis funktioniert.

# 8. Weiterführende Links

* **Methoden-Repo (dieses Repository)**
* **Prompt-Generator – Code-Repository:**
  [https://github.com/hrmnns/cher-prompt-generator](https://github.com/hrmnns/cher-prompt-generator)
* **Beispielhafte Ergebnisblöcke (Phasen 1–6)**
* **Workflow: Arbeiten mit zwei parallelen Chats**
