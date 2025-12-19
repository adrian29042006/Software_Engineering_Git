# Sprint 3
---
### 1. Sprint Planning
Zu Beginn des 3. Sprint habe ich die relevanten Anforderungen (Requirements) ausgewählt. Konkret wurde die folgende Kernfunktion identifiziert und berücksichtigt:
- Performance  / Reaktionszeit
- Funktionale Timer-Eigenschaften (nice to have)


---
Sprint Datum : 12.12.2025
---

Es wurden diese Requirements ergänzt für Sprint 3:
- R1.3 Reaktionszeit ≤ 100 ms
- R2.3 Reaktionszeit beim Betätigen ≤ 500 ms
- R3.2 Anzeigeverzögerung ≤ 500 ms
- R5.1 Einstellbare Kochzeit von 1–20 Minuten
- R5.2 Timeranzeige reagiert mit max. 500 ms Verzögerung

Bei der Auswahl der Requirements wurde darauf geachtet, Nice-to-Have-Requirementsin diesem Sprint aufzunehmen.


Diese wurden anschließend in der Traceability Matrix nochmal genauer beschrieben.



---

### Schritt 2: Architektur

[Architektur](Architektur3.md)

---

### Schritt 3: Design

[Design3](https://github.com/adrian29042006/Software_Engineering_Git/blob/main/docs/Sprint1/Design3.md)

---


### Schritt 4: Testphase
[Testen](../../Testen)
---

### Schritt 5: Rewies und Retroperspektive


# Schritt 5: Review und Retrospektive – Sprint 3

## Was lief gut?
- Alle neu aufgenommenen Anforderungen (R1.3, R2.3, R3.2, R5.1, R5.2) konnten erfolgreich umgesetzt werden.  
- Die Implementierung des Echtzeit-/Interrupt-Moduls hat dazu geführt, dass Eingaben und Anzeigen nun innerhalb der geforderten Reaktionszeiten erfolgen.  
- Das Timer-/Einstellungsmodul ermöglicht nun die flexible Einstellung der Kochzeit von 1–20 Minuten und eine reaktionsschnelle Timeranzeige (≤ 500 ms Verzögerung).  
- Die Erweiterung der bestehenden Architektur um die neuen Module war problemlos möglich, ohne dass Kernfunktionen beeinträchtigt wurden.  
- Das System wirkt spürbar schneller und benutzerfreundlicher, was das Vertrauen in das Produkt erhöht.

## Was lief nicht gut?
- Exakte Messungen der Reaktionszeiten für alle Eingaben und Anzeigen konnten teilweise nicht in allen Szenarien durchgeführt werden.  
- Der Aufwand für die Integration der Timer‑Funktionen war höher als ursprünglich geplant.  
- Es gab zeitweise Unsicherheit bei der Abstimmung zwischen Steuerung, Timer-Modul und Anzeige.

## Lessons Learned
- Frühzeitige Planung und Zuordnung neuer Module zu den Anforderungen erleichtert die Umsetzung und verhindert spätere Konflikte.  
- Teststrategien für Performance- und Echtzeit-Anforderungen sollten bereits bei der Architekturplanung berücksichtigt werden.  
- Durch das Hinzufügen dedizierter Module (Echtzeit-/Interrupt-Modul, Timer-/Einstellungsmodul) konnte die Systemreaktionszeit zuverlässig eingehalten werden – separate Module erleichtern sowohl Implementierung als auch zukünftige Erweiterungen.  
- SCRUM-Reviews und Retrospektiven helfen, Lessons Learned unmittelbar in die nächsten Sprints zu übertragen.  

## Ausblick
- Weitere Optimierung der Reaktionszeiten und Timeranzeige bei unterschiedlichen Lastbedingungen.  
- Überprüfung und Validierung der Benutzerfreundlichkeit unter realen Nutzungsszenarien.  
- Fortführung der Dokumentation und Vorbereitung der finalen Systemintegration.
