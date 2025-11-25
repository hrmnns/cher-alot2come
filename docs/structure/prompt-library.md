# Prompt Library

Die Prompt Library bündelt alle wiederkehrenden, getesteten und stabilen Prompts im ALOT2COME-Framework. Sie dient als Werkzeugkasten für die operative Zusammenarbeit mit dem LLM über alle Phasen des Makro- und Mikroprozesses hinweg.

Ziel der Sammlung ist es:

- robuste und driftresistente Prompts jederzeit verfügbar zu machen
- Rollen sauber und konsistent zu aktivieren
- Startpunkte für neue Chats klar zu definieren
- Übergaben, Persistenzschritte und Korrekturmechanismen zu standardisieren
- eine einheitliche Interaktion über viele Iterationen sicherzustellen

Die Prompt Library ist ein struktureller Baustein der Methodik und erleichtert sowohl die Arbeit des Nutzers als auch die Stabilität des LLM durch präzise Steuerimpulse. Alle Prompts sind kategorisiert, methodisch begründet und kompatibel mit Drift-Management, Persistenzmechanismen und Rollenmodell.

# Inhaltsverzeichnis

- [1. Start-Prompts](#Start-Prompts)
- [2. Drift-Korrektur-Prompts](#2-drift-korrektur-prompts)
- [3. Persistenz-Prompts](#3-persistenz-prompts)
- [4. Rollenaktivierungs-Prompts](#Rollenaktivierungs-Prompts)
- [5. Handover-Prompts](#5-handover-prompts)
- [6. Mini-Checks](#6-mini-checks)
- [7. Quick-Prompts](#7-quick-prompts)
- [8. Arbeitssteuerungs-Prompts](#8-arbeitssteuerungs-prompts)
- [Zusammenfassung](#zusammenfassung)
- [Fazit](#fazit)

<a name="Start-Prompts"></a>
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

**Zweck:** Stoppt semantische Drift.  
**Wirkung:** Rückführung auf Glossardefinition.  
**Risiken:** Verwässerte Terminologie.  
**Prozessbezug:** Drift-Korrektur.  

``` md
Wir haben eine Begriffsdrift: Der definierte Begriff ist "<Begriff>".
Bitte korrigiere alle abweichenden Stellen.
```

Zweck: Korrigiert sofortige Abweichungen von persistierten Strukturen.  
Wirkung: LLM richtet Aufbau und Struktur exakt an gespeicherten Dokumenten aus.  
Risiken: Strukturinkonsistenz, verschobene Kapitel, Fehler beim Persistieren.  
Prozessbezug: Drift-Management, Mikroprozess D.  

``` md
Bitte stelle die Struktur gemäß Repository-Version wieder her (Datei: <Pfad>).
```

### 2.2 Kontextrekalibrierung

Zweck: Reinitialisiert Steuerlogik und Terminologie.  
Wirkung: LLM setzt Rollen, Regeln und Begriffe neu und stabil.  
Risiken: Rollenfehler, Terminologiedrift, unklare Formatlogik.  
Prozessbezug: Drift-Reset, Mikroprozess A/D.  

``` md
Bitte lade die Projektanweisung neu und bestätige die gültigen Begriffe aus dem Glossar.
```

Zweck: Stellt korrekte Prozessphasen wieder her.   
Wirkung: LLM synchronisiert mit offizieller Makroprozess-Definition.  
Risiken: Falsche Prozesslogik, inkorrekte Übergänge.  
Prozessbezug: Drift-Management, Makroprozess-Validierung.  

``` md
Wir haben eine leichte Strukturdrift. Bitte stelle die Phasennummerierung gemäß Makroprozess wieder her.
```

### 2.3 Vergleich mit Repository

Zweck: Identifiziert alle Unterschiede gegenüber der persistierten Version.  
Wirkung: LLM listet Driftstellen strukturiert auf.  
Risiken: Unentdeckte Abweichungen gelangen in Folgearbeit.  
Prozessbezug: Konsolidierung (Phase 4).  

``` md
Vergleiche deine letzte Antwort mit der Version aus <Dokument>.
Liste alle Abweichungen auf.
```

Zweck: Erzwingt eine driftfreie Neufassung gemäß Repository.  
Wirkung: LLM baut Text streng entlang der gespeicherten Struktur neu auf. 
Risiken: Vermischung alter und neuer Versionen.  
Prozessbezug: Drift-Reparatur, Phase 4.  

``` md
Bitte formuliere den Abschnitt neu, strikt entlang der persistierten Struktur aus <Dokument>.
```

### 2.4 Reparatur-Workflow

Zweck: Sichtbarmachen aller Driftstellen.  
Wirkung: LLM markiert strukturiert alle Abweichungen.  
Risiken: Übersehene Drift, unvollständige Reparatur.  
Prozessbezug: Drift-Detektion, Mikroprozess D.  

``` md
Bitte markiere alle Passagen, die von der persistierten Version abweichen.
```

Zweck: Qualitätssicherung nach Driftkorrektur.  
Wirkung: Reviewer prüft Logik, Terminologie und Struktur.  
Risiken: verbleibende Inkonsistenzen, fehlerhafte Persistenz.  
Prozessbezug: Konsolidierung (Phase 4), Mikroprozess D.  

``` md
Aktiviere Reviewer.
Prüfe die Überarbeitung auf Konsistenz und Driftfreiheit.
```

# 3. Persistenz-Prompts

### 3.1 Repository-Übergabe vorbereiten

Zweck: Erzeugt persistierbaren Endblock.  
Wirkung: LLM trennt finalen Inhalt klar vom Chat-Kontext.  
Risiken: Vermischung mit Chattext, falsche Persistenz.  
Prozessbezug: Mikroprozess E / Phase 5.  

``` md
Bitte liefere den Ergebnisblock als sauberen, getrennten Block.
Ohne Meta-Text.
Status: "final für Repository".
```

### 3.2 Persistenz-Check

Zweck: Qualitätssicherung vor Persistenz.  
Wirkung: LLM validiert Struktur, Terminologie und Versionsbezug.  
Risiken: fehlerhafte Inhalte gelangen ins Repo.  
Prozessbezug: Phase 5.  

``` md
Bitte prüfe dieses Ergebnis gegen bestehende Dokumente auf:
– Begriffe
– Struktur
– Konsistenz
– Versionen.
```

### 3.3 Auswahl der Zielorte

Zweck: Finden des korrekten Ablageorts.  
Wirkung: LLM prüft Repository-Ordnung & Strukturachsen.  
Risiken: falsche Ablage, spätere Inkonsistenz.  
Prozessbezug: Persistenzphase.  

``` md
Welcher Abschnitt und welche Datei sind gemäß Informationsarchitektur korrekt für dieses Ergebnis?
```

### 3.4 Übergabeformat

Zweck: Formatkonformität herstellen.  
Wirkung: LLM erstellt Markdown-kompatible finale Fassung.  
Risiken: Formatfehler, persistenzuntaugliche Inhalte.  
Prozessbezug: Phase 5.  

``` md
Bitte gib eine Repository-fertige Fassung des Ergebnisblocks gemäß Formatregeln aus.
```

<a name="Rollenaktivierungs-Prompts"></a>
# 4. Rollenaktivierungs-Prompts

### 4.1 LLM-Methodiker

Zweck: Aktiviert methodische Kontrollrolle.  
Wirkung: LLM prüft Prozesslogik, Struktur und Zielausrichtung.  
Risiken: unklare Arbeitsweise, fehlende Struktur.  
Prozessbezug: Phase A–D.  

``` md
Bitte agiere als LLM-Methodiker.
Prüfe Struktur, Vorgehen, Konsistenz und Zielklarheit dieses Abschnitts.
```

### 4.2 Strukturgeber

Zweck: Struktur erzeugen ohne Inhalte.  
Wirkung: LLM liefert reine Gliederung/Modelle.  
Risiken: unstrukturierte Ergebnisse.  
Prozessbezug: Phase B–D.  

``` md
Bitte agiere als Strukturgeber.
Erstelle eine präzise Gliederung für <Thema>. Kein Fließtext.
```

### 4.3 Reviewer

Zweck: Qualität prüfen ohne Inhaltserweiterung.  
Wirkung: LLM bewertet neutral Logik & Struktur.  
Risiken: Rollenvermischung, inhaltliche Eingriffe.  
Prozessbezug: Mikroprozess D.  

``` md
Bitte agiere als Reviewer.
Prüfe diesen Text ausschließlich auf:
– Logik
– Konsistenz
– Terminologie
– Struktur (ohne neue Inhalte).
```

### 4.4 Prompt-Engineer

Zweck: Verbesserung von Promptstabilität.  
Wirkung: LLM erkennt Ambiguitäten und behebt sie.  
Risiken: driftanfällige Prompts.  
Prozessbezug: Mikroprozess A–C.  

``` md
Bitte agiere als Prompt-Engineer.
Optimiere diesen Prompt für Ambiguitätsresistenz und Rollenstabilität.
```

### 4.5 Domänenexperte

Zweck: Fachliche Präzision.  
Wirkung: LLM liefert korrekte Inhalte & Beispiele.  
Risiken: fachliche Ungenauigkeit.  
Prozessbezug: Phase B–C.  

``` md
Bitte agiere als Domänenexperte für <Domäne>.
Erkläre <Begriff> und gib ein kurzes Beispiel.
```

# 5. Handover-Prompts

### 5.1 Übergabe an neuen Chat

Zweck: Übergabe an nächste Arbeitseinheit.  
Wirkung: Sicherer, vollständiger Kontexttransfer.  
Risiken: Kontextverlust, Fehlinterpretation.  
Prozessbezug: Phase 6 / Mikroprozess E.  

``` md
Bitte erstelle einen Handover-Block mit:
– Kontext
– bisherigen Ergebnissen
– offenen Punkten
– nächstem Schritt.
```

### 5.2 Übergabe an Issue

Zweck: Überführung eines Arbeitspakets in Issue-Form.  
Wirkung: LLM erzeugt strukturierte Issue-Vorlage.  
Risiken: unvollständige Issues.  
Prozessbezug: Phase 6.  

``` md
Bitte erstelle einen Handover-Block für ein neues Issue:
– Thema
– Aktueller Stand
– Offenes
– Benötigte Rolle
– Betroffene Dateien.
```

### 5.3 Übergabe zur Persistenz

Zweck: Vollständige Persistenzvorbereitung.  
Wirkung: LLM bündelt alles Relevante für das Repo.  
Risiken: Fehlende Inhalte, falsche Ablage.  
Prozessbezug: Phase 5–6.  

``` md
Bitte erstelle den Handover-Block zur Persistenz:
– Inhalte zur Übertragung
– Quelle
– Zielort
– Hinweise / Versionierung.
```

### 5.4 Abschluss eines Chats

Zweck: Sauberer Chat-Abschluss.  
Wirkung: LLM liefert vollständige Abschlussübersicht.  
Risiken: offene Enden, Kontextverlust.  
Prozessbezug: Mikroprozess E.  

``` md
Bitte stelle einen Abschlussblock bereit:
– Zusammenfassung
– Offene Punkte
– Repository-Übergaben
– Nächste Schritte.
```

# 6. Mini-Checks

### 6.1 Drift-Check

Zweck: Führt einen Mini-Drift-Check durch, um die Arbeitseinheit stabil auszurichten.
Wirkung: LLM synchronisiert Begriffe, Struktur und aktuelles Ziel mit dem Repository-Stand.
Risiken: Unbemerkte Begriffs-, Struktur- oder Fokusdrift innerhalb des Chats.
Prozessbezug: Mikroprozess Phase A (Initialisierung) und Phase D (Review).

``` md
Bitte bestätige Terminologie, Struktur und Zielrahmen dieser Arbeitseinheit.
```

### 6.2 Rollen-Check

**Zweck:** Rollenklarheit.  
**Wirkung:** Modell arbeitet bewusst im richtigen Modus.  
**Risiken:** Rollenvermischung.  
**Prozessbezug:** Mikroprozess A.  

``` md
In welcher Rolle arbeitest du gerade?
```

### 6.3 Struktur-Check

**Zweck:** Sicherstellt korrekte Begriffe und Struktur.  
**Wirkung:** Synchronisation mit Repo.  
**Risiken:** Begriffs- und Strukturdrift.  
**Prozessbezug:** Drift-Check.  

``` md
Bitte gib die gültige Prozess- oder Dokumentstruktur aus <Dokument> wieder.
```

# 7. Quick-Prompts

Zweck: Stoppt thematische Abdrift.  
Wirkung: LLM richtet Antwort wieder an aktuelle Aufgabe aus.  
Risiken: Themenverwässerung, Kontextsprünge.  
Prozessbezug: Mikroprozess B–D.  

``` md
Bitte zurück zum Fokus.
```

Zweck: Reaktivierung des expliziten Arbeitsziels.  
Wirkung: LLM stellt Orientierung neu her.  
Risiken: unklare Zielausrichtung.  
Prozessbezug: Mikroprozess A.  

``` md
Bitte bestätige den aktuellen Zielrahmen.
```

Zweck: Strukturvergleich ermöglichen.  
Wirkung: LLM liefert divergente Strukturansätze.  
Risiken: unstrukturierter Variantenmix ohne klare Vorgabe.  
Prozessbezug: Mikroprozess B.  

``` md
Bitte gib drei Strukturvarianten.
```

Zweck: Markierung eines stabilen Zwischenstands.  
Wirkung: LLM liefert klaren, sauber benannten Ergebnisblock.  
Risiken: fehlende Ergebnissicherung.  
Prozessbezug: Mikroprozess C/E.  

``` md
Bitte gib eine stabile Version als Ergebnisblock.
```

Zweck: Erfasst alle noch ungelösten Aufgaben und Fragen.  
Wirkung: LLM extrahiert und strukturiert offene Punkte aus dem gesamten Chatverlauf.  
Risiken: Aufgaben oder Klärpunkte gehen im Verlauf verloren; Anschlussfehler im nächsten Chat.  
Prozessbezug: Mikroprozess Phase E (Abschluss), Makroprozess Phase 6 (Übergabe).  

``` md
Bitte liste alle offenen Punkte aus diesem Chat.
```

# 8. Arbeitssteuerungs-Prompts

Diese Kategorie ergänzt alle Promptarten, die im Mikroprozess und Drift-Management vorgesehen sind, aber bisher nicht in der Prompt-Library enthalten waren.

## 8.1 Zielpräzisierung

### 8.1.1 Prompt: Ziel wiederholen

**Zweck:** Sicherstellung korrekter Zielinterpretation.\
**Wirkung:** Das LLM formuliert das Ziel in eigenen Worten.\
**Risiken:** Fehlinterpretation des Arbeitsziels.\
**Prozessbezug:** Mikroprozess Phase A.

``` md
Bitte wiederhole das Ziel dieser Arbeitseinheit in deinen eigenen Worten.
```

### 8.1.2 Prompt: Zielpräzisierung

**Zweck:** Verfeinert das Arbeitsziel.\
**Wirkung:** Das LLM erzeugt eine präzisierte Zieldefinition.\
**Risiken:** unscharfe Aufgabenstellung.\
**Prozessbezug:** Mikroprozess Phase A.

``` md
Bitte gib eine präzisierte Version der Zieldefinition aus.
```

## 8.2 Kontextpräzisierung

### 8.2.1 Prompt: Kontext kurz zusammenfassen

**Zweck:** Aktiviert den relevanten Kontext für die Arbeitseinheit.\
**Wirkung:** Das LLM fasst Kontext knapp und korrekt zusammen.\
**Risiken:** Kontextdrift.\
**Prozessbezug:** Mikroprozess Phase A.

``` md
Bitte gib den relevanten Kontext dieser Arbeitseinheit in 3 Sätzen wieder.
```

### 8.2.2 Prompt: Kontext-Reset

**Zweck:** Setzt Arbeitskontext aktiv neu.\
**Wirkung:** LLM rekonstruiert Ziel und Begriffe aus Projektanweisung &
Glossar.\
**Risiken:** fortgeschriebene Kontextdrift.\
**Prozessbezug:** Drift-Management, Phase A/D.

``` md
Bitte aktualisiere deinen Kontext: Ziel ist <Ziel>.
Formuliere in 2–3 Sätzen, wie du dieses Ziel auf Basis der Projektanweisung und des Glossars interpretierst.
```

## 8.3 Iterationssteuerung

### 8.3.1 Prompt: Überarbeitung entlang Feedback

**Zweck:** Steuert gezielte Iteration.\
**Wirkung:** LLM arbeitet Feedback präzise ein.\
**Risiken:** zu breite Überarbeitungen.\
**Prozessbezug:** Mikroprozess Phase C/D.

``` md
Bitte überarbeite die letzte Version entlang der folgenden Punkte: <Liste>.
```

### 8.3.2 Prompt: Variante präzisieren

**Zweck:** Verfeinert eine Variante.\
**Wirkung:** LLM erzeugt präzisere Nachfolgeversion.\
**Risiken:** Varianten vermischen sich.\
**Prozessbezug:** Mikroprozess Phase C.

``` md
Bitte verfeinere Variante <Nummer> entlang der zentralen Argumentationslinie.
```

## 8.4 Variantenvergleich

### 8.4.1 Prompt: Unterschiede markieren

**Zweck:** Identifiziert Unterschiede zwischen Varianten.\
**Wirkung:** LLM vergleicht strukturiert.\
**Risiken:** fehlende Trennschärfe.\
**Prozessbezug:** Mikroprozess Phase C/D.

``` md
Bitte markiere die Unterschiede zwischen Variante <A> und Variante <B>.
```

### 8.4.2 Prompt: Vergleichende Bewertung

**Zweck:** Bewertet Varianten anhand Kriterien.\
**Wirkung:** LLM erstellt vergleichende Analyse.\
**Risiken:** unklare Entscheidungsgrundlagen.\
**Prozessbezug:** Mikroprozess Phase D.

``` md
Bitte vergleiche Variante <A> und <B> anhand der folgenden Kriterien: <Liste>.
```

## 8.5 Fokusgrenzen

### 8.5.1 Prompt: Fokus auf Struktur

**Zweck:** Einschränkung auf Strukturebene.\
**Wirkung:** Modell arbeitet ohne Fließtext.\
**Risiken:** Vermischung von Struktur & Inhalt.\
**Prozessbezug:** Mikroprozess Phase B/D.

``` md
Bitte bleibe ausschließlich auf Strukturebene und formuliere nicht im Fließtext.
```

### 8.5.2 Prompt: Fokus auf Abschnitt

**Zweck:** Begrenzung des Arbeitsbereichs.\
**Wirkung:** LLM fokussiert auf definierten Teilbereich.\
**Risiken:** zu breiter Scope.\
**Prozessbezug:** Mikroprozess Phase C/D.

``` md
Bitte konzentriere dich ausschließlich auf den Abschnitt <Name>.
```

## 8.6 Ergebnisbenennungen

### 8.6.1 Prompt: Zwischenergebnis benennen

**Zweck:** Eindeutige Benennung eines Ergebnisses.\
**Wirkung:** LLM markiert Ergebnis klar referenzierbar.\
**Risiken:** Verwechslungen späterer Iterationen.\
**Prozessbezug:** Mikroprozess Phase C/E.

``` md
Bitte benenne dieses Ergebnis als „<Name des Zwischenergebnisses> – stabil“.
```

### 8.6.2 Prompt: Finale Version benennen

**Zweck:** Kennzeichnet eine finale Fassung.\
**Wirkung:** LLM markiert stabilen Endstand.\
**Risiken:** Unklarheit über finale Version.\
**Prozessbezug:** Mikroprozess Phase E.

``` md
Bitte markiere diese Version als „Finale Fassung <Bezeichnung>“.
```


# **Zusammenfassung**

Die *Prompt Library* bündelt alle zentralen Steuerprompts der Methodik in einem einzigen, klar strukturierten Referenzdokument. Sie deckt Start-Prompts, Drift-Korrekturen, Persistenz-Mechanismen, Rollenaktivierungen und Handover-Formate vollständig ab und stellt damit eine stabile Grundlage für jeden Arbeitsschritt im Mikroprozess dar.

Durch die klare Kategorisierung und konsequente Verwendung von Code-Blöcken ermöglicht die Prompt Library eine schnelle, fehlerfreie und driftresistente Interaktion mit dem LLM. Sie stellt damit sicher, dass die Zusammenarbeit über viele Iterationen hinweg konsistent bleibt und methodisch an die definierten Strukturen anknüpft.

# **Fazit**

Die Prompt Library ist ein essenzielles Werkzeug der Methodik. Sie schafft Klarheit, Wiederholbarkeit und hohe Stabilität im Umgang mit dem LLM und reduziert typische Fehlerquellen wie Drift, Rollenvermischung oder unklare Aufgabenformulierung.

Mit ihr steht ein kompakter, belastbarer und sofort einsetzbarer Prompt-Baukasten zur Verfügung, der den gesamten Arbeitsfluss unterstützt und die Qualität der Ergebnisse nachhaltig verbessert.
