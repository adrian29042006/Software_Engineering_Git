# Anforderungen Temperatursensor Induktionskochfeld

## Hier Nochmal eine kleine übersicht von den Requirements

| Nr.   | Typ             | Beschreibung |
|------|-----------------|--------------|
| R1.1 | Funktional      | 9 klar unterscheidbare Leistungsstufen |
| R1.2 | Funktional      | Auswahl der Leistungsstufen über Touch, Drehknopf oder Tasten |
| R1.3 | Nicht-Funktional | Reaktionszeit ≤ 100 ms |
| R1.4 | Nicht-Funktional | Zuverlässige Funktion auch bei verschmutzten Fingern |
| R1.5 | Nicht-Funktional | Lebensdauer der LED-Anzeige ≥ 500 h |
|------|-----------------|--------------|
| R2.1 | Funktional      | Taste „P“ muss klar erkennbar sein |
| R2.2 | Nicht-Funktional | Zustand der Taste (Ein/Aus) muss sichtbar sein |
| R2.3 | Nicht-Funktional | Reaktionszeit beim Betätigen ≤ 500 ms |
| R2.4 | Nicht-Funktional | Taste „P“ muss sich in Form oder Farbe von anderen unterscheiden |
| R2.5 | Funktional |Die Funktion muss 10 Minuten lang laufen und sich selbst deaktivieren. |
|------|-----------------|--------------|
| R3.1 | Funktional      | Temperatur in der Pfanne wird kontinuierlich überwacht |
| R3.2 | Nicht-Funktional | Anzeigeverzögerung ≤ 500 ms |
|------|-----------------|--------------|
| R4.1 | Funktional      | Gerät verfügt über einen Ein-/Aus-Schalter |
| R4.2 | Nicht-Funktional | Schalter hält ≥ 100 000 Betätigungen ohne Defekt |
|------|-----------------|--------------|
| R5.1 | Funktional      | Einstellbare Kochzeit von 1–20 Minuten |
| R5.2 | Nicht-Funktional | Timeranzeige reagiert mit max. 500 ms Verzögerung |
| R5.3 | Funktional | Die Zeit wird heruntergezählt werden und die Kochzone wird daraufhin abschalten. |

---

![Komponentendiagramm](https://github.com/adrian29042006/Software_Engineering_Git/blob/main/lib/Sensor%20(Hardware%20Block)%20NTC%20Widerstand%20ADC.pdf)

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

