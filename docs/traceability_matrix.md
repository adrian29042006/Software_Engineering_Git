# Traceability Matrix – Induktionskochfeld

## Funktionale Anforderungen

| Anforderungs-ID | Beschreibung | Komponenten | Testfälle / Bemerkungen | **Zugeordnete Komponente(n)**  | Design Klassen         | Sprint |
|-----------------|-------------|--------------|-------------------------|--------------------------------|------------------------|--------|
| R1.1 | 9 klar unterscheidbare Leistungsstufen | UI, Steuerung/Logik, Aktuatoren | Prüfen der Auswahl jeder Stufe und Umsetzung im Kochfeld |`UIHandler`, `PowerController`, `Heizelemente`|`LED-Display`, `Button`, `PowerManager`, `PowerSwitch`| Sprint 1✔️ |
| R1.2 | Auswahl der Leistungsstufen über Touch, Drehknopf oder Tasten | UI, Steuerung/Logik | Test der Eingabemöglichkeiten | `UIHandler` | `Button`, `Touchcontroller`| Sprint 1✔️ |
| R2.1 | Taste „P“ muss klar erkennbar sein | UI | Sichtprüfung und Vergleich mit anderen Tasten |`UIHandler` | `LED-Display`, `Button`, `LED`| Sprint 1✔️ |
| R2.5 | Die Funktion muss 10 Minuten laufen und sich selbst deaktivieren | Steuerung/Logik, Sicherheitsmodul, Aktuatoren | Timer testen, automatische Abschaltung prüfen | `PowerController`, `Heizelemente`|`TimerController`, `InducitonCoil`, `TimerController`, `TimerManager`|  Sprint 2✔️ |
| R3.1 | Temperatur in der Pfanne wird kontinuierlich überwacht | Sensorik, Steuerung/Logik | Modultest: 1,2 und 3, Integrationstest: 4, 5 und 6 |`TempSensorReader`, `PowerController`, `Heizelemente`| `TimerController`, `TempController`,`TempSensor`, `InducitonCoil`, `TimerController`, `TimerManager` | Sprint 1✔️ |
| R4.1 | Gerät verfügt über einen Ein-/Aus-Schalter | UI, Steuerung/Logik, Aktuatoren | Schalterfunktion testen | `UIHandler`, `PowerController`,  `Heizelemente` | `Button`|  Sprint 1✔️ |
| R5.1 | Einstellbare Kochzeit von 1–20 Minuten | UI, Steuerung/Logik, Aktuatoren | Timerfunktion testen |`UIHandler`, `Touchcontroller`, `Heizelemente`|`Button`|  Sprint 3✔️ |
| R5.3 | Zeit wird heruntergezählt und Kochzone abschalten | Steuerung/Logik, Sicherheitsmodul, Aktuatoren | Timerabschaltung prüfen |  `PowerController`,  `Heizelemente`| `TimerController`, `TempController`,`TempSensor`, `InducitonCoil`, `TimerController`, `TimerManager`, `PowerController`| Sprint 2✔️ |

## Nicht-funktionale Anforderungen

| Anforderungs-ID | Beschreibung | Komponenten | Testfälle / Bemerkungen |**Zugeordnete Komponente(n)**  | Design Klassen         |Sprint |
|-----------------|--------------|-------------|-------------------------|-------------------------------|------------------------|-------|
| R1.3 | Reaktionszeit ≤ 100 ms | UI, Steuerung/Logik | Zeitmessung der Leistungsstufenauswahl |`UIHandler`, `PowerController`, `Heizelemente`| `Button`, `Touchcontroller`, `Mikrocontroller`|  Sprint 3✔️|
| R1.4 | Zuverlässige Funktion bei verschmutzten Fingern | UI, Steuerung/Logik | Touch-Eingabe mit feuchten Fingern prüfen |`UIHandler`| `Button`, `Touchcontroller` | Sprint 2✔️
| R1.5 | Lebensdauer der LED-Anzeige ≥ 500 h | UI | Dauerbetriebstest der LEDs |`UIHandler`, `PowerController`|  `LED-Display`, `Button`, `LED`, `Touchcontroller`| Sprint 2✔️|
| R2.2 | Zustand der Taste (Ein/Aus) muss sichtbar sein | UI | Sichtprüfung der Zustandsanzeige |`UIHandler` |`LED-Display`, `Button`, `LED`| Sprint 1✔️| 
| R2.3 | Reaktionszeit beim Betätigen ≤ 500 ms | UI, Steuerung/Logik | Reaktionszeitmessung der Taste |`UIHandler`, `PowerController`, `Heizelemente`| `Button`, `TouchController`, `TempController`|Sprint 3✔️|
| R2.4 | Taste „P“ muss sich in Form oder Farbe unterscheiden | UI | Sichtprüfung / Designvergleich |`UIHandler` |  `Button`| Sprint 2✔️|
| R3.2 | Anzeigeverzögerung ≤ 500 ms | UI, Sensorik, Steuerung/Logik | Integrationstest: 4 und 6 |`UIHandler`, `PowerController`|`LED-Display`,`Mikrocontroller`|  Sprint 3✔️|
| R4.2 | Schalter hält ≥ 100.000 Betätigungen ohne Defekt | UI, Aktuatoren | Dauerbelastungstest des Schalters |`UIHandler`|`Button`| Sprint 2✔️|
| R5.2 | Timeranzeige reagiert mit max. 500 ms Verzögerung | UI, Steuerung/Logik | Test der Timeranzeige auf Genauigkeit |`UIHandler`, `PowerController`|`LED-Display`,`Mikrocontroller`|Sprint 3✔️|
