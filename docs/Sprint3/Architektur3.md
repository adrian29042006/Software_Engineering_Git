## Komponentendiagramm:
Senden  von Eingaben
---
<img width="1920" height="1080" alt="User (2)" src="https://github.com/user-attachments/assets/2520096a-9899-453c-8022-9d70a343d823" />

## Komponentendiagramm zugeordnete Requierements

| Komponente | Zugeordnete Requirements |
|-----------|--------------------------|
| **User Interface (UI)** | R1.1, R1.2, R1.3, R1.4, R1.5, R2.1, R2.2, R2.3, R2.4, R4.1, R4.2 |
| **Steuerung / Logik (MCU)** | R1.1, R1.2, R1.3, R1.4, R2.3, R2.5, R3.1, R3.2, R4.1, R5.1, R5.3 |
| **Sensorik** | R1.4, R3.1 |
| **Sicherheitsmodul** | R2.5, R3.1, R5.3 |
| **Aktuatoren** | R1.1, R2.5, R4.1, R4.2, R5.3 |
| **Zeit-/Timer-Modul** | R2.5, R5.1, R5.2, R5.3 |
| **Leistungsabschaltstufe** | R2.5, R5.3 |
| **Echtzeit-/Interrupt-Modul** | R1.3, R2.3, R3.2, R5.2 |
| **Timer-/Einstellungsmodul** | R5.1, R5.2 |

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


### Zeit-/Timer-Modul
- Bereitstellung der Countdown-Funktion (R2.5, R5.3)  
- Automatische Deaktivierung der Funktion nach Ablauf  
- Signalisiert das Ende der Zeit an Steuerung, Sicherheitsmodul und Aktuatoren  

### Leistungsabschaltstufe
- Physische Umsetzung der Abschaltung der Kochzone (R2.5, R5.3)  
- Entkopplung von Logik/MCU und Hochleistungsteil  
- Sicherstellung der Abschaltung auch bei Ausfall der Steuerung
  
### Echtzeit-/Interrupt-Modul
- Verarbeitung von Benutzereingaben, Sensordaten und Anzeige-Updates mit minimaler Latenz  
- Sicherstellung der Reaktionszeiten ≤ 100 ms (R1.3), ≤ 500 ms (R2.3, R3.2)  
- Koordination mit Steuerung und UI für zeitkritische Operationen

### Timer-/Einstellungsmodul
- Verwaltung der einstellbaren Kochzeit (1–20 min) (R5.1)  
- Ausgabe der Timerwerte an Anzeige und Steuerung  
- Sicherstellen, dass Timeranzeige höchstens 500 ms verzögert reagiert (R5.2)  
- Signalisiert Ende der Kochzeit an Steuerung, Sicherheitsmodul und Aktuatoren

  
---
---

## Fazit
Mit dem Zeit-/Timer-Modul und der Leistungsabschaltstufe sind alle zeitabhängigen und sicherheitskritischen Funktionen (R2.5, R5.3) robust abgedeckt.  
Die Architektur deckt alle relevanten Sprint-1- und Sprint-2-Requirements vollständig ab und stellt einen sicheren, zuverlässigen Betrieb sicher.
