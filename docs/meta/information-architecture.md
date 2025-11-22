# Informationsarchitektur für das Dokumentationssystem

## Version
v0.1 – Erstfassung der Informationsarchitektur

## 1. Zweck dieses Dokuments

Dieses Dokument beschreibt die Informationsarchitektur für das `docs/`-Verzeichnis des Projekts *cher-alot2come*. Es legt fest, wie die Dokumentation strukturiert, gruppiert, versioniert und navigierbar gehalten wird, um auch bei wachsender Anzahl von Markdown-Dateien dauerhaft Übersicht und Konsistenz sicherzustellen.


## 2. Anforderungen an die Informationsarchitektur

Die Architektur muss sicherstellen, dass:

- thematisch verwandte Inhalte gemeinsam abgelegt sind  
- alle Dokumente leicht auffindbar sind  
- die Navigation innerhalb des Wissensraums klar und verlässlich ist  
- Redundanzen und Widersprüche vermieden werden  
- alle Inhalte Versionierung und Pflege ermöglichen  
- das System langfristig skalierbar bleibt  

Die Architektur dient damit als Grundlage für alle folgenden Dokumentationsarbeiten.

## 3. Struktur des `docs/`-Verzeichnisses

Die Dokumente werden nach funktionaler Zugehörigkeit gruppiert. Vorgeschlagene Ordnerstruktur:

```
docs/
│
├── foundations/
│   └── methodology-foundations.md
│
├── processes/
│   ├── process-macro.md
│   ├── process-micro-chat.md
│   └── handover-and-closure.md
│
├── structure/
│   ├── methodology-building-blocks.md
│   ├── roles-llm.md
│   └── document-types-and-storage.md
│
├── quality/
│   ├── persistence-mechanisms.md
│   └── drift-management.md
│
└── meta/
    └── decision-log-method.md
```

Diese Struktur ordnet Dateien sowohl thematisch als auch funktional.


## 4. Zentrales Inhaltsverzeichnis (`docs/README.md`)

Zur Übersicht über alle Dokumente wird eine zentrale Einstiegsseite gepflegt.  
Diese Datei enthält:

- eine thematisch gruppierte Übersicht aller Dokumente  
- direkte Links auf jedes Dokument  
- Statusanzeigen (✔ fertig, 🚧 in Arbeit, ⏳ geplant)  
- Regeln zur Aktualisierung der Struktur  
- Verweise auf verwandte Dokumente  

Beispielstruktur:

```md
# Dokumentationsübersicht

## Foundations
- [methodology-foundations.md](foundations/methodology-foundations.md) ✔

## Prozesse
- [process-macro.md](processes/process-macro.md) 🚧
- [process-micro-chat.md](processes/process-micro-chat.md) 🚧
- [handover-and-closure.md](processes/handover-and-closure.md) ⏳

## Struktur & Rollen
- [methodology-building-blocks.md](structure/methodology-building-blocks.md) ⏳
- [roles-llm.md](structure/roles-llm.md) ⏳
- [document-types-and-storage.md](structure/document-types-and-storage.md) ⏳

## Qualitätssicherung
- [persistence-mechanisms.md](quality/persistence-mechanisms.md) ⏳
- [drift-management.md](quality/drift-management.md) ⏳

## Meta
- [decision-log-method.md](meta/decision-log-method.md) ⏳
```

## 5. Backlink-System

Um Zusammenhänge deutlich zu machen, enthält jedes Dokument am Ende einen Abschnitt:

```
**Weiterführende Dokumente:**
- Drift Management
- Persistenzmechanismen
- Makroprozess
```

Dies schafft einen „Wiki-artigen“ Workflow und reduziert das Risiko, Inhalte zu verlieren oder zu isolieren.

## 6. Regeln für `docs/` vs. Wiki

### `docs/`  
- Arbeitsdokumente  
- iterativ  
- versioniert  
- detailreich  
- veränderlich  
- Grundlage der Methodikentwicklung  

### Wiki  
- stabile, belastbare Endfassung  
- Orientierung für Nutzer:innen  
- Zusammenfassungen, Übersichten, Leitfäden  
- keine Entwürfe oder Work-in-Progress  

Diese Abgrenzung verhindert, dass sich Arbeitsstand und Finaldokumentation vermischen.


## 7. Pflege & Weiterentwicklung

- Änderungen an der Struktur werden zunächst im `docs/README.md` erfasst.  
- Jedes neue Dokument muss:
  - in der passenden Kategorie abgelegt werden  
  - im Inhaltsverzeichnis verlinkt werden  
  - Backlinks enthalten  
- Größere Strukturänderungen müssen in einem eigenen Issue behandelt werden.

## 8. Ausblick

Diese Informationsarchitektur bildet die Grundlage für:

- die Erstellung der einzelnen Methodologie-Dokumente  
- spätere Automatisierung (z. B. Dokumentlinks generieren)  
- Integration in das Wiki  
- langfristige Skalierung des Projekts  

## Weiterführende Dokumente
– (werden im Verlauf ergänzt)

---

*Ende des Dokuments.*
