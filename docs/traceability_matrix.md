# Traceability Matrix – Induktionskochfeld

## Funktionale Anforderungen

| Anforderungs-ID | Beschreibung | Komponenten | Testfälle / Bemerkungen | Zugeordnete Komponente(n) | Design Klassen | Sprint | Priorität | Begründung |
|-----------------|-------------|------------|-------------------------|---------------------------|----------------|--------|-----------|------------|
| R1.1 | 9 klar unterscheidbare Leistungsstufen | UI, Steuerung/Logik, Aktuatoren | UT1, IT1 | `UIHandler`, `PowerController`, `Heizelemente` | `LED-Display`, `Button`, `PowerManager`, `PowerSwitch` | Sprint 1✔️ | Hoch | Grundfunktion des Kochfelds; essenziell für Benutzerkontrolle |
| R1.2 | Auswahl der Leistungsstufen über Touch, Drehknopf oder Tasten | UI, Steuerung/Logik | UT2, IT1 | `UIHandler` | `Button`, `Touchcontroller` | Sprint 1✔️ | Hoch | Direkte Bedienbarkeit, zentrale Benutzerinteraktion |
| R2.1 | Taste „P“ muss klar erkennbar sein | UI | UT8, IT8 | `UIHandler` | `LED-Display`, `Button`, `LED` | Sprint 1✔️ | Mittel | Nutzer muss Sonderfunktion leicht finden, Sicherheit weniger kritisch |
| R2.4 | Taste „P“ muss sich in Form oder Farbe unterscheiden | UI | UT5, IT4 | `UIHandler` | `Button` | Sprint 2✔️ | Mittel | Ergonomie und intuitive Nutzung |
| R2.5 | Die Funktion muss 10 Minuten laufen und sich selbst deaktivieren | Steuerung/Logik, Sicherheitsmodul, Aktuatoren | UT6, IT5 | `PowerController`, `Heizelemente` | `TimerController`, `InductionCoil`, `TimerManager` | Sprint 2✔️ | Hoch | Sicherheitsfunktion gegen Überhitzung oder Brandrisiko |
| R3.1 | Temperatur in der Pfanne wird kontinuierlich überwacht | Sensorik, Steuerung/Logik | UT3, IT3, IT6 | `TempSensorReader`, `PowerController`, `Heizelemente` | `TimerController`, `TempController`, `TempSensor`, `InductionCoil`, `TimerController`, `TimerManager` | Sprint 1✔️ | Hoch | Grundvoraussetzung für effizientes und sicheres Kochen |
| R3.2 | Anzeigeverzögerung ≤ 500 ms | UI, Sensorik, Steuerung/Logik | UT10, IT8, IT9 | `UIHandler`, `PowerController` | `LED-Display`, `Mikrocontroller` | Sprint 3✔️ | Mittel | Komfort für den Benutzer, keine Sicherheitskritik |
| R4.1 | Gerät verfügt über einen Ein-/Aus-Schalter | UI, Steuerung/Logik, Aktuatoren | UT7, IT2 | `UIHandler`, `PowerController`, `Heizelemente` | `Button` | Sprint 1✔️ | Hoch | Grundlegende Ein-/Aus-Funktion, Sicherheitsaspekt |
| R4.2 | Schalter hält ≥ 100.000 Betätigungen ohne Defekt | UI, Aktuatoren | UT7, IT6 | `UIHandler` | `Button` | Sprint 2✔️ | Mittel | Langlebigkeit, Benutzerkomfort |
| R5.1 | Einstellbare Kochzeit von 1–20 Minuten | UI, Steuerung/Logik, Aktuatoren | IT7, IT9 | `UIHandler`, `Touchcontroller`, `Heizelemente` | `Button` | Sprint 3✔️ | Hoch | Kernfunktion für Zeitsteuerung beim Kochen |
| R5.2 | Timeranzeige reagiert mit max. 500 ms Verzögerung | UI, Steuerung/Logik | IT7, IT9 | `UIHandler`, `PowerController` | `LED-Display`, `Mikrocontroller` | Sprint 3✔️ | Mittel | Komfortfunktion, erleichtert Benutzerkontrolle |
| R5.3 | Zeit wird heruntergezählt und Kochzone abschalten | Steuerung/Logik, Sicherheitsmodul, Aktuatoren | UT6, IT5 | `PowerController`, `Heizelemente` | `TimerController`, `TempController`, `TempSensor`, `InductionCoil`, `TimerController`, `TimerManager` | Sprint 2✔️ | Hoch | Sicherheitsfunktion, verhindert Überkochen oder Brandgefahr |

## Nicht-funktionale Anforderungen

| Anforderungs-ID | Beschreibung | Komponenten | Testfälle / Bemerkungen | Zugeordnete Komponente(n) | Design Klassen | Sprint | Priorität | Begründung |
|-----------------|--------------|-------------|-------------------------|---------------------------|----------------|-------|-----------|------------|
| R1.3 | Reaktionszeit ≤ 100 ms | UI, Steuerung/Logik | UT8, IT8 | `UIHandler`, `PowerController`, `Heizelemente` | `Button`, `Touchcontroller`, `Mikrocontroller` | Sprint 3✔️ | Mittel | Benutzerfreundlichkeit und direkte Rückmeldung |
| R1.4 | Zuverlässige Funktion bei verschmutzten Fingern | UI, Steuerung/Logik | UT4, IT4 | `UIHandler` | `Button`, `Touchcontroller` | Sprint 2✔️ | Mittel | Ergonomie, Bedienkomfort, keine Sicherheitskritik |
| R1.5 | Lebensdauer der LED-Anzeige ≥ 500 h | UI | UT5 | `UIHandler`, `PowerController` | `LED-Display`, `Button`, `LED`, `Touchcontroller` | Sprint 2✔️ | Niedrig | Wartungsfreundlichkeit, keine direkte Sicherheitsrelevanz |
| R2.2 | Zustand der Taste (Ein/Aus) muss sichtbar sein | UI | UT3, IT1 | `UIHandler` | `LED-Display`, `Button`, `LED` | Sprint 1✔️ | Hoch | Klar erkennbare Betriebszustände, Sicherheitsaspekt |
| R2.3 | Reaktionszeit beim Betätigen ≤ 500 ms | UI, Steuerung/Logik | UT9, IT8 | `UIHandler`, `PowerController`, `Heizelemente` | `Button`, `TouchController`, `TempController` | Sprint 3✔️ | Mittel | Komfortfunktion, keine direkte Sicherheitskritik |
