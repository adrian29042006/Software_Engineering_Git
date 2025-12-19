# Sprint 2
---
### 1. Sprint Planning
Zu Beginn des 2. Sprint habe ich die relevanten Anforderungen (Requirements) ausgewählt. Konkret wurde die folgende Kernfunktion identifiziert und berücksichtigt:
- Barrierefreiheit
- Sicherheit während der Benutzung und drüber hinaus
- Zuverlässigkeit und Lebensdauer
- Funktionale Logik und Ablauf
- Bedienung und Ergonomie


---
Sprint Datum : 12.12.2025
---

Es wurden diese Requirements ergänzt:
- R1.4 Zuverlässige Funktion bei verschmutzten Fingern
- R1.5 Lebensdauer der LED-Anzeige ≥ 500 h
- R2.4 Taste „P“ muss sich in Form oder Farbe unterscheiden
- R2.5 Die Funktion muss 10 Minuten laufen und sich selbst deaktivieren
- R4.2 Schalter hält ≥ 100.000 Betätigungen ohne Defekt
- R5.3 Zeit wird heruntergezählt und Kochzone abschalten

Bei der Auswahl der Requirements wurde darauf geachtet, Nice-to-Have-Requirements nicht in diesem Sprint aufzunehmen (diese werden in Sprint 3 umgesetzt). Es wurden bestimmte Anforderungen ausgewählt, die für die grundlegende Funktion und sichere Bedienung des Produkts zwingend notwendig sind. Ziel war es, in diesem Sprint ausschließlich jene Kernanforderungen zu berücksichtigen, die den zuverlässigen und benutzerfreundlichen Betrieb sicherstellen.


Alle Requirements (Sprint 1 + 2):
- R1.1 9 klar unterscheidbare Leistungsstufen
- R1.2 Auswahl der Leistungsstufen über Touch, Drehknopf oder Tasten
- R1.4 Zuverlässige Funktion bei verschmutzten Fingern
- R1.5 Lebensdauer der LED-Anzeige ≥ 500 h
- R2.1 Taste „P“ muss klar erkennbar sein
- R2.2 Zustand der Taste (Ein/Aus) muss sichtbar sein
- R2.3 Reaktionszeit beim Betätigen ≤ 500 ms
- R2.4 Taste „P“ muss sich in Form oder Farbe unterscheiden
- R2.5 Die Funktion muss 10 Minuten laufen und sich selbst deaktivieren
- R3.1 Temperatur in der Pfanne wird kontinuierlich überwacht
- R4.1 Gerät verfügt über einen Ein-/Aus-Schalter
- R4.2 Schalter hält ≥ 100.000 Betätigungen ohne Defek
- R5.3 Zeit wird heruntergezählt und Kochzone abschalten

Diese wurden anschließend in der Traceability Matrix nochmal genauer beschrieben.



---

### Schritt 2: Architektur

[Architektur2](../Sprint2/Architektur2.md)

---

### Schritt 3: Design

[Design2](https://github.com/adrian29042006/Software_Engineering_Git/blob/main/docs/Sprint2/Design2.md)

---


### Schritt 4: Testphase

[Test2](https://github.com/adrian29042006/Software_Engineering_Git/blob/main/docs/Sprint2/Test2.md )

---

# Schritt 5: Review und Retrospektive – Sprint 2

## Was lief gut?
- Alle ausgewählten Kernanforderungen (R1.4, R1.5, R2.4, R2.5, R4.2, R5.3, inkl. Reaktionszeiten und Timerfunktionen) wurden umgesetzt.
- Die Implementierung der Sicherheitsfunktionen (z.B. automatische Abschaltung, zuverlässiger Timer) hat das System in typischen Nutzungssituationen deutlich vertrauenswürdiger gemacht.
- Erfahrungen aus Sprint 1 konnten genutzt werden, z.B. bei der Priorisierung der Requirements und der Einteilung von Entwicklungsaufgaben.
- Teamarbeit und Kommunikation innerhalb des SCRUM-Frameworks funktionierten effizient; tägliche Stand-ups halfen, den Überblick über Fortschritte zu behalten.

## Was lief nicht gut?
- Der Zeitplan konnte erneut nicht vollständig eingehalten werden, u.a. durch Verzögerungen in Sprint 1.
- Zeitdruck hat dazu geführt, dass einige Implementierungsdetails unter Stress erledigt werden mussten.
- Teilweise wurde der Testaufwand für Reaktionszeiten und Timerfunktionen unterschätzt.

## Was werde ich im nächsten Sprint anders machen?
- Früher mit der Planung starten, um Puffer für Testphasen und unerwartete Verzögerungen einzuplanen.
- Priorisierung der Aufgaben noch klarer nach kritischen Anforderungen (z.B. Sicherheitsfunktionen) vornehmen.
- Motivation hochhalten, da das Projekt sich dem Ende nähert; regelmäßige kurze Feedback-Schleifen einplanen, um kleine Erfolge sichtbar zu machen.

## Lessons Learned
- SCRUM hilft, den Entwicklungsfortschritt transparent zu halten, aber Zeitplanung und realistische Schätzungen sind entscheidend für die Einhaltung von Sprints.
- Sicherheits- und Zeitfunktionen sollten frühzeitig in die Architektur eingebunden werden, um spätere Nacharbeiten zu vermeiden.
- Dokumentation und klare Zuordnung von Requirements zu Komponenten erleichtern sowohl die Implementierung als auch spätere Reviews.
- Kontinuierliches Testen der Reaktionszeiten und Timerfunktionen ist essentiell, um die Systemzuverlässigkeit zu gewährleisten.


  

