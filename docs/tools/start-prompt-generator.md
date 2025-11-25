# 📄 Start-Prompt-Generator (Markdown)

> **Zweck:**
> Dieses Template erzeugt einen vollständigen, driftresistenten, methodisch korrekten Start-Prompt für jede neue Arbeitseinheit (Mikroprozess Phase A).
>
> **Hinweis:**
> Alle Platzhalter mit `<…>` ausfüllen.


```md
# 🧩 Start-Prompt-Generator

Bitte agiere als LLM-Methodiker.
Wir starten eine neue Arbeitseinheit.

## 1) Kontext
<Kurzbeschreibung des Themas / Stands>
(Relevante Dokumente: <Dateien / Links>)

## 2) Ziel dieses Chats
<Klares, eng gefasstes Ziel der Einheit>

## 3) Rolle des LLM
<Rolle auswählen: Methodiker / Strukturgeber / Reviewer / Prompt-Engineer / Domänenexperte>

## 4) Arbeitsmodus
<Analysieren / Strukturieren / Ausarbeiten / Review / Konsolidieren>

## 5) Relevante Artefakte
<List of docs/issues aus Repository, z. B.>
– docs/processes/process-micro-chat.md
– docs/quality/drift-management.md

## 6) Fokusgrenzen
– Keine Änderung an persistierten Strukturen  
– Keine neue Terminologie  
– Klar auf die definierte Aufgabe begrenzen

## 7) Bitte bestätigen
Bitte bestätige:
– Rolle  
– Ziel  
– Arbeitsmodus  
– relevante Dokumente  
– dass keine Drift vorliegt
```

# ✔ Hinweise zur Nutzung

* **Jeder neue Chat** beginnt mit diesem Generator.
* Er verhindert **Begriffs-, Struktur- und Kontextdrift**, wie in *drift-management.md* definiert ().
* Er aktiviert **Rolle + Arbeitsmodus**, wie im *Rollenmodell des LLM* festgelegt ist ().
* Er etabliert klare **Fokusgrenzen**, damit der Chat nicht abgleitet.
* Der Prompt ist kompatibel mit den Regeln zu Persistenz und Übergaben aus *handover-and-closure.md* ().
