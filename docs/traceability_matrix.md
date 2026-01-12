# Traceability Matrix – Induktionskochfeld


## Funktionale Anforderungen

| Anforderungs-ID | Beschreibung | Testfälle / Bemerkungen | Schnittstellen | Zugeordnete Komponenten | Design Klassen | Sprint | Priorität | Begründung |
|-----------------|-------------|------------------------|----------------|------------------------|----------------|--------|-----------|------------|
| R1.1 | 9 klar unterscheidbare Leistungsstufen | UT1, IT1 | `UserInterface ↔ Steuerung/Logik`, `Steuerung/Logik ↔ Leistungsabschaltstufe` | UserInterface, Steuerung/Logik, Leistungsabschaltstufe | LED-Display, PowerManager, PowerSwitch, Mikrocontroller | Sprint 1✔️ | Hoch | Grundfunktion des Kochfelds |
| R1.2 | Auswahl der Leistungsstufen über Touch, Drehknopf oder Tasten | UT2, IT1 | `UserInterface ↔ Steuerung/Logik` | UserInterface, Steuerung/Logik | Benutzer, TouchController, PowerManager, Mikrocontroller | Sprint 1✔️ | Hoch | Zentrale Benutzerinteraktion |
| R2.1 | Taste „P“ muss klar erkennbar sein | UT8, IT8 | `UserInterface ↔ Anzeige` | UserInterface | Taste P, LED, LED-Display | Sprint 1✔️ | Mittel | Auffindbarkeit der Sonderfunktion |
| R2.4 | Taste „P“ unterscheidet sich in Form oder Farbe | UT5, IT4 | `UserInterface ↔ Anzeige` | UserInterface | Taste P, LED | Sprint 2✔️ | Mittel | Ergonomie |
| R2.5 | Funktion muss 10 Minuten laufen und sich selbst deaktivieren | UT6, IT5 | `Timer/Einstellungsmodul ↔ Steuerung/Logik`, `Steuerung/Logik ↔ Leistungsabschaltstufe` | Timer/Einstellungsmodul, Zeit/Timer Modul, Sicherheitsmodul, Leistungsabschaltstufe | TimerController, TimerManager, PowerManager, Mikrocontroller | Sprint 2✔️ | Hoch | Sicherheitsabschaltung |
| R3.1 | Temperatur in der Pfanne kontinuierlich überwachen | UT3, IT3, IT6 | `Sensorik ↔ Steuerung/Logik` | Sensorik, Steuerung/Logik | TempSensor, TempController, Mikrocontroller | Sprint 1✔️ | Hoch | Sicherheit und Effizienz |
| R3.2 | Anzeigeverzögerung ≤ 500 ms | UT10, IT8, IT9 | `Steuerung/Logik ↔ UserInterface` | UserInterface, Echtzeit/Interrupt Modul | LED-Display, Mikrocontroller | Sprint 3✔️ | Mittel | Benutzerkomfort |
| R4.1 | Gerät verfügt über Ein-/Aus-Schalter | UT7, IT2 | `UserInterface ↔ Steuerung/Logik`, `Steuerung/Logik ↔ Leistungsabschaltstufe` | UserInterface, Steuerung/Logik, Leistungsabschaltstufe | Benutzer, PowerSwitch, Mikrocontroller | Sprint 1✔️ | Hoch | Grundlegende Sicherheitsfunktion |
| R4.2 | Schalter hält ≥ 100.000 Betätigungen ohne Defekt | UT7, IT6 | `Mechanische Betätigung ↔ Aktuator` | Aktuator | PowerSwitch | Sprint 2✔️ | Mittel | Langlebigkeit |
| R5.1 | Einstellbare Kochzeit von 1–20 Minuten | IT7, IT9 | `UserInterface ↔ Timer/Einstellungsmodul` | UserInterface, Timer/Einstellungsmodul, Zeit/Timer Modul | Benutzer, TouchController, TimerController, TimerManager | Sprint 3✔️ | Hoch | Zeitsteuerung |
| R5.2 | Timeranzeige reagiert mit max. 500 ms Verzögerung | IT7, IT9 | `Zeit/Timer Modul ↔ UserInterface` | UserInterface, Echtzeit/Interrupt Modul | LED-Display, TimerController, Mikrocontroller | Sprint 3✔️ | Mittel | Komfortfunktion |
| R5.3 | Zeit wird heruntergezählt und Kochzone abgeschaltet | UT6, IT5 | `Zeit/Timer Modul ↔ Steuerung/Logik`, `Steuerung/Logik ↔ Heizmodul` | Zeit/Timer Modul, Sicherheitsmodul, Heizmodul, Leistungsabschaltstufe | TimerController, TimerManager, PowerManager, InductionCoil | Sprint 2✔️ | Hoch | Verhindert Überkochen oder Brand |

---

## Nicht-funktionale Anforderungen

| Anforderungs-ID | Beschreibung | Testfälle / Bemerkungen | Schnittstellen | Zugeordnete Komponenten | Design Klassen | Sprint | Priorität | Begründung |
|-----------------|--------------|------------------------|----------------|------------------------|----------------|--------|-----------|------------|
| R1.3 | Reaktionszeit ≤ 100 ms | UT8, IT8 | `UserInterface ↔ Echtzeit/Interrupt Modul` | UserInterface, Echtzeit/Interrupt Modul | TouchController, Mikrocontroller | Sprint 3✔️ | Mittel | Bediengefühl |
| R1.4 | Zuverlässige Funktion bei verschmutzten Fingern | UT4, IT4 | `UserInterface ↔ Touch-Erfassung` | UserInterface | TouchController | Sprint 2✔️ | Mittel | Ergonomie |
| R1.5 | Lebensdauer der LED-Anzeige ≥ 500 h | UT5 | `Anzeige ↔ UserInterface` | UserInterface | LED, LED-Display | Sprint 2✔️ | Niedrig | Wartungsfreundlichkeit |
| R2.2 | Zustand der Taste (Ein/Aus) sichtbar | UT3, IT1 | `Steuerung/Logik ↔ Anzeige` | UserInterface | LED, LED-Display, PowerSwitch | Sprint 1✔️ | Hoch | Klarer Betriebszustand |
| R2.3 | Reaktionszeit beim Betätigen ≤ 500 ms | UT9, IT8 | `UserInterface ↔ Steuerung/Logik ↔ Aktuator` | UserInterface, Steuerung/Logik, Aktuator | TouchController, PowerManager, Mikrocontroller | Sprint 3✔️ | Mittel | Komfortfunktion |

---

