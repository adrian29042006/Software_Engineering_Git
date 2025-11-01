##Zustandsdiagramm:
<img width="1270" height="714" alt="User" src="https://github.com/user-attachments/assets/6cd9abb8-b4d9-4a46-8df0-abaf0471fc04" />


| **Komponente**      | **Requirements**                                                                          | 
|---------------------|-------------------------------------------------------------------------------------------|
| Sensor(Hardware)    | Req. 1.3, Req. 1.4, Req. 2.3, Req. 2.5, Req. 3.1, Req. 4.2                                | 
| Verarbeitung        | Req. 1.1, Req. 2.5, Req. 5.3                                                              | 
| Steuerung/Anzeige   | Req. 1.2, Req. 1.5 Req. 2.1 Req. 2.2 Req. 2.4 Req. 3.2 Req. 4.1, Req 5.1, Req. 5.2        |

Verantwortlichkeiten der Komponenten:

| **Komponente**      | Rolle            | Verantwortlichkeiten |
|---------------------|------------------|---------------------|
| Sensor (Hardware)   | Hardware-Block   | Misst die Pfannenbodentemperatur und liefert kontinuierlich Sensordaten an die Verarbeitung                                      |
| Verarbeitung        | Logik-Block      | Verarbeitet Sensordaten, steuert Leistungsstufen, aktiviert/deaktiviert Power-Boost, Timer-Countdown, Sicherheitslogik |
| Steuerung/Anzeige   | HMI-Block        | Ermöglicht Benutzereingaben (Touch/Tasten/Drehknopf), zeigt Leistungsstufen, Timer, Power-Boost-Status und Temperatur an    |



Traceability Matrix
| Requirement | Beschreibung | Komponente | Verantwortlichkeit |
|-------------|--------------|------------|------------------|
| R1.1 | 9 klar unterscheidbare Leistungsstufen | Verarbeitung | Leistungsstufen steuern, Heizleistung anpassen |
| R1.2 | Auswahl der Leistungsstufen über Touch/Drehknopf/Tasten | Steuerung/Anzeige | Benutzeroberfläche, Eingaben erfassen |
| R1.3 | Reaktionszeit ≤ 100 ms | Sensor (Hardware) | Sensordaten liefern |
| R1.4 | Zuverlässige Funktion bei verschmutzten Fingern | Sensor (Hardware) | Sensordaten zuverlässig erfassen |
| R1.5 | Lebensdauer der LED-Anzeige ≥ 500 h | Steuerung/Anzeige | Anzeige implementieren |
| R2.1 | Taste „P“ klar erkennbar | Steuerung/Anzeige | Darstellung und Layout der Taste |
| R2.2 | Zustand der Taste sichtbar | Steuerung/Anzeige | Anzeige implementieren |
| R2.3 | Reaktionszeit beim Betätigen ≤ 500 ms | Sensor (Hardware) | Tastenzustand erfassen |
| R2.4 | Taste „P“ unterscheidbar | Steuerung/Anzeige | Anzeige implementieren |
| R2.5 | Funktion 10 Min laufen & selbst deaktivieren | Sensor / Verarbeitung | Sensordaten + Logik steuern Power-Boost |
| R3.1 | Temperatur kontinuierlich überwacht | Sensor (Hardware) | Temperaturdaten liefern |
| R3.2 | Anzeigeverzögerung ≤ 500 ms | Steuerung/Anzeige | Anzeige aktualisieren |
| R4.1 | Gerät verfügt über Ein-/Aus-Schalter | Steuerung/Anzeige | Schalter darstellen / Eingabe erfassen |
| R4.2 | Schalter ≥ 100.000 Betätigungen | Sensor (Hardware) | Hardware Schalter robust |
| R5.1 | Einstellbare Kochzeit 1–20 min | Steuerung/Anzeige | Benutzeroberfläche für Timer |
| R5.2 | Timeranzeige Verzögerung ≤ 500 ms | Steuerung/Anzeige | Countdown korrekt anzeigen |
| R5.3 | Zeit herunterzählen, Kochzone abschalten | Verarbeitung | Timerlogik steuern, Heizelement abschalten |
