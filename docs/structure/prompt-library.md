# Prompt Library

Die Prompt Library bündelt alle wiederkehrenden, getesteten und stabilen Prompts im ALOT2COME-Framework. Sie dient als Werkzeugkasten für die operative Zusammenarbeit mit dem LLM über alle Phasen des Makro- und Mikroprozesses hinweg.

Ziel der Sammlung ist es:

- robuste und driftresistente Prompts jederzeit verfügbar zu machen
- Rollen sauber und konsistent zu aktivieren
- Startpunkte für neue Chats klar zu definieren
- Übergaben, Persistenzschritte und Korrekturmechanismen zu standardisieren
- eine einheitliche Interaktion über viele Iterationen sicherzustellen

Die Prompt Library ist ein struktureller Baustein der Methodik und erleichtert sowohl die Arbeit des Nutzers als auch die Stabilität des LLM durch präzise Steuerimpulse. Alle Prompts sind kategorisiert, methodisch begründet und kompatibel mit Drift-Management, Persistenzmechanismen und Rollenmodell.

# 1. Start-Prompts (Chat-Start / Mikroprozess Phase A)

### 1.1 Standard-Start-Prompt

**Zweck:** Setzt methodischen Rahmen und Ziel.\
**Wirkung:** Aktiviert korrekten Rollenmodus, verhindert frühen Drift.\
**Risiken:** Unklare Ziele, Rollendrift.\
**Prozessbezug:** Mikroprozess A.

``` md
Bitte agiere als LLM-Methodiker.
Wir starten eine neue Arbeitseinheit.
Kontext: <Kurzkontext>.
Ziel dieses Chats: <konkretes Ziel>.
Arbeitsmodus: <Modus>.
Relevante Artefakte: <Dateien, Issues>.
Bitte bestätige den Start-Prompt.
```

### 1.2 Start-Prompt für Issue-Bearbeitung

**Zweck:** Richtet den Chat sauber am Issue aus.\
**Wirkung:** Verhindert Abweichungen.\
**Risiken:** Fehlinterpretation.\
**Prozessbezug:** Mikroprozess A / Phase 3.

``` md
Neuer Chat zur Bearbeitung von Issue <Nummer>.
Bitte als Methodiker arbeiten.
Kontext: <Kurzfassung aus dem Issue>.
Ziel: <Ziel des Issues>.
Bitte bestätige Rollen, Ziel und Vorgehen.
```

### 1.3 Start-Prompt für Dokumentüberarbeitung

**Zweck:** Schützt persistierte Struktur.\
**Wirkung:** Strukturarbeit ohne Inhaltserweiterung.\
**Risiken:** Strukturdrift.\
**Prozessbezug:** Phase 4--5.

``` md
Bitte agiere als Strukturgeber.
Wir überarbeiten Abschnitt <Name> aus <Dokument>.
Ziel: Struktur verbessern, ohne Inhalte zu verändern.
Arbeitsmodus: Strukturierung.
```

# 2. Drift-Korrektur-Prompts

### 2.1 Begriffsdrift korrigieren

**Zweck:** Stoppt semantische Drift.\
**Wirkung:** Rückführung auf Glossardefinition.\
**Risiken:** Verwässerte Terminologie.\
**Prozessbezug:** Drift-Korrektur.

``` md
Wir haben eine Begriffsdrift: Der definierte Begriff ist "<Begriff>".
Bitte korrigiere alle abweichenden Stellen.
```

``` md
Bitte stelle die Struktur gemäß Repository-Version wieder her (Datei: <Pfad>).
```

### 2.2 Kontextrekalibrierung

``` md
Bitte lade die Projektanweisung neu und bestätige die gültigen Begriffe aus dem Glossar.
```

``` md
Wir haben eine leichte Strukturdrift. Bitte stelle die Phasennummerierung gemäß Makroprozess wieder her.
```

### 2.3 Vergleich mit Repository

``` md
Vergleiche deine letzte Antwort mit der Version aus <Dokument>.
Liste alle Abweichungen auf.
```

``` md
Bitte formuliere den Abschnitt neu, strikt entlang der persistierten Struktur aus <Dokument>.
```

### 2.4 Reparatur-Workflow

``` md
Bitte markiere alle Passagen, die von der persistierten Version abweichen.
```

``` md
Aktiviere Reviewer.
Prüfe die Überarbeitung auf Konsistenz und Driftfreiheit.
```

# 3. Persistenz-Prompts

### 3.1 Repository-Übergabe vorbereiten

``` md
Bitte liefere den Ergebnisblock als sauberen, getrennten Block.
Ohne Meta-Text.
Status: "final für Repository".
```

### 3.2 Persistenz-Check

``` md
Bitte prüfe dieses Ergebnis gegen bestehende Dokumente auf:
– Begriffe
– Struktur
– Konsistenz
– Versionen.
```

### 3.3 Auswahl der Zielorte

``` md
Welcher Abschnitt und welche Datei sind gemäß Informationsarchitektur korrekt für dieses Ergebnis?
```

### 3.4 Übergabeformat

``` md
Bitte gib eine Repository-fertige Fassung des Ergebnisblocks gemäß Formatregeln aus.
```

# 4. Rollenaktivierungs-Prompts

### 4.1 LLM-Methodiker

``` md
Bitte agiere als LLM-Methodiker.
Prüfe Struktur, Vorgehen, Konsistenz und Zielklarheit dieses Abschnitts.
```

### 4.2 Strukturgeber

``` md
Bitte agiere als Strukturgeber.
Erstelle eine präzise Gliederung für <Thema>. Kein Fließtext.
```

### 4.3 Reviewer

``` md
Bitte agiere als Reviewer.
Prüfe diesen Text ausschließlich auf:
– Logik
– Konsistenz
– Terminologie
– Struktur (ohne neue Inhalte).
```

### 4.4 Prompt-Engineer

``` md
Bitte agiere als Prompt-Engineer.
Optimiere diesen Prompt für Ambiguitätsresistenz und Rollenstabilität.
```

### 4.5 Domänenexperte

``` md
Bitte agiere als Domänenexperte für <Domäne>.
Erkläre <Begriff> und gib ein kurzes Beispiel.
```

# 5. Handover-Prompts

### 5.1 Übergabe an neuen Chat

``` md
Bitte erstelle einen Handover-Block mit:
– Kontext
– bisherigen Ergebnissen
– offenen Punkten
– nächstem Schritt.
```

### 5.2 Übergabe an Issue

``` md
Bitte erstelle einen Handover-Block für ein neues Issue:
– Thema
– Aktueller Stand
– Offenes
– Benötigte Rolle
– Betroffene Dateien.
```

### 5.3 Übergabe zur Persistenz

``` md
Bitte erstelle den Handover-Block zur Persistenz:
– Inhalte zur Übertragung
– Quelle
– Zielort
– Hinweise / Versionierung.
```

### 5.4 Abschluss eines Chats

``` md
Bitte stelle einen Abschlussblock bereit:
– Zusammenfassung
– Offene Punkte
– Repository-Übergaben
– Nächste Schritte.
```

# 6. Mini-Checks

### 6.1 Drift-Check

``` md
Bitte bestätige Terminologie, Struktur und Zielrahmen dieser Arbeitseinheit.
```

### 6.2 Rollen-Check

**Zweck:** Rollenklarheit.\
**Wirkung:** Modell arbeitet bewusst im richtigen Modus.\
**Risiken:** Rollenvermischung.\
**Prozessbezug:** Mikroprozess A.

``` md
In welcher Rolle arbeitest du gerade?
```

### 6.3 Struktur-Check

**Zweck:** Sicherstellt korrekte Begriffe und Struktur.\
**Wirkung:** Synchronisation mit Repo.\
**Risiken:** Begriffs- und Strukturdrift.\
**Prozessbezug:** Drift-Check.

``` md
Bitte gib die gültige Prozess- oder Dokumentstruktur aus <Dokument> wieder.
```

# 7. Quick-Prompts

``` md
Bitte zurück zum Fokus.
```

``` md
Bitte bestätige den aktuellen Zielrahmen.
```

``` md
Bitte gib drei Strukturvarianten.
```

``` md
Bitte gib eine stabile Version als Ergebnisblock.
```

``` md
Bitte liste alle offenen Punkte aus diesem Chat.
```

Hier ist eine **kurze, präzise und methodisch saubere Zusammenfassung + ein kompaktes Fazit**, passend zum Stil der bestehenden Dokumentation:

# **Zusammenfassung**

Die *Prompt Library* bündelt alle zentralen Steuerprompts der Methodik in einem einzigen, klar strukturierten Referenzdokument. Sie deckt Start-Prompts, Drift-Korrekturen, Persistenz-Mechanismen, Rollenaktivierungen und Handover-Formate vollständig ab und stellt damit eine stabile Grundlage für jeden Arbeitsschritt im Mikroprozess dar.

Durch die klare Kategorisierung und konsequente Verwendung von Code-Blöcken ermöglicht die Prompt Library eine schnelle, fehlerfreie und driftresistente Interaktion mit dem LLM. Sie stellt damit sicher, dass die Zusammenarbeit über viele Iterationen hinweg konsistent bleibt und methodisch an die definierten Strukturen anknüpft.

# **Fazit**

Die Prompt Library ist ein essenzielles Werkzeug der Methodik. Sie schafft Klarheit, Wiederholbarkeit und hohe Stabilität im Umgang mit dem LLM und reduziert typische Fehlerquellen wie Drift, Rollenvermischung oder unklare Aufgabenformulierung.

Mit ihr steht ein kompakter, belastbarer und sofort einsetzbarer Prompt-Baukasten zur Verfügung, der den gesamten Arbeitsfluss unterstützt und die Qualität der Ergebnisse nachhaltig verbessert.

# Weiterführende Dokumente

-- Drift-Management\
-- Persistenzmechanismen\
-- Mikroprozess\
-- Rollenmodell
