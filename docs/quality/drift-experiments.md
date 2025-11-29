# Experimente zum Nachweis von Begriffsdrift in LLMs

Ziel: Nachweisen, dass ein klar definierter Begriff (z. B. „Modul“) über längere Zeit trotzdem substituiert, erweitert, umdefiniert oder verwässert wird.

### **Regelprinzip: Drift entsteht oft erst, wenn mehrere Faktoren gleichzeitig auftreten:**

* leichte Ambiguität
* Kontextverschiebung
* Variation in der Fragestellung
* Überfrachtung
* „Optimierungsangebote“
* Analogien
* Befehle in widersprüchliche Richtungen

Dieses Protokoll bildet diese Faktoren systematisch ab.

## 🧭 **Vorbereitung**

Verwende einen sehr generischen Begriff, z. B.:

> **Unser Definitionsbegriff:**
> „Ein **Modul** ist ein klar abgegrenzter Bestandteil einer WebApp, bestehend aus Eingabefeldern und Logik. Bitte verwende *ausschließlich* das Wort ‚Modul‘ und keine Synonyme.“

Wichtig: nicht *zu hart* verbieten. Ein zu striktes Verbot bremst Drift.

## 🧩 **Phase 1: Stabilisierung (Prompts 1–4)**

Ziel: Modell soll eine klare Basis gewinnen (diese ist später wichtig, um Drift sichtbar zu machen).

**1. Prompt**
„Wir definieren den Begriff *Modul* wie folgt: … Bitte wiederhole die Definition in eigenen Worten.“

**2. Prompt**
„Welche Eigenschaften hat ein Modul?“

**3. Prompt**
„Wozu braucht man Module? Bitte kurz.“

**4. Prompt**
„Erstelle eine kleine Tabelle, die ein Modul von anderen Bausteinen unterscheidet.“

➡️ Die ersten vier Prompts verankern den Begriff.

## 🧩 **Phase 2: Leichte Störungen einführen (Prompts 5–10)**

Ziel: minimale Ambiguität erzeugen.

**5. Prompt**
„Ein Kollege spricht statt von Modulen von *Bausteinen*.
Erklär ihm bitte, warum wir *Modul* sagen.“

**6. Prompt**
„Kannst du ein Beispiel-Modul in 3 Sätzen beschreiben?“

**7. Prompt**
„Gibt es Fälle, in denen *Baustein* doch sinnvoll wäre? Bitte kurz.“

**8. Prompt**
„Formuliere den Begriff *Modul* so, dass auch ein Anfänger ihn versteht.“

**9. Prompt**
„Wie unterscheidet sich ein Modul von einem *Abschnitt*?“

**10. Prompt**
„Mach aus der Erklärung ein kleines Storytelling-Beispiel.“

➡️ Erste Drifttrends:
Viele Modelle benutzen in Prompt 10 unbemerkt „Abschnitt“ oder „Baustein“ in erzählerischen Formulierungen.
Wenn nicht → weiter.

## 🧩 **Phase 3: Diversifikation (Prompts 11–15)**

Ziel: Bedeutungsraum dehnen, ohne dass es offensichtlich ist.

**11. Prompt**
„Stell dir vor, wir benutzen das Wort Modul in einer anderen Domäne, z. B. im Projektmanagement.
Wie könnte der Begriff dort interpretiert werden?“

**12. Prompt**
„Könnte man das auch ‚Element‘ nennen? Warum ja/nein?“

**13. Prompt**
„Bitte führe eine Liste von 5 möglichen Missverständnissen, wenn man ‚Modul‘ falsch versteht.“

**14. Prompt**
„Erkläre Modul so, dass es sowohl für WebApps als auch für Workshops passt.“

**15. Prompt**
„Wie würde ein Designer ein Modul definieren?“

➡️ Ergebnis:
Viele Modelle beginnen spätestens hier Begriffe wie *Element*, *Komponente*, *Block*, *Section*, *Baustein* in ihren Antworten einzuweben, obwohl du das nie erlaubt hast.

Wenn noch nicht: weiter.

## 🧩 **Phase 4: Kontextwechsel erzwingen (Prompts 16–20)**

Ziel: Domainshift provoziert fast immer Drift.

**16. Prompt**
„Wir wechseln jetzt die Perspektive:
Stell dir eine *E-Commerce-App* vor. Welche Module gäbe es dort?“

**17. Prompt**
„Wie würde ein Product Owner das Modul-System beschreiben?“

**18. Prompt**
„Kann ein Modul auch als ‚Feature‘ verstanden werden? Bitte vergleiche.“

**19. Prompt**
„Walnimm jetzt an, wir dokumentieren das Modul als Teil eines Fachkonzepts.
Wie würde die Überschrift lauten?“

**20. Prompt**
„Bitte schreibe eine kurze Erklärung der Module im Kontext der E-Commerce-App.“

➡️ Erwartetes Verhalten:
Spätestens hier entstehen driftsichere Substitutionen:

* „Feature“
* „Komponente“
* „Bereich“
* „Abschnitt“
* „Funktionsteil“

Moderne Modelle versuchen semantisch „klüger“ zu antworten → **und entfernen sich vom Ausgangsbegriff**.

## 🧩 **Phase 5: Drift sichtbar machen (Prompts 21–25)**

Ziel: Das Modell entlarvt, dass es vom definierten Begriff abweicht.

**21. Prompt**
„Bitte erkläre nochmal in eigenen Worten, was ein Modul ist.“

**22. Prompt**
„Welche *Synonyme* hast du in unseren letzten Antworten für ‚Modul‘ verwendet?“

➡️ Viele Modelle erkennen hier nicht, dass sie Synonyme verwendet haben.

**23. Prompt**
„Bitte liste alle Begriffe auf, die du in den letzten 10 Antworten *statt* Modul verwendet hast.“

**24. Prompt**
„Habe ich dich gebeten, Synonyme zu verwenden?“

**25. Prompt**
„Bitte vergleiche deine aktuelle Definition mit der ursprünglichen Definition, die wir gemeinsam festgelegt haben.“

➡️ Das ist der Moment, in dem Drift klar sichtbar wird.

## 📌 **Warum funktioniert dieses Langzeitexperiment zuverlässig?**

Weil es die **natürlichen Ursachen von Drift simuliert**:

| Drift-Ursache       | Wie im Experiment provoziert |
| ------------------- | ---------------------------- |
| Kontextwechsel      | Phase 3 + 4                  |
| Analogien           | Phase 3                      |
| Ambiguität          | Phase 2                      |
| Synonym-Generierung | Phase 3                      |
| Rollenwechsel       | optional integrierbar        |
| Domain-Shift        | Phase 4                      |
| „Optimierung“       | Phase 2–3                    |
| lange Chatdauer     | gesamtes Experiment          |

**→ Genau dieselben Ursachen, die auch ALOT2COME adressiert.**
