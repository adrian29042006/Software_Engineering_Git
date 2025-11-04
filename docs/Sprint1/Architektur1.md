## Komponentendiagramm:
<img width="1270" height="714" alt="User" src="https://github.com/user-attachments/assets/6cd9abb8-b4d9-4a46-8df0-abaf0471fc04" />

---

## Komponentendiagramm zugeordnete Requierements

| Komponente | Zugeordnete Requirements |
|------------|-------------------------|
| User Interface (UI) | R1.1, R1.2, R2.1, R4.1, R5.1, R1.3, R1.4, R1.5, R2.2, R2.3, R2.4, R3.2, R5.2, R4.2 |
| Steuerung / Logik (MCU) | R1.1, R1.2, R2.5, R3.1, R4.1, R5.1, R5.3, R1.3, R1.4, R2.3, R3.2, R5.2 |
| Sensorik | R3.1, R3.2 |
| Sicherheitsmodul | R2.5, R5.3 |
| Aktuatoren | R1.1, R2.5, R4.1, R5.1, R5.3, R4.2 |

---
## Verantwortlichkeit der Komponenten

**User Interface (UI)**
- Eingaben an Steuerung/Logik
- Anzeigen von Statusinfos von Steuerung, Sensorik und Sicherheitsmodul

**Steuerung / Logik**
- Empfängt Eingaben von UI
- Steuert Aktuatoren (Leistungsstufen, Boost, Timer)
- Liest Sensorik-Daten (Temperatur)
- Überwacht Sicherheitsmodul

**Sensorik**
- Liefert Temperatur- und Statusdaten an Steuerung/Logik

**Sicherheitsmodul**
- Überwacht Induktionsfeld, Strom, Temperatur
- Sendet Warnungen / Abschaltungen an Steuerung/Logik

**Aktuatoren**
- Setzen Steuerbefehle der Logik um (Heizung, LEDs, Summer)

---

 [★ Traceability Matrix – Induktionskochfeld](docs/traceability_matrix.md)


