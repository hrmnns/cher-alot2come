# 📘 Beispielprojekt: Prompt-Generator (V1)

Dieses Kapitel beschreibt das vollständige Beispielprojekt **„Prompt-Generator“**, das die Anwendung der cher-alot2come-Methodik exemplarisch demonstriert.
Der Prompt-Generator ist ein kleines, rein clientseitiges WebTool, mit dem strukturierte Prompts auf Basis der Methodik erzeugt werden können.

Die **technische Umsetzung** befindet sich im separaten Repository:

👉 **[https://github.com/hrmnns/cher-prompt-generator](https://github.com/hrmnns/cher-prompt-generator)**  
👉 **[https://github.com/hrmnns/cher-prompt-generator/src/index.html](https://github.com/hrmnns/cher-prompt-generator/src/index.html)**

Dieses Kapitel konzentriert sich ausschließlich auf die **methodische Durchführung**.

# 1. Projektsteckbrief

**Titel:** Prompt-Generator WebApp
**Projektart:** Demonstrator / Beispielprojekt
**Technologie:** HTML, Tailwind CSS, Vanilla JavaScript
**Ziel:** Zeigen, wie ein reales Mini-Projekt vollständig nach dem Makro- und Mikroprozess der cher-alot2come-Methodik durchgeführt wird.
**Ergebnis:** Funktionale WebApp, vollständige Dokumentation, Release-Bundle.

# 2. Zweck des Beispielprojekts

Das Beispielprojekt dient dazu zu demonstrieren:

* wie man ein Thema **methodisch sauber** von Phase 1–6 durchführt,
* wie man **Drift-Kontrolle**, **Persistenz**, **Rollenmodell** und **Startprompts** nutzt,
* wie man zwei parallele Chats (Meta/Projekt) koordiniert,
* wie man Ergebnisse sauber ins Repo überführt,
* und wie aus einem abstrakten Problem eine strukturierte Lösung entsteht.

Das Projekt ist bewusst **klein, überschaubar und vollständig dokumentiert**, um als Lern- und Referenzbeispiel zu dienen.

# 3. Vorgehen gemäß Makroprozess

Das Beispielprojekt wurde vollständig entlang des cher-alot2come-Makroprozesses durchgeführt:

## **Phase 1 – Vorbereitung**

* Projektziel geklärt
* Scope / Nicht-Scope definiert
* erste funktionale Anforderungen gesammelt
* Projektanweisung im Projekt-Chat formuliert
* initialer Projektaufbau erarbeitet

**Persistiert als:**
`docs/examples/prompt-generator/phase-1.md` *(empfohlen)*

## **Phase 2 – Problemrahmen definieren**

* Definition der Prompt-Typen (5 Typen)
* Definition aller Felder je Typ
* Datenmodell (PromptType, Field, PromptInstance)
* Auswahlwerte (Rollen, Driftarten etc.)
* UI-Flows und Wizard-Konzept

**Ergebnis:** vollständige funktionale Spezifikation.

## **Phase 3 – Operative Bearbeitung**

* Grundstruktur der WebApp angelegt
* Projektstruktur definiert (`src/`, `js/`, `ui/`)
* HTML-Skeleton + Header/Footer
* State-Management eingerichtet
* dynamische Formfelder & Preview-Placeholder

**Ergebnis:** funktionierendes Grundgerüst.

## **Phase 4 – Konsolidierung**

* Event-Handling
* Live-State-Updates
* Markdown-Generator
* Prompt-Templates
* Copy-to-Clipboard
* Modulgrenzen bereinigt

**Ergebnis:** voll funktionsfähige Kernlogik.

## **Phase 5 – Feinschliff & Optimierung**

* UI-Polishing
* Responsive Design
* Markdown-to-HTML-Ansicht
* Validierung & Error-Handling
* Wizard-Grundstruktur

**Ergebnis:** benutzerfreundliche, stabile App.

**Hinweis:** Die Phase 5 des Beispielprojekts („Feinschliff & Optimierung“) unterscheidet sich funktional von Phase 5 des Makroprozesses („Persistenz“). Da das Beispielprojekt ein technisches Softwareprojekt ist, fügt es eine projektspezifische Feinschliffphase zwischen Konsolidierung und Abschluss ein. Persistenz und Projektabschluss entsprechen im Beispielprojekt der Phase 6. Damit ergibt sich folgende Zuordnung:
- Beispiel Phasen 1–4 ↔ Makroprozess Phasen 1–4
- Beispiel Phase 5 ↔ operative/konsolidierende Vertiefung (Phase 3/4)
- Beispiel Phase 6 ↔ Makroprozess Phase 5–6

## **Phase 6 – Abschluss & Übergabe**

* Finaler UI-Check
* konsolidierte Templates
* Dokumentationspaket erstellt
* Release-Bundle generiert
* V1.0.0 bereit

**Ergebnis:** Projekt abgeschlossen & release-ready.

# 4. Drift-Management im Beispielprojekt

Während des Projekts wurden mehrere Formen von Drift aktiv identifiziert und korrigiert, u. a.:

### **Begriffliche Drift**

* unterschiedliche Bezeichnungen für Prompt-Typen
* wurde korrigiert durch Abgleich mit Phase-2-Datenmodell

### **Strukturdrift**

* UI-Ablauf war uneindeutig (Wizard vs. Single-Page)
* wurde durch klare Priorisierung (Single-Page als Standard) behoben

### **Rollen-/Zieldrift**

* der Projektchat neigte teilweise dazu, zusätzliche Features vorzuschlagen
* wurde per Prompt-Korrektur gestoppt („kein Backend, keine neuen Prompt-Typen“)

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
