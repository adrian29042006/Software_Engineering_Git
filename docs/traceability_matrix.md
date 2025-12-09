# Traceability Matrix – Induktionskochfeld

## Funktionale Anforderungen

| Anforderungs-ID | Beschreibung | Komponenten | Testfälle / Bemerkungen | **Zugeordnete Komponente(n)**  | Design Klassen         |
|-----------------|-------------|--------------|-------------------------|--------------------------------|------------------------|
| R1.1 | 9 klar unterscheidbare Leistungsstufen | UI, Steuerung/Logik, Aktuatoren | Prüfen der Auswahl jeder Stufe und Umsetzung im Kochfeld |`PowerController`, `UIHandler`, `Heizelemente`|`LED-Display`, `Button`, `PowerManager`, `PowerSwitch`|
| R1.2 | Auswahl der Leistungsstufen über Touch, Drehknopf oder Tasten | UI, Steuerung/Logik | Test der Eingabemöglichkeiten | `UIHandler` | `Button`, `Touchcontroller`|
| R2.1 | Taste „P“ muss klar erkennbar sein | UI | Sichtprüfung und Vergleich mit anderen Tasten |`UIHandler` | `LED-Display`, `Button`, `LED`
| R2.5 | Die Funktion muss 10 Minuten laufen und sich selbst deaktivieren | Steuerung/Logik, Sicherheitsmodul, Aktuatoren | Timer testen, automatische Abschaltung prüfen |
| R3.1 | Temperatur in der Pfanne wird kontinuierlich überwacht | Sensorik, Steuerung/Logik | Modultest: 1,2 und 3, Integrationstest: 4, 5 und 6 |`TempSensorReader`, `PowerController`, `Heizelemente`| `TimerController`, `TempController`,`TempSensor`, `TempSensor`, `InducitonCoil`, `TimerController`, `TimerManager` |
| R4.1 | Gerät verfügt über einen Ein-/Aus-Schalter | UI, Steuerung/Logik, Aktuatoren | Schalterfunktion testen | `UIHandler`, `PowerController`,  `Heizelemente` | `Button`
| R5.1 | Einstellbare Kochzeit von 1–20 Minuten | UI, Steuerung/Logik, Aktuatoren | Timerfunktion testen |
| R5.3 | Zeit wird heruntergezählt und Kochzone abschalten | Steuerung/Logik, Sicherheitsmodul, Aktuatoren | Timerabschaltung prüfen |

## Nicht-funktionale Anforderungen

| Anforderungs-ID | Beschreibung | Komponenten | Testfälle / Bemerkungen |**Zugeordnete Komponente(n)**  | Design Klassen         |
|-----------------|--------------|-------------|-------------------------|-------------------------------|------------------------|
| R1.3 | Reaktionszeit ≤ 100 ms | UI, Steuerung/Logik | Zeitmessung der Leistungsstufenauswahl |`UIHandler`, `PowerController`, `Heizelemente`| `Button`, `Touchcontroller`, `Mikrocontroller`|
| R1.4 | Zuverlässige Funktion bei verschmutzten Fingern | UI, Steuerung/Logik | Touch-Eingabe mit feuchten Fingern prüfen |
| R1.5 | Lebensdauer der LED-Anzeige ≥ 500 h | UI | Dauerbetriebstest der LEDs |
| R2.2 | Zustand der Taste (Ein/Aus) muss sichtbar sein | UI | Sichtprüfung der Zustandsanzeige |`UIHandler` |`LED-Display`, `Button`, `LED`|
| R2.3 | Reaktionszeit beim Betätigen ≤ 500 ms | UI, Steuerung/Logik | Reaktionszeitmessung der Taste |`UIHandler`, `PowerController`, `Heizelemente`| `Button`, `TouchController`, `TempController`|
| R2.4 | Taste „P“ muss sich in Form oder Farbe unterscheiden | UI | Sichtprüfung / Designvergleich |
| R3.2 | Anzeigeverzögerung ≤ 500 ms | UI, Sensorik, Steuerung/Logik | Integrationstest: 4 und 6 |
| R4.2 | Schalter hält ≥ 100.000 Betätigungen ohne Defekt | UI, Aktuatoren | Dauerbelastungstest des Schalters |
| R5.2 | Timeranzeige reagiert mit max. 500 ms Verzögerung | UI, Steuerung/Logik | Test der Timeranzeige auf Genauigkeit |
