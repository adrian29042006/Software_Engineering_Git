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


### Schritt 5: Testphase
## Modultests (Sensor)
Testfall 1: „Sensorwert innerhalb normaler Temperatur“
→ R3.1 (kontinuierliche Temperaturüberwachung, Genauigkeit als Qualitätsmerkmal)​


Testfall 2: „Sensorwert außerhalb Grenzbereich“
→ R3.1 (Überwachung) + R2.5/R5.3 indirekt, weil ein Fehler zur Abschaltung / Sicherheitsreaktion führt, auch wenn das nicht explizit als eigenes Safety‑Requirement formuliert ist.​


Testfall 3: „Sensor liefert fehlerhafte Werte (HW‑Fehler)“
→ R3.1 (Überwachung der Temperaturdaten) + R2.5/R5.3 indirekt (Sicherheitsmodus/Abschaltung bei Fehler).​


## Integrationstests (Sensor + Steuerung)
Testfall 4: „Sensor + Kochfeldsteuerung normale Kommunikation“
→ R3.1 (Temperaturüberwachung) + R1.1/R1.2 (Leistungsstufen einstellen und anpassen).​


Testfall 5: „Sensor + Kochfeldsteuerung Ausfall Sensor“
→ R3.1 (Überwachung) + R2.5/R5.3 (Abschalten/Sicherheitsverhalten bei Problem).​

Testfall 6: „Sensor + Kochfeldsteuerung Grenzwerttemperatur“
→ R3.1 (Überwachung) + R1.1 (Leistungsregelung) + R2.5/R5.3 (kein Überschreiten, ggf. Abschalten).


---

### Schritt 6: Rewies und Retroperspektive


Was lief gut?
- Alle Anforderungen wurden umgesetzt
- Die Umsetzung der Reaktionszeit‑Anforderungen hat dafür gesorgt, dass Eingaben und Anzeigen nun deutlich schneller und direkter wirken.
- Die Erweiterung der Timer‑Funktionen konnte ohne größere Umstrukturierungen integriert werden und passt gut in das bestehende Konzept.
- Zeitplan wurde eingehalten
- Das Gefühl, ein „spürbar schnelleres“ und besser reagierendes System umgesetzt zu haben, sorgt für Stolz und ein stärkeres Verantwortungsbewusstsein für die Produktqualität.
  
Was nicht gut lief?
- Die exakten Messungen der Reaktionszeiten und Anzeigeverzögerungen wurden nicht gemacht.
- Der Druck, genaue Zeitmessungen und Performance-Ziele zu erreichen, hat zeitweise zu Stress geführt

Lessons Learned:
- Es lohnt sich, bei der Planung neben technischen Zielen auch den Arbeitsaufwand und die mentale Belastung mitzudenken, um zukünftige Sprints fokussierter und entspannter gestalten zu können.
