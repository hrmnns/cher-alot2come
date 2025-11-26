# Collaboration
Das Beispiel zeigt, wie bei ALOT2COME zwei getrennte Chats zusammenarbeiten:
- Der Meta-Chat strukturiert das Vorgehen, definiert Aufgaben und erstellt Startprompts.
- Der Projekt-Chat führt diese Aufgaben operativ aus und liefert Ergebnisblöcke zurück.

Der Nutzer wechselt zwischen beiden Chats, indem er Startprompts in den Projekt-Chat überträgt und Ergebnisblöcke zur Überprüfung in den Meta-Chat zurückführt. Dieser zyklische Ablauf — Strukturierung → Umsetzung → Review — wird für jede Phase wiederholt und sorgt für Klarheit, Driftsicherheit und saubere Ergebnisse.

## Phase 1

Das Projekt wird definiert, Ziel, Scope und Rahmenbedingungen werden geklärt. Am Ende steht ein sauberer Startpunkt mit klaren Rollen und ersten Strukturen.

### Prompt

``` md
# Phase 1 – Projektvorbereitung starten

Wir beginnen jetzt Phase 1 des Projekts **cher-prompt-generator**.
Bitte übernimm die Rollen *Frontend-Entwickler*, *Strukturgeber* und *Reviewer*.

## Ziel dieser Phase
Einen vollständigen, klar strukturierten Projektrahmen für die spätere Umsetzung der WebApp definieren.

## Aufgaben in Phase 1
- Ziel des Projekts präzise beschreiben
- Scope und Nicht-Scope definieren
- Erste funktionale und nichtfunktionale Anforderungen festlegen
- Technische Basisarchitektur (HTML, Tailwind, JS) grob abstecken
- UI-Hauptkomponenten benennen
- Risiken, offene Punkte und Abhängigkeiten sammeln
- Ergebnis als klaren, kompakten „Vorbereitungsblock“ ausgeben

## Hinweise
- Die methodische Dokumentation liegt im separaten Repository *cher-alot2come*, ist aber **nicht erforderlich** für die technische Umsetzung in diesem Projekt.
- Bitte arbeite technisch fokussiert und ohne Methodikdetails.
- Ergebnisse bitte als saubere Markdown-Blöcke anbieten, damit ich sie direkt ins GitHub-Repo übernehmen kann.

### Bitte beginne mit:
1. einer kurzen Begrüßung als Projektpartner,
2. der Erhebung der Projektparameter (Ziel, Scope, Abgrenzungen),
3. und erzeuge anschließend einen **Ergebnisblock Phase 1 – Vorbereitungsdokument**.

Los geht’s.
```

### Ergebnisblock

``` md
# Phase 1 – Vorbereitungsdokument  
cher-prompt-generator

## 1. Projektziel
Eine minimalistische, rein clientseitige HTML/Tailwind/JS-WebApp, die strukturierte Prompts anhand dynamischer Eingaben erzeugt und in Markdown live darstellt. Ziel ist eine schnelle, klare, zuverlässige Prompt-Erstellung mit Copy-to-Clipboard.

## 2. Scope
- Auswahl verschiedener Prompt-Typen  
- Dynamische Eingabefelder je Typ  
- ComboBoxes für Rollen/Driftarten  
- Markdown-Live-Vorschau  
- Kopierfunktion  
- Optionaler Wizard mit 2–3 Schritten  
- Header & Footer  
- Keine Server-Komponenten  

## 3. Nicht-Scope
- Kein Login, kein Backend  
- Keine Persistenz zwischen Sessions  
- Keine komplexen Frameworks  
- Keine KI-Funktion oder Prompt-Optimierung  
- Keine methodische Anleitung  

## 4. Funktionale Anforderungen
- Prompt-Typ-Auswahl  
- Dynamische Formfelder  
- Markdown-Rendering  
- Copy-to-Clipboard  
- Wizard-Steuerung (optional)  
- Responsives UI  

## 5. Nichtfunktionale Anforderungen
- Minimalistische UI, schnelle Reaktion  
- Browserkompatibilität  
- Keine Cookies/kein Tracking  
- Saubere, modulare Codebasis  

## 6. Architektur (grob)
- HTML als Struktur  
- TailwindCSS  
- Vanilla JS (ES6-Module)  
- Markdown-Renderer (z. B. marked.js)  
- Strukturvorschlag:
  - `/public/index.html`
  - `/public/js/app.js`
  - `/public/js/prompt-types/*`
  - `/public/js/ui/*`
  - `/public/css/tailwind.css`

## 7. Haupt-UI-Komponenten
- Header  
- PromptTypeSelector  
- DynamicFormArea  
- PreviewPane  
- ClipboardButton  
- WizardControls  
- Footer  

## 8. Risiken & Offene Punkte
- Markdown-Library-Auswahl  
- Wizard-Komplexität  
- Modulgrenzen  
- Tailwind-Build oder CDN  
- UX bei langen Prompts
```

## Phase 2

Die fachlichen und technischen Anforderungen werden präzisiert, Begriffe geklärt und Modelle erstellt. Damit entsteht ein stabiles Fundament für alle späteren Entscheidungen.

### Prompt

``` md
# Phase 2 – Problemrahmen definieren

Wir wechseln jetzt in Phase 2. Bitte arbeite weiterhin in der Rolle als Frontend-Entwickler, Strukturgeber und Reviewer.

## Ziel dieser Phase
Den Problemrahmen so präzise definieren, dass wir eine stabile Grundlage für alle Architektur-, UI- und Modellierungsentscheidungen haben.

## Aufgaben in Phase 2
- Definition der zentralen Prompt-Typen für die initiale Version
- Beschreibung der erforderlichen Eingabefelder je Prompt-Typ
- Definition der festen Auswahlwerte (z. B. Rollen, Driftarten)
- Strukturierung des Datenmodells:
  - Prompt-Typ
  - Felder
  - Feldtypen (Textbox, ComboBox, MultiLine, Boolean)
  - Validierungsregeln (falls nötig)
- Klärung der Wizard-Logik (optional)
- Detaillierung der UI-Flows (1-seitig vs. mehrstufig)
- Identifikation von Abhängigkeiten und UX-Spezifika
- Ergebnis als „Ergebnisblock Phase 2 – Problemrahmen“ ausgeben

## Hinweise
- Wir arbeiten weiterhin rein technisch.
- Keine methodischen Inhalte oder Begriffe laden.
- Die Phase dient der Spezifikation, noch nicht der Implementierung.

Bitte starte Phase 2 mit:
1. einer kurzen Einordnung,
2. einer Auflistung der Prompt-Typen, die du für Version 1 vorschlägst,
3. und einer ersten Datenmodell-Skizze.
```

### Ergebnisblock

``` md
# Phase 2 – Problemrahmen  
cher-prompt-generator

## 1. Prompt-Typen (V1)
- Start-Prompt  
- Drift-Korrektur  
- Rollenaktivierung  
- Persistenz-Prompt  
- Handover

## 2. Datenmodell (Grundschema)
### PromptType
- id  
- label  
- description  
- fields[]  
- wizardSteps[] (optional)

### Field
- id  
- label  
- type (textbox | textarea | select | boolean)  
- required  
- placeholder  
- options[] (falls select)  
- validation (optional)

### Prompt-Instanz
- type  
- values{}  

## 3. Felder je Prompt-Typ
### Start-Prompt
- ziel (textarea, required)  
- rolle (select, required)  
- kontext (textarea)  
- arbeitsstil (textbox)  
- constraints (textarea)  
- ausgabeformat (textbox)

### Drift-Korrektur
- driftart (select, required)  
- korrekturtext (textarea, required)  
- ziel (textarea)  
- restriktionen (textarea)

### Rollenaktivierung
- rolle (select, required)  
- rollenbeschreibung (textarea)  
- umfang (textbox)  
- hinweise (textarea)

### Persistenz-Prompt
- regeln (textarea, required)  
- kontext (textarea)  
- sichtbarkeit (select: offen/implizit, required)  
- hinweise (textarea)

### Handover
- kontext (textarea, required)  
- aufgabenstand (textarea, required)  
- ziele (textarea)  
- restriktionen (textarea)  
- adresse (textbox)

## 4. Feste Auswahlwerte
### Rollen
Assistent, Experte, Reviewer, Analyst, Erklärer, Coach, Ideengeber

### Driftarten
Fokusverlust, Stilabweichung, Rollendrift, Zielverfehlung, Unklare Struktur

### Persistenz-Sichtbarkeit
offen, implizit

## 5. Wizard-Logik
- optional  
- schrittbasiert  
- Step = Gruppe von Feldern  
- Falls keine Steps definiert → Single-Page

## 6. UI-Flows
- Flow A: Single-Page mit dynamischem Formular + Vorschau  
- Flow B: Wizard mit Fortschrittsanzeige  

## 7. Abhängigkeiten & UX-Punkte
- Markdown-Sicherheit  
- zentrales Options-Management  
- State-Handling je Prompt-Typ  
- Debouncing für Vorschau  
- Mobile-Optimierung  
- Minimierung der visuellen Überladung
```

## Phase 3

Die eigentliche Umsetzung beginnt: Module, Strukturen, Inhalte oder Funktionen werden iterativ entwickelt. Der Fokus liegt auf greifbaren Ergebnissen und funktionsfähigen Artefakten.

### Prompt

``` md
# Phase 3 – Operative Bearbeitung

Wir starten nun Phase 3. Bitte arbeite weiterhin als Frontend-Entwickler, Strukturgeber und Reviewer.  
Ziel: Die technische Umsetzung des Prompt-Generators vorbereiten und erste Bausteine erstellen.

## Aufgaben in Phase 3
1. Erzeugung einer soliden Projektstruktur im `src/`-Bereich:
   - `/src/index.html`
   - `/src/js/app.js`
   - `/src/js/types.js` (Prompt-Typen + Felder)
   - `/src/js/ui/*.js` (UI-Komponenten)
   - `/src/assets/icon.svg`

2. Implementierung der **Grundgerüste**:
   - Header-Komponente
   - Prompt-Typ-Auswahl (ComboBox)
   - Platzhalter-basiertes `DynamicFormArea`
   - Markdown-Vorschau (Platzhalter)
   - Footer-Komponente

3. Erstellung eines Datenmodells:
   - `PromptTypes` (Enum + Definition)
   - Felderstrukturen je Prompt-Typ
   - Feste Auswahlwerte (Rollen, Driftarten, Persistenz-Sichtbarkeit)

4. Einrichtung der State-Logik:
   - `currentType`
   - `currentValues`
   - Rendering-Funktionen

5. Ausgabe als **„Ergebnisblock Phase 3 – Grundstruktur & Setup“**.

## Hinweise
- Fokus liegt auf Struktur, Templates, klarer Codebasis.
- Noch keine vollständige UI und keine Templates für fertige Prompts.
- Bitte klare Modulgrenzen und saubere Benennungen verwenden.

Bitte beginne Phase 3 mit:
1. dem Aufbau der Projektstruktur,
2. und der Erzeugung der HTML-Basis mit Header, Hauptbereich und Footer.
```

### Ergebnisblock

``` md
# Phase 3 – Grundstruktur & Setup  
cher-prompt-generator

## 1. Projektstruktur
- /src/index.html  
- /src/js/app.js  
- /src/js/types.js  
- /src/js/state.js  
- /src/js/ui/*.js (Header, Footer, Selector, Form, Preview)  
- /src/assets/icon.svg  

## 2. HTML-Basis
- Tailwind via CDN  
- Header, Main, Footer  
- Zwei-Spalten-Layout (Form links, Preview rechts)  

## 3. JS-Basis
- PromptTypes + PromptDefinitions  
- Rollen, Driftarten, Persistenz-Sichtbarkeit  
- State-Objekt (`currentType`, `currentValues`)  
- UI-Gerüste: Header, Footer, Selector, DynamicFormArea, PreviewPane  

## 4. Rendering-Flow
- App initialisiert Header/Footer  
- Prompt-Type-Selector lädt dynamische Formfelder  
- Preview zeigt Platzhalter  
- Saubere Modulgrenzen und klare Benennung  

## 5. Nächste Schritte (Phase 4)
- Event-Handling für Formularfelder  
- State-Updates in Echtzeit  
- Markdown-Rendering  
- Copy-to-Clipboard  
- Ausarbeitung der finalen Prompt-Templates  
```

## Phase 4

Die bisherigen Ergebnisse werden überprüft, bereinigt, vereinheitlicht und stabilisiert. Strukturen werden geradegezogen, Inkonsistenzen behoben und der Gesamtstand gesichert.

### Prompt

``` md
# Phase 4 – Konsolidierung

Wir starten Phase 4. Bitte arbeite weiterhin als Frontend-Entwickler, Strukturgeber und Reviewer.

## Ziel dieser Phase
Die bisherige Grundstruktur funktional zu schließen, Event-Handling zu implementieren und die Kernlogik für dynamische Formulare, Markdown-Ausgabe und Copy-Funktion zu stabilisieren.

## Aufgaben in Phase 4
1. Implementierung der Event-Handler für alle Feldtypen  
2. Live-Updates im State-Objekt  
3. Dynamische Generierung der Markdown-Vorschau  
4. Implementierung des Copy-to-Clipboard-Buttons  
5. Konsolidierung der UI-Komponenten  
6. Ausarbeitung der finalen Prompt-Templates  
7. Ergebnis als **„Ergebnisblock Phase 4 – Konsolidierung“** ausgeben

## Hinweise
- Fokus liegt auf Funktionalität und Stabilität.  
- UI-Design kann minimal bleiben.  
- Sobald die Kernlogik steht, folgen Feinschliff und UX-Verbesserungen in Phase 5.

Bitte starte Phase 4 mit:
1. Einrichtung des Event-Handlings,
2. und der Implementierung der State-Updates in Echtzeit.
```

### Ergebnisblock

``` md
# Phase 4 – Konsolidierung  
cher-prompt-generator

## 1. Implementiert
- Event-Handling für alle Feldtypen  
- Live-State-Updates (input → state → preview)  
- Dynamische Markdown-Generierung  
- Prompt-Templates für alle Prompt-Typen  
- Copy-to-Clipboard integriert  
- UI-Komponenten konsolidiert  

## 2. Neue Module
- renderer.js → Markdown-Generator  
- aktualisierte dynamicFormArea.js  
- aktualisiertes previewPane.js  
- erweiterte app.js  

## 3. Stabiler Rendering-Flow
- Eingabe → Event → State-Update → Markdown-Generator → Preview  

## 4. Status nach Phase 4
Die WebApp ist funktionsfähig, reagiert auf Eingaben und erzeugt Markdown-Prompts.  
Die Kernlogik steht, die Module sind sauber getrennt und erweiterbar.

## 5. Grundlage für Phase 5
- Markdown-to-HTML-Rendering  
- UI-Polishing  
- Wizard-Modus  
- Error-Handling / Validierung  
- Mobile-Optimierung  
```

## Phase 5

Details, UX, Qualität und Robustheit werden verbessert, letzte Lücken geschlossen. Das Projekt wird reif für Abschluss und Übergabe gemacht.

### Prompt

``` md
# Phase 5 – Feinschliff & Finalisierung

Wir starten Phase 5. Bitte arbeite weiterhin als Frontend-Entwickler, Strukturgeber und Reviewer.

## Ziel dieser Phase
Die WebApp funktional zu verfeinern, stabiler und benutzerfreundlicher zu machen, sowie vorbereitende Schritte für den Wizard-Mode und den späteren Abschluss zu realisieren.

## Aufgaben in Phase 5
1. UI-Polishing:
   - Abstände, Typografie, Farben
   - Layout-Stabilität (Desktop & Mobile)
   - visuelle Klarheit der Formulare und Preview

2. Optionales Markdown-to-HTML-Rendering ergänzen

3. Wizard-Modus (Grundstruktur):
   - Step-Bar
   - Step-Container
   - Navigation (Weiter/Zurück)

4. Validierung & Error-Handling für Pflichtfelder

5. Mobile-Optimierung:
   - responsive Breakpoints
   - Spaltenverhalten (Stacking)
   - Touch-Interaktionen

6. Ergebnis als **„Ergebnisblock Phase 5 – Feinschliff & Optimierung“** ausgeben.

## Hinweise
- Fokus: Qualität, UX und Stabilität.
- Keine neuen Prompt-Typen oder Datenmodelle einführen.
- Wizard zunächst nur grundlegend implementieren.

Bitte starte Phase 5 mit:
1. UI-Polishing der bestehenden Komponenten,
2. und einer stabilen responsiven Grundstruktur.
```

### Ergebnisblock

Alle Ergebnisse werden final dokumentiert, gebündelt und als Release oder Handover-Paket übergeben. Das Projekt wird offiziell abgeschlossen und für spätere Nutzung bereitgestellt.

``` md
# Phase 5 – Feinschliff & Optimierung  
cher-prompt-generator

## 1. UI-Polishing
- konsistente Abstände, paddings, margins  
- klare Typografie (größer, einheitlich, kontrastreich)  
- Panels mit rounded-xl, soft-shadow, border-gray-100  
- Header/Footer harmonisiert  
- Formlabels präzise, required-Felder markiert  

## 2. Responsive Optimierung
- stabile max-width (6xl)  
- Grid stackt sauber auf Mobil  
- Panels mit min-h für Scroll-Stabilität  

## 3. Markdown-to-HTML-Rendering (optional)
- Preview nutzt `marked`  
- HTML-Ansicht in Prose-Container  
- verbessert Lesbarkeit & UX  

## 4. Wizard-Modus (Grundstruktur)
- Step-Bar  
- Step-Container  
- Weiter/Zurück-Navigation  
- neutral eingebunden, kein Einfluss auf Single-Page-Mode  

## 5. Validierung & Error-Handling
- Pflichtfelder mit rot markiert  
- Validierung bei jeder Eingabe  
- einfache Feedback-Logik  

## 6. Stand nach Phase 5
Die App hat nun:
- stabiles Layout  
- mobile Optimierung  
- Markdown-/HTML-Vorschau  
- Wizard-Grundgerüst  
- visuelle Klarheit und verbesserte Bedienbarkeit  

Bereit für Phase 6 (Abschluss, Review und Vorbereitung auf Release).
```

## Phase 6

### Prompt

``` md
# Phase 6 – Abschluss & Übergabe

Wir starten Phase 6. Bitte arbeite weiterhin als Frontend-Entwickler, Strukturgeber und Reviewer.

## Ziel dieser Phase
Die WebApp finalisieren, dokumentieren, stabilisieren und für ein Release vorbereiten.  
Sichtbare Ergebnisse und klare Übergabepunkte sollen entstehen.

## Aufgaben in Phase 6
1. Finaler UI-Check (Layout, Abstände, Fehlerfälle)
2. Konsolidierung aller Prompt-Templates (Finale V1-Version)
3. Erstellung klarer Markdown-Blöcke für:
   - README-Auszug
   - Features
   - Strukturübersicht
   - Projektarchitektur
4. Erstellung eines minimalen Release-Bundles:
   - index.html  
   - js-Module  
   - assets/icon  
5. Finaler "Ergebnisblock Phase 6 – Abschluss & Ready for Release"
6. Optional: Mini-Demo-Section in index.html integrieren

## Hinweise
- Keine neuen Features einführen.
- Fokus: Klarheit, Stabilität, Release-Fähigkeit.
- Bitte achte auf vollständige Konsistenz der Beschriftungen, Feldnamen und Typen.

Bitte beginne Phase 6 mit:
1. Finalem UI-Check,
2. und der schriftlichen Konsolidierung aller Prompt-Templates.

```

### Ergebnisblock

``` md
# Phase 6 – Abschluss & Ready for Release  
cher-prompt-generator

## 1. Finaler UI-Check
- Mobile & Desktop stabil
- Saubere Abstände, klare Typografie
- Panels konsistent (shadow-md, rounded-xl)
- Pflichtfeld-Validierung integriert
- Copy-Funktion zuverlässig
- Preview (Markdown + HTML) solide

## 2. Konsolidierte Prompt-Templates (V1)
- Start-Prompt
- Drift-Korrektur
- Rollenaktivierung
- Persistenz-Prompt
- Handover
→ konsistent, vollständig, releasefertig

## 3. Dokumentation
- README-Auszug
- Features-Block
- Projektarchitektur
- Strukturübersicht
→ alles als Markdown bereitgestellt

## 4. Release-Bundle (bereits erzeugt)
- index.html
- vollständige JS-Module (app.js, types.js, state.js, renderer.js, ui/*)
- assets/icon.svg

## 5. Status
Die WebApp ist:
- funktional vollständig
- UX-optimiert
- modular erweitertbar
- release-ready

## 6. Nächste Schritte (optional)
- GitHub Readme finalisieren
- Pages-Deployment hinzufügen
- Versionstag `v1.0.0`
```

