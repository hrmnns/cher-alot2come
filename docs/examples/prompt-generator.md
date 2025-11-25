# Beispielprojekt: Prompt-Generator WebApp

Dieses Dokument beschreibt ein vollständiges Beispielprojekt gemäß der cher-alot2come-Methodik.  
Die technische Umsetzung der WebApp erfolgt **nicht** in diesem Repository, sondern in einem **separaten Projekt-Repository**.  
Hier werden ausschließlich die **methodischen Schritte, Entscheidungen und Erkenntnisse** dokumentiert.

## 1. Projektsteckbrief

**Titel:** Prompt-Generator WebApp  
**Ziel:** Erzeugung strukturierter Prompts gemäß cher-alot2come (z. B. Start-Prompts, Drift-Korrektur-Prompts).  
**Typ:** Beispielprojekt zur Demonstration der Methode  
**Technologie:** HTML, Tailwind CSS, JavaScript  
**Status:** In Arbeit  

**Verlinktes Code-Repository:**  
*(wird ergänzt, sobald angelegt)*

## 2. Zweck des Beispielprojekts

Dieses Projekt dient dazu, die cher-alot2come-Methodik **konkret, nachvollziehbar und vollständig** anhand eines realen Mini-Tools zu demonstrieren.

Es zeigt exemplarisch:

- Anwendung des **Makroprozesses**  
- Anwendung des **Mikroprozesses**  
- Beispiele für **Drift-Management**  
- Nutzung von **Persistenzmechanismen**  
- Übergabe, Dokumentation und Abschluss eines Teilprojekts

## 3. Projektumfang (Scope)

### 3.1 Funktionaler Umfang
- Auswahl verschiedener Prompt-Kategorien (Start-Prompt, Drift-Korrektur, Persistenz, Rollenaktivierung, Handover etc.)
- Dynamische Felder je Prompt-Kategorie
- Combo-Boxen für eingeschränkte Auswahlfelder (z. B. Rollen, Drift-Arten)
- Markdown-Preview des fertigen Prompts
- „Kopieren in Zwischenablage“-Button
- Optionaler mehrstufiger Workflow mit Fortschrittsbalken
- Header-/Footer-Bereich für Branding und Metainformationen

### 3.2 Nicht-Ziele
- Keine Speicherung von Nutzerdaten  
- Keine Backend-Logik  
- Keine Authentifizierung  
- Kein Deployment innerhalb dieses Repos  

## 4. Durchführung gemäß Makroprozess

### 4.1 Phase 1 – Vorbereitung
- Definition des Projektziels
- Analyse der benötigten Prompt-Kategorien
- Erstellung eines Start-Prompts  
- Erstellen von Issues für Unteraufgaben  

**Ergebnisse:**  
*(Platzhalter für spätere Dokumentation)*

### 4.2 Phase 2 – Problemrahmen definieren
- Klärung des exakten Scopes  
- Auflistung relevanter Rollen  
- Abgrenzung funktionaler und nichtfunktionaler Anforderungen  

**Ergebnisse:**  
*(Platzhalter)*

### 4.3 Phase 3 – Operative Bearbeitung
**Hier werden alle relevanten Mikroprozess-Chats referenziert.**

Beispielhafte Inhalte:

- UI-Design und Komponentenliste  
- Struktur der Prompt-Templates  
- Erstellung dynamischer Formulare  
- Logik zur Markdown-Generierung  
- Copy-to-Clipboard-Funktion  

**Verweise auf Mikroprozess-Chats:**  
- Chat 1: Start des Projekts  
- Chat 2: UI-Design iterativ  
- Chat 3: Prompt-Template-Schema  
- Chat 4: Standardisierter Outputblock  

*(Platzhalter für echte Verlinkungen/Abschnitte)*

### 4.4 Phase 4 – Konsolidierung
- Überprüfung gegen Glossar, Rollenmodell und Prompt-Library  
- Bereinigung von Terminologie  
- Überarbeitung der Feldbenennungen  
- Konsistenzprüfung der Prompt-Templates  

**Ergebnisse:**  
*(Platzhalter)*

### 4.5 Phase 5 – Persistenz
- Ablage dieses Dokuments in `docs/examples/`  
- Ergänzung im Wiki („Beispielprojekt: Prompt-Generator“)  
- Aufnahme in `docs/README.md`  
- Verlinkung zum externen Code-Repository  

**Persistierte Artefakte:**  
- Architekturüberblick  
- Prompt-Template-Struktur  
- Spezifikation der Formularfelder  
- Beispiel-Prompts  

### 4.6 Phase 6 – Abschluss & Übergabe
- Handover-Block für zukünftige Weiterentwicklung  
- Verweis auf Code-Repository  
- Finaler Statusbericht  
- Lessons Learned  

**Abschluss:**  
*(Platzhalter)*

## 5. Mikroprozess-Beispiele

Hier werden exemplarische Chats dokumentiert, die den Mikroprozess A–E durchlaufen.

### 5.1 Mikroprozess-Chat: UI-Grundstruktur
*(Platzhalter für späteres Markdown mit Start-Prompt, Iterationen, Ergebnissicherung und Abschlussblock)*

### 5.2 Mikroprozess-Chat: Prompt-Template-Definition
*(Platzhalter)*

### 5.3 Mikroprozess-Chat: Drift-Korrektur-Beispiel
*(z. B. Strukturdrift oder Begriffsdrift)*

## 6. Drift-Management im Projekt

### 6.1 Beispiele identifizierter Drifts
- Terminologieabweichung bei Prompt-Typen  
- Rollenbezeichnungen inkonsistent  
- Feldnamen im UI vs. in der Dokumentation  

### 6.2 Eingesetzte Korrekturmechanismen
- Drift klar benannt  
- Bezug zur Prompt-Library hergestellt  
- Konsolidierter Prompt neu formuliert  

*(Bei Bedarf echte Chat-Beispiele hier einfügen)*

## 7. Persistenzmechanismen

Beschreibung, wie in diesem Projekt Persistenz angewendet wurde:

- stabile Dokumentation in `docs/examples/`  
- benannte Ergebnisblöcke im Chat  
- Überführung ins externe Repo  
- versionierte Ablage von UI-Assets  
- keine „Chat-Only“-Informationen  

## 8. Architekturüberblick der WebApp

*(Abstrakter Überblick, ohne Code – der Code liegt im anderen Repo)*

### 8.1 Komponenten
- Header  
- Progress-Bar (optional)  
- Prompt-Typ-Auswahl  
- Dynamische Formularfelder  
- Markdown-Preview  
- Footer  

### 8.2 Datenmodell (Prompt-Definition)
- Prompt-Typ  
- Felder  
- Regeln (z. B. „Rolle = ComboBox mit festen Werten“)  
- Markdown-Template  

## 9. Lessons Learned

*(Platzhalter, später ausfüllen)*

Mögliche Aspekte:
- Rollenmodell klar bestimmen früh im Prozess  
- Drift-Management aktiv einsetzen  
- Prompt-Library als Quelle der Wahrheit  
- Beispielprojekte funktionieren besser in separaten Repositories  

## 10. Fazit

Kurzfazit zur Demonstration des Makro-/Mikroprozesses anhand eines realen Mini-Projekts.

*(Platzhalter)*

## 11. Weiterführende Links

- Methode: cher-alot2come (dieses Repository)  
- Prompt-Library  
- Rollenmodell  
- Drift-Management  
- Externes Code-Repository der WebApp *(wird ergänzt)*  
