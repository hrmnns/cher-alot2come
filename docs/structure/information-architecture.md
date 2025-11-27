# Informationsarchitektur des Dokumentationssystems
**Version:** v0.2  
**Status:** überarbeitet  
**Geltungsbereich:** Methoden-Repository *cher-alot2come*  
**Verantwortung:** Dokumentationsverantwortlicher · LLM-Methodiker

## 1. Zweck dieses Dokuments
Die Informationsarchitektur definiert die Struktur, Ablageorte und Navigationsregeln für alle Dokumente des Projekts *cher-alot2come*.  
Sie bildet die methodische Grundlage für eine **konsistente, versionierte und skalierbare Wissensbasis**, die über alle Phasen des Makro- und Mikroprozesses hinweg stabil bleibt.

Die IA ist ein zentraler Baustein der **Persistenzmechanismen (Makroprozess Phase 5)** und stellt sicher, dass:

- alle Inhalte wiederauffindbar und nachvollziehbar abgelegt sind  
- thematisch verwandte Dokumente logisch gruppiert sind  
- Redundanzen, Widersprüche und Drift vermieden werden  
- Nutzer:innen (Mensch + LLM) zielgerichtet navigieren können  
- Skalierung des Wissensraums auch bei vielen Dateien gewährleistet ist  

## 2. Rolle der Informationsarchitektur in der Methodik

Die Informationsarchitektur ist nicht nur eine Ordnerstruktur — sie ist ein methodischer Kontrollmechanismus, der eng mit den Prozessen der Methodik verknüpft ist.

### Makroprozess-Bezug
| Phase | Bedeutung der IA |
|-------|-------------------|
| **Phase 1 – Vorbereitung** | Grundstruktur anlegen, erste Zuordnung der Dokumenttypen |
| **Phase 2 – Problemrahmen** | Strukturachsen definieren, Begriffe stabilisieren |
| **Phase 3 – Operative Bearbeitung** | Arbeitsdokumente korrekt einsortieren |
| **Phase 4 – Konsolidierung** | Inhalte harmonisieren, redundante Dateien identifizieren |
| **Phase 5 – Persistenz** | finale Versionierung & Ablage gemäß IA |
| **Phase 6 – Abschluss** | IA-Stand prüfen, Backlinks aktualisieren |

### Mikroprozess-Bezug
- **Phase A (Start):** Relevante Artefakte werden über IA gezielt benannt.  
- **Phase C (Ergebnissicherung):** Ergebnisblöcke werden anhand der IA zugeordnet.  
- **Phase D (Persistenz):** Speicherung erfolgt *ausschließlich* entlang der IA.  
- **Phase E (Abschluss):** Referenzen, Backlinks, Ordnerzuordnung aktualisieren.

### Parallel-Chat-Modell
- **Meta-Chat:** Pflege, Anpassung, Strukturentscheidungen  
- **Projekt-Chat:** reine Nutzung der bestehenden Struktur, keine Änderungen  

Dadurch bleibt die Dokumentation auch über viele Arbeitszyklen driftfrei.

## 3. Grundprinzipien der Informationsarchitektur

Die IA folgt fünf stabilen Leitprinzipien:

1. **Funktionale Ordnung**  
2. **Eindeutige Zuständigkeiten**  
3. **Skalierbarkeit**  
4. **Versionierbarkeit**  
5. **Navigierbarkeit**

## 4. Ordnerstruktur des `docs/`-Verzeichnisses

```
docs/
│
├── foundations/
│   └── methodology-foundations.md
│
├── processes/
│   ├── process-macro.md
│   ├── process-micro-chat.md
│   ├── handover-and-closure.md
│   └── parallel-chat-coordination.md
│
├── structure/
│   ├── methodology-building-blocks.md
│   ├── roles-llm.md
│   ├── document-types-and-storage.md
│   └── information-architecture.md
│
├── quality/
│   ├── persistence-mechanisms.md
│   ├── drift-management.md
│
├── library/
│   ├── prompt-library.md
│   └── start-prompt-generator.md
│
└── meta/
    ├── decision-log-method.md
    └── changelog.md
```

### Erläuterung der Kategorien
*(gekürzt für Klarheit in der Datei)*

## 5. Zentrales Inhaltsverzeichnis (`docs/README.md`)
Beschreibt Übersicht, Statusanzeigen, Navigationslogik und Pflegehinweise.

## 6. Backlink-System
Jedes Dokument endet mit:

```
**Weiterführende Dokumente:**
- …
```

Regeln:
- mind. 3 Backlinks  
- sinnvolle Querverweise  
- Aktualisierung bei Dokumentänderungen  

## 7. Dokumenttypen & Verantwortlichkeiten

| Rolle | Verantwortungsbereich |
|-------|------------------------|
| LLM-Methodiker | Strukturentscheidungen |
| Dokumentationsverantwortlicher | Ablage, Versionierung |
| Reviewer | Konsistenzprüfung, Driftkontrolle |
| Prompt-Autor | Zuweisung im Mikroprozess |
| Projekt-Chat | nutzt Struktur, verändert sie nicht |

## 8. Pflege & Weiterentwicklung

Regeln:
- neue Dateien → Kategorie + README + Backlinks + Versionsheader  
- Änderungen → Mini-Issue + Commit  
- größere Anpassungen → strukturierte Konsolidierung (Makroprozess Phase 4+5)

## 9. Ausblick
Automatisierung, Wiki-Integration, Link-Generatoren, weitere Bibliotheken.

## Weiterführende Dokumente
- process-macro.md  
- persistence-mechanisms.md  
- drift-management.md  
- document-types-and-storage.md  
- methodology-building-blocks.md
