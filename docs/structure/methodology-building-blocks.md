# Methodology Building Blocks

Dieses Dokument beschreibt die zentralen Bausteine der Methodologie für strukturierte, komplexe Zusammenarbeit mit einem LLM.  
Jeder Baustein ist ein eigenständiges Element, besitzt klaren Zweck, definierte Inhalte, Schnittstellen, typische Artefakte und Verantwortlichkeiten.

---

# 1. Steuerlogik (Projektanweisung)

## Zweck
Schafft einen stabilen methodischen Rahmen für die gesamte LLM-Zusammenarbeit.

## Inhalte
- Rollenmodell
- Format- und Strukturvorgaben
- Arbeitsregeln (iterativ, präzise, keine Ausschweifungen)
- Regeln für Konsistenz und Rückfragen

## Schnittstellen
- Mikroprozesse (Anwendung)
- Drift-Management (Stabilität)
- Persistenz (Einbettung in Gesamtstruktur)

## Typische Artefakte
- Projektanweisung
- Rollenbeschreibung

## Verantwortlichkeit
- **Nutzer:** Definition & Pflege  
- **LLM:** Einhaltung & Anwendung

---

# 2. Externe Wissensbasis (Repository)

## Zweck
Dient als versionierte, langfristige Wissensbasis und zentrale Dokumentationsquelle.

## Inhalte
- Ordnerstruktur (`docs/`)
- Informationsarchitektur
- Markdown-Dokumente, Modelle, Prozesse

## Schnittstellen
- Persistenz-Mechanismen (Überführung)
- Makroprozesse (Phasendokumente)
- Drift-Management (Vermeidung von Wissensverlust)

## Typische Artefakte
- Gesamtes `docs/`-Verzeichnis
- Inhaltsverzeichnis (`docs/README.md`)

## Verantwortlichkeit
- **Nutzer:** Pflege & Aktualisierung  
- **LLM:** Nutzung als Referenz

---

# 3. Makroprozesse

## Zweck
Beschreiben den übergeordneten Ablauf in 6–8 klar definierten Phasen.

## Inhalte
- Phasenmodell (1–8)
- Ziele, Inputs, Outputs je Phase
- Rollen & Übergaben

## Schnittstellen
- Mikroprozesse (operative Ausgestaltung)
- Persistenz (Überführung der Ergebnisse)
- Übergaben & Abschlussformate

## Typische Artefakte
- `process-macro.md`
- Phase-Tabellen & Diagramme

## Verantwortlichkeit
- **Nutzer & LLM gemeinsam:** Erarbeitung & Anwendung

---

# 4. Mikroprozesse

## Zweck
Definieren die feingliedrige Ablaufsteuerung einzelner Chats oder Chat-Segmente.

## Inhalte
- Schrittfolgen (Analyse → Klarifikation → Erzeugung → Review)
- Rolleninteraktion im Chat
- Regeln für iterative Verbesserung

## Schnittstellen
- Makroprozesse (Einbettung)
- Chat-Design (konkrete Umsetzung im Prompting)

## Typische Artefakte
- `process-micro-chat.md`
- Mikroablaufdiagramme

## Verantwortlichkeit
- **Nutzer:** Steuerung  
- **LLM:** strukturierte Ausführung

---

# 5. Chat-Design

## Zweck
Strukturiert einzelne Chat-Nachrichten, Prompts und Sequenzen.

## Inhalte
- Aufbau eines klaren Prompts
- Rollenansprache
- Sequenzlogik
- Input-/Output-Formate

## Schnittstellen
- Mikroprozesse
- Drift-Management

## Typische Artefakte
- Prompt-Templates
- Designprinzipien

## Verantwortlichkeit
- **Nutzer:** Formulierung  
- **LLM:** Interpretation

---

# 6. Begriffs- und Strukturmanagement

## Zweck
Sorgt für einheitliche Sprache, konsistente Definitionen und klare Strukturachsen.

## Inhalte
- Glossar
- Begriffssystem
- Strukturkategorien (Prozesse, Rollen, Artefakte)

## Schnittstellen
- Makroprozesse
- Mikroprozesse
- Drift-Management (Prüfpunkt)

## Typische Artefakte
- glossary.md
- Strukturübersichten

## Verantwortlichkeit
- **Nutzer:** Definition & Pflege  
- **LLM:** Nutzung

---

# 7. Drift-Management

## Zweck
Verhindert schleichende Kontextverschiebung und logische Abweichungen.

## Inhalte
- Kontrollmechanismen
- Drift-Indikatoren
- Prüfpunkte während der Mikroprozesse

## Schnittstellen
- Chat-Design
- Persistenz
- Begriffsmanagement

## Typische Artefakte
- Drift-Checklisten
- Prüfprotokolle

## Verantwortlichkeit
- **LLM:** Meldet Drift  
- **Nutzer:** Validiert & korrigiert

---

# 8. Persistenz-Mechanismen

## Zweck
Überführen der relevanten Chat-Ergebnisse in das Repository, versionssicher.

## Inhalte
- Übertragungsregeln
- Naming-Conventions
- Dokumentation im richtigen Ordner

## Schnittstellen
- Repository
- Makroprozesse (v. a. Phase 4–6)
- Abschlussformate

## Typische Artefakte
- Commits
- Releases
- Markdown-Dokumente

## Verantwortlichkeit
- **Nutzer:** Umsetzung  
- **LLM:** Vorstrukturierung der Inhalte

---

# 9. Rollen des LLM

## Zweck
Festlegen, wie das LLM agiert und welche methodischen Funktionen es übernimmt.

## Inhalte
- Methodiker
- Reviewer
- Strukturgeber
- Schreibassistent

## Schnittstellen
- Mikroprozesse
- Chat-Design

## Typische Artefakte
- Rollendefinitionen
- Einsatzhinweise in der Projektanweisung

## Verantwortlichkeit
- **LLM:** Nutzung der Rollen  
- **Nutzer:** Aktivierung & Kontextgebung

---

# 10. Übergaben & Abschlussformate

## Zweck
Sichert konsistente, nachvollziehbare Zwischen- und Endstände im gesamten Prozess.

## Inhalte
- Übergabedefinitionen (Input/Output)
- Abschlussformate (Dokumentation, Review)
- Kriterien für „fertig“

## Schnittstellen
- Makroprozesse
- Persistenz
- Repository

## Typische Artefakte
- Übergabedokumente
- Abschlussberichte
- Issue-Abschlüsse

## Verantwortlichkeit
- **Nutzer:** Finalisierung  
- **LLM:** Strukturierung & Unterstützung

---

# Gesamtzusammenhang
Alle Bausteine wirken zusammen und bilden ein kohärentes System:  
- **Steuerlogik** legt Verhalten fest  
- **Repository** speichert Wissen  
- **Makro- & Mikroprozesse** steuern Ablauf  
- **Chat-Design** strukturiert Interaktion  
- **Begriffsmanagement** sorgt für Konsistenz  
- **Drift-Management** schützt Stabilität  
- **Persistenz** macht Ergebnisse dauerhaft nutzbar  
- **Rollen** operationalisieren das Modell  
- **Übergaben** sichern Qualität

Dieses System bildet die Grundlage für reproduzierbare, klare, belastbare LLM-Zusammenarbeit.

