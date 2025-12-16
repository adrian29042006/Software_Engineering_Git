# Traceability Matrix – Induktionskochfeld

## Funktionale Anforderungen

| Anforderungs-ID | Beschreibung | Testfälle / Bemerkungen | Schnittstellen | Zugeordnete Komponenten | Design Klassen | Sprint | Priorität | Begründung |
|-----------------|-------------|------------------------|----------------|------------------------|----------------|--------|-----------|------------|
| R1.1 | 9 klar unterscheidbare Leistungsstufen | UT1, IT1 | `UI <-> PowerController`, `PowerController <-> Heizelemente` | UI, Steuerung/Logik, Aktuatoren | `LED-Display`, `PowerManager`, `PowerSwitch` | Sprint 1✔️ | Hoch | Grundfunktion des Kochfelds; essenziell für Benutzerkontrolle |
| R1.2 | Auswahl der Leistungsstufen über Touch, Drehknopf oder Tasten | UT2, IT1 | `UI <-> PowerController` | UI, Steuerung/Logik | `Button`, `Touchcontroller` | Sprint 1✔️ | Hoch | Direkte Bedienbarkeit, zentrale Benutzerinteraktion |
| R2.1 | Taste „P“ muss klar erkennbar sein | UT8, IT8 | `UI <-> LED` | UI | `LED-Display`, `Button`, `LED` | Sprint 1✔️ | Mittel | Nutzer muss Sonderfunktion leicht finden, Sicherheit weniger kritisch |
| R2.4 | Taste „P“ muss sich in Form oder Farbe unterscheiden | UT5, IT4 | `UI <-> LED` | UI | `Button` | Sprint 2✔️ | Mittel | Ergonomie und intuitive Nutzung |
| R2.5 | Funktion muss 10 Minuten laufen und sich selbst deaktivieren | UT6, IT5 | `PowerController <-> TimerController`, `TimerController <-> Heizelemente` | Steuerung/Logik, Sicherheitsmodul, Aktuatoren | `TimerController`, `InductionCoil`, `TimerManager` | Sprint 2✔️ | Hoch | Sicherheitsfunktion gegen Überhitzung oder Brandrisiko |
| R3.1 | Temperatur in der Pfanne kontinuierlich überwachen | UT3, IT3, IT6 | `TempSensor <-> PowerController`, `PowerController <-> UI` | Sensorik, Steuerung/Logik | `TempController`, `TempSensor`, `InductionCoil`, `TimerController`, `TimerManager` | Sprint 1✔️ | Hoch | Grundvoraussetzung für effizientes und sicheres Kochen |
| R3.2 | Anzeigeverzögerung ≤ 500 ms | UT10, IT8, IT9 | `UI <-> PowerController` | UI, Sensorik, Steuerung/Logik | `LED-Display`, `Mikrocontroller` | Sprint 3✔️ | Mittel | Komfort für den Benutzer |
| R4.1 | Gerät verfügt über Ein-/Aus-Schalter | UT7, IT2 | `UI <-> PowerController`, `PowerController <-> Heizelemente` | UI, Steuerung/Logik, Aktuatoren | `Button` | Sprint 1✔️ | Hoch | Grundlegende Ein-/Aus-Funktion, Sicherheitsaspekt |
| R4.2 | Schalter hält ≥ 100.000 Betätigungen ohne Defekt | UT7, IT6 | `UI <-> PowerController` | UI, Aktuatoren | `Button` | Sprint 2✔️ | Mittel | Langlebigkeit, Benutzerkomfort |
| R5.1 | Einstellbare Kochzeit von 1–20 Minuten | IT7, IT9 | `UI <-> TimerController`, `TimerController <-> Heizelemente` | UI, Steuerung/Logik, Aktuatoren | `Button` | Sprint 3✔️ | Hoch | Kernfunktion für Zeitsteuerung beim Kochen |
| R5.2 | Timeranzeige reagiert mit max. 500 ms Verzögerung | IT7, IT9 | `UI <-> TimerController` | UI, Steuerung/Logik | `LED-Display`, `Mikrocontroller` | Sprint 3✔️ | Mittel | Komfortfunktion |
| R5.3 | Zeit wird heruntergezählt und Kochzone abschalten | UT6, IT5 | `TimerController <-> PowerController`, `PowerController <-> Heizelemente` | Steuerung/Logik, Sicherheitsmodul, Aktuatoren | `TimerController`, `InductionCoil` | Sprint 2✔️ | Hoch | Sicherheitsfunktion, verhindert Überkochen oder Brandgefahr |

## Nicht-funktionale Anforderungen

| Anforderungs-ID | Beschreibung | Testfälle / Bemerkungen | Schnittstellen | Zugeordnete Komponenten | Design Klassen | Sprint | Priorität | Begründung |
|-----------------|--------------|------------------------|----------------|------------------------|----------------|-------|-----------|------------|
| R1.3 | Reaktionszeit ≤ 100 ms | UT8, IT8 | `UI <-> PowerController` | UI, Steuerung/Logik | `Button`, `Touchcontroller`, `Mikrocontroller` | Sprint 3✔️ | Mittel | Benutzerfreundlichkeit |
| R1.4 | Zuverlässige Funktion bei verschmutzten Fingern | UT4, IT4 | `UI <-> Touchcontroller` | UI, Steuerung/Logik | `Button`, `Touchcontroller` | Sprint 2✔️ | Mittel | Ergonomie, Bedienkomfort |
| R1.5 | Lebensdauer der LED-Anzeige ≥ 500 h | UT5 | `UI <-> LED` | UI | `LED-Display`, `Button`, `LED`, `Touchcontroller` | Sprint 2✔️ | Niedrig | Wartungsfreundlichkeit |
| R2.2 | Zustand der Taste (Ein/Aus) sichtbar | UT3, IT1 | `UI <-> LED` | UI | `LED-Display`, `Button`, `LED` | Sprint 1✔️ | Hoch | Klar erkennbare Betriebszustände, Sicherheitsaspekt |
| R2.3 | Reaktionszeit beim Betätigen ≤ 500 ms | UT9, IT8 | `UI <-> PowerController` | UI, Steuerung/Logik, Aktuatoren | `Button`, `TouchController`, `TempController` | Sprint 3✔️ | Mittel | Komfortfunktion |
