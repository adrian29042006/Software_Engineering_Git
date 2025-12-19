## Komponentendiagramm:

<img width="1920" height="1080" alt="User (1)" src="https://github.com/user-attachments/assets/c60f9d13-ea67-41ab-bfa9-333a0b6e84bc" />

# Architektur – Requirement-Zuordnung und Verantwortlichkeiten

## Zuordnung: Komponenten → Requirements

| Komponente | Zugeordnete Requirements |
|-----------|--------------------------|
| **User Interface (UI)** | R1.1, R1.2, R1.4, R1.5, R2.1, R2.2, R2.3, R2.4, R4.1, R4.2 |
| **Steuerung / Logik (MCU)** | R1.1, R1.2, R1.4, R2.3, R2.5, R3.1, R4.1, R5.3 |
| **Sensorik** | R1.4, R3.1 |
| **Sicherheitsmodul** | R2.5, R3.1, R5.3 |
| **Aktuatoren** | R1.1, R2.5, R4.1, R4.2, R5.3 |

---

## Verantwortlichkeiten der Komponenten

### User Interface (UI)
- Erfassung von Benutzereingaben (Tasten, Touch) (R1.2)
- Zuverlässige Bedienung auch bei verschmutzten Fingern (R1.4)
- Visuelle Rückmeldung über LEDs und Anzeigen (R1.5, R2.2)
- Klare Erkennbarkeit und Unterscheidbarkeit der Taste „P“ (R2.1, R2.4)
- Reaktionszeit bei Eingaben ≤ 500 ms (R2.3)
- Mechanische Auslegung der Bedienelemente für hohe Lebensdauer (R4.2)

---

### Steuerung / Logik (MCU)
- Verarbeitung der Benutzereingaben vom UI
- Umsetzung der Leistungsstufen (R1.1)
- Zeitsteuerung mit Countdown und automatischer Abschaltung nach 10 Minuten (R2.5)
- Auswertung der Sensordaten (Temperatur) (R3.1)
- Ansteuerung der Aktuatoren
- Abschaltung der Kochzone bei Ablauf der Zeit oder Fehlerzuständen (R5.3)

---

### Sensorik
- Kontinuierliche Erfassung der Temperatur in der Pfanne (R3.1)
- Unterstützung der zuverlässigen Bedienung durch Plausibilisierung (R1.4)
- Weitergabe der Messwerte an die Steuerung

---

### Sicherheitsmodul
- Überwachung sicherheitskritischer Zustände (z. B. Übertemperatur) (R3.1)
- Erzwingen der automatischen Deaktivierung nach Zeitablauf (R2.5)
- Sichere Abschaltung der Kochzone unabhängig von der Steuerung (R5.3)

---

### Aktuatoren
- Umsetzung der Steuerbefehle der Logik
- Schalten der Heizleistung und der Kochzone (R1.1, R5.3)
- Abschaltung bei Sicherheits- oder Timerereignissen (R2.5)
- Auslegung für ≥ 100.000 Schaltzyklen (R4.2)

---

## Fazit
Die Architekturkomponenten decken alle für Sprint 1 und Sprint 2 definierten funktionalen und nicht-funktionalen Requirements vollständig ab.  
Die Trennung von Steuerungs- und Sicherheitsfunktionen stellt einen zuverlässigen und sicheren Betrieb des Systems sicher.


 [★ Traceability Matrix – Induktionskochfeld](../traceability_matrix.md)



