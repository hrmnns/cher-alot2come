# Methodology Building Blocks

Dieses Dokument beschreibt die zentralen Bausteine der Methodologie für strukturierte, komplexe Zusammenarbeit mit einem LLM.  
Jeder Baustein folgt einer einheitlichen Struktur: **Zweck – Inhalte – Schnittstellen – Artefakte – Verantwortlichkeit**.

# 1. Steuerlogik (Projektanweisung)

## Zweck
Definiert das stabile methodische Rahmenwerk der LLM-Zusammenarbeit und wirkt als „operatives Betriebssystem“ des Projekts.

## Inhalte
- Rollenmodell des LLM
- Formatregeln (Markdown, Struktur, Präzision)
- Arbeitsweise (iterativ, klärend, konsistent)
- Rückfrageprinzip und Entscheidungslogik
- Qualitätsprinzipien (Klarheit, Struktur, Anschlussfähigkeit)

## Schnittstellen
- **Mikroprozesse:** Anwendung der Regeln auf Chat-Ebene  
- **Drift-Management:** Steuerlogik als Referenzrahmen  
- **Persistenzmechanismen:** Definition der Überführungsregeln  

## Typische Artefakte
- Projektanweisung (ChatGPT-Projekt)
- Rollenbeschreibung
- Formatregelkatalog

## Verantwortlichkeit
- **Nutzer:** Definiert, pflegt und aktualisiert  
- **LLM:** Hält Vorgaben konsequent ein


# 2. Externe Wissensbasis (Repository)

## Zweck
Versionierte, langlebige Ablage aller Ergebnisse – Single Source of Truth für das gesamte Projekt.

## Inhalte
- Verzeichnisstruktur (`docs/`)
- Informationsarchitektur
- Markdown-Dokumente, Prozesse, Modelle, Glossare
- Roadmaps, Entscheidungen, Issues

## Schnittstellen
- **Persistenzmechanismen:** Überführung der Ergebnisse  
- **Makroprozesse:** Ablage je nach Phase  
- **Drift-Management:** Referenzpunkt gegen Kontextverlust  

## Typische Artefakte
- `docs/`-Verzeichnis
- Zentrales Inhaltsverzeichnis (`docs/README.md`)
- Begleitdokumentation (Foundations, Processes, Structure)

## Verantwortlichkeit
- **Nutzer:** Pflege, Commits, Versionierung  
- **LLM:** Nutzung als Wissensquelle


# 3. Makroprozesse

## Zweck
Beschreiben den übergeordneten Ablauf in 6–8 Phasen und geben Orientierung für langfristige Themenbearbeitung.

## Inhalte
- Phasen 1–8 (Vorbereitung → Monitoring)
- Ziel, Input, Output jeder Phase
- Rollen, Übergabepunkte, Entscheidungsschritte

## Schnittstellen
- **Mikroprozesse:** Taktung der operativen Arbeit  
- **Persistenz:** Überführung von Phase 4–6  
- **Übergaben:** Definition der formalen Schritte  

## Typische Artefakte
- `process-macro.md`
- Phasen-Tabellen
- Prozessdiagramme (PlantUML)

## Verantwortlichkeit
- **Nutzer:** Steuerung und Anwendung  
- **LLM:** Strukturierung und Ausarbeitung


# 4. Mikroprozesse

## Zweck
Feinsteuerung der operativen Zusammenarbeit in einzelnen Chats oder Chat-Segmenten.

## Inhalte
- Sequenzen: Analyse → Klärung → Erzeugung → Review
- Rolleninteraktion im Chat
- Regeln der Iteration und Rückkopplung

## Schnittstellen
- **Makroprozesse:** Mikroprozesse füllen die Makroprozesse operativ  
- **Chat-Design:** Gestaltung einzelner Prompts  
- **Drift-Management:** Kontrollpunkte pro Chat-Schritt  

## Typische Artefakte
- `process-micro-chat.md`
- Ablaufdiagramme
- Chat-Templates

## Verantwortlichkeit
- **Nutzer:** Moderation, Steuerung  
- **LLM:** Durchführung, Strukturierung


# 5. Chat-Design

## Zweck
Strukturiert die operative Interaktion zwischen Mensch und LLM auf Nachrichtenebene.

## Inhalte
- Prompt-Architektur
- Rollenansprache
- Sequenzlogik
- Outputformatierung
- Explizite Anforderungen (z. B. Tabellen, Gliederungen)

## Schnittstellen
- **Mikroprozesse** (operative Umsetzung)
- **Drift-Management** (klare Strukturen verhindern Drift)
- **Rollen des LLM** (gezielte Aktivierung)

## Typische Artefakte
- Prompt-Templates
- Chat-Design-Guides
- Beispielprompts

## Verantwortlichkeit
- **Nutzer:** Formuliert & steuert  
- **LLM:** Interpretiert & strukturiert


# 6. Begriffs- und Strukturmanagement

## Zweck
Sorgt für einheitliche, klare und konsistente Begriffe sowie stabile Strukturachsen im Projekt.

## Inhalte
- Glossar zentraler Begriffe
- Strukturachsen (Rollen, Prozesse, Artefakte)
- Benennungsregeln

## Schnittstellen
- **Makroprozesse:** Nutzung der Terminologie  
- **Mikroprozesse:** Einheitliche Sprache im Chat  
- **Drift-Management:** Abgleich gegen Begriffsabweichungen  

## Typische Artefakte
- `glossary.md`
- Strukturmodelle
- Definitionslisten

## Verantwortlichkeit
- **Nutzer:** Pflegt & entscheidet  
- **LLM:** Nutzt konsistent


# 7. Drift-Management

## Zweck
Verhindert Kontextverlust, Logikdrift und semantische Abweichungen über den Projektverlauf hinweg.

## Inhalte
- Drift-Indikatoren
- Kontrollpunkte in Mikroprozessen
- Wiederholungs- und Verankerungsmechanismen

## Schnittstellen
- **Chat-Design:** Klare Prompts reduzieren Drift  
- **Persistenzmechanismen:** Regelmäßige Überführung  
- **Begriffsmanagement:** Konsistenzprüfung  

## Typische Artefakte
- Drift-Checklisten
- Prüfprotokolle
- Standardisierte Reviewfragen

## Verantwortlichkeit
- **LLM:** Meldet Drift  
- **Nutzer:** Validiert, korrigiert, persistiert


# 8. Persistenz-Mechanismen

## Zweck
Überführen relevanter Erkenntnisse aus Chats in versionierte, stabile Dokumente.

## Inhalte
- Übertragungsregeln
- Commit-Logik
- Dokumentationsstandards
- Regelmäßige Konsolidierung

## Schnittstellen
- **Repository:** Zielpunkt der Persistenz  
- **Makroprozesse:** Phase 4–6  
- **Abschlussformate:** formaler Abschluss  

## Typische Artefakte
- Markdown-Dokumente
- Commit-Historie
- Releases

## Verantwortlichkeit
- **Nutzer:** Persistiert  
- **LLM:** Strukturiert Inhalte vor


# 9. Rollen des LLM

## Zweck
Operationalisieren typische Arbeitsweisen des Modells und ermöglichen gezielte methodische Nutzung.

## Inhalte
- LLM-Methodiker (Struktur)
- Prompt-Engineer (Formulierungslogik)
- Strukturgeber (Ordnung, Gliederung)
- Reviewer (Konsistenzprüfung)

## Schnittstellen
- **Mikroprozesse:** Rollen werden situativ aktiviert  
- **Chat-Design:** Rolleninformation fließt in Prompts  

## Typische Artefakte
- Rollensteckbriefe
- Aktivierungs-Prompts

## Verantwortlichkeit
- **Nutzer:** Aktiviert & steuert  
- **LLM:** Führt Rollen aus


# 10. Übergaben & Abschlussformate

## Zweck
Sichern eindeutig definierte Zwischen- und Endstände für Transparenz, Nachvollziehbarkeit und Anschlussfähigkeit.

## Inhalte
- Übergabedefinitionen (Input/Output)
- Abschlussdokumente
- Übergabe-Checklisten
- Freigabekriterien

## Schnittstellen
- **Makroprozesse:** formale Übergabepunkte  
- **Persistenzmechanismen:** finalisierte Dokumente  
- **Repository:** Zielpunkt aller Übergaben  

## Typische Artefakte
- Übergabedokumente  
- Abschlussberichte  
- Issue-Abschlüsse  

## Verantwortlichkeit
- **Nutzer:** finalisiert & dokumentiert  
- **LLM:** strukturiert & vorbereitet


# Gesamtzusammenhang

Die Bausteine bilden ein integriertes System:

- **Steuerlogik** gibt den methodischen Rahmen.  
- **Repository** hält das Wissen dauerhaft fest.  
- **Makroprozesse** definieren den Projektfluss.  
- **Mikroprozesse** steuern den Chat-Betrieb.  
- **Chat-Design** strukturiert die einzelnen Nachrichten.  
- **Begriffsmanagement** schafft gemeinsame Sprache.  
- **Drift-Management** sichert die Stabilität.  
- **Persistenz** macht Ergebnisse dauerhaft nutzbar.  
- **Rollen** operationalisieren das LLM.  
- **Übergaben** sichern klare Projektzustände.

Gemeinsam ermöglichen sie **eine präzise, konsistente, reproduzierbare und nachhaltige Zusammenarbeit mit einem LLM**.

