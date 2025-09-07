# Kreisrund-Übersetzung (Ez Chajim)

Die Kreisrund-Übersetzung (KÜ) ist ein neues Verfahren, um große hebräische Werke – wie **Ez Chajim** – nichtlinear zu erschließen.  
Sie macht Inhalte holografisch sichtbar: nicht als reine Textzeilen, sondern als **Mandala-Struktur** mit Zentrum, Ringen und Wellen.

---

## Grundprinzip

- **Zentrum** = Profil (Lesegewichte L0–L5)  
- **Ringe** = Übersetzungsspuren  
  - L0: wörtlich  
  - L1: Lesefluss  
  - L2: Terminologie  
  - L3: Kommentar  
  - L4: Morphologie  
  - L5: Didaktik  
- **Wellen** = Ereignisse im Lesetakt (Scroll, Blick, Ticks)  

Jedes Segment trägt eine **stabile ID** (`bk:ch:sec:para:sent`), hat **Reading-Ticks (start/end)**, Morphologie-Infos, Glossar-Verweise und Referenzen.

---

## CLI: `etz-compile`

Die Pipeline baut aus JSON-Segmenten (`data/ez-chajim/`) reproduzierbare Artefakte:

- **Input**:  
  - `--src data/ez-chajim/` (Segmentdateien im YAML/JSON-Schema)  
  - optional `--gloss data/glossary.yml` (Terminologie)  

- **Output**:  
  - `--out data/ez-chajim/ezchajim.vtt-r` (WebVTT-ähnlich mit `X-UNITS: ticks`)  
  - `--index data/ez-chajim/ezchajim.jsonl` (prüfbarer Index mit sha256)  

Das Glossar wird auf Spur L2 angewendet und auf Konsistenz geprüft.  
Alles läuft deterministisch und reproduzierbar.

---

## UI-Einbindung

- **Mandala-Viewer**: Segmente erscheinen als Nodes  
  - Radius = Nähe zum Profil  
  - Winkel θ = Hash der Referenz  
  - Puls = Lesetakt  
- **Overlay „Warum hier?“**: erklärt Profil-Gewichte vs. Segment-Score  
- **Events**: in `data/events.jsonl`, Frontend pollt alle 3s, erzeugt Wellen

---

## Nutzen

- Schnellere Orientierung in großen Texten  
- Weniger Terminologie-Drift  
- Räumlicher Kontext sichtbar  
- Adaptive Tiefe: L0 bis L5 parallel  
- Nachvollziehbare Übersetzungsschritte

---

## Hinweis

Die Kreisrund-Übersetzung ist Teil des größeren Projekts **KREISRUND**, das lineare Ströme verlustarm in eine holografische Kreisform faltet – und zurück.  
Ziel ist eine **holografische Informationsverarbeitung** für Forschung, Lehre und digitale Editionen.

---
