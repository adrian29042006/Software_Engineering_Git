***
# 🧪 Testfälle – Sprint 1
***

## Projektinformationen

- **Projekt:** Induktionskochfeld
- **Sprint:** 1
- **Abgedeckte Requirements:** R1.1, R1.2, R1.3, R2.2, R2.3, R3.1, R4.1

***

## 🔹 Unit-Tests

***

### UT1 – Leistungsstufen: Untergrenze

- **Ziel:**  
  Sicherstellen, dass die Leistungsstufe nicht unter die minimale Stufe (1) fällt.

- **Ausgangszustand:**
  - Leistungsstufe = 1
  - Gerät = EIN
  - Topf erkannt = TRUE

- **Ereignis:**  
  - Benutzer drückt die „–“-Taste

- **Eingabe:**
  - ButtonInput = „–“

- **Erwartete Reaktion:**
  - Leistungsstufe bleibt bei 1
  - Keine Abschaltung
  - Keine Fehlermeldung

- **Erwarteter Folgezustand:**
  - Leistungsstufe = 1
  - Gerät weiterhin aktiv

- **Klasse:** PowerController  
- **Requirement:** R1.1, R1.2

***

### UT2 – Reaktionszeit UI-Eingabe

- **Ziel:**  
  UI-Eingaben werden innerhalb von ≤ 100 ms verarbeitet.

- **Ausgangszustand:**
  - Gerät = EIN
  - Leistungsstufe = 3

- **Ereignis:**  
  - Kurzes Drücken der „+“-Taste

- **Eingabe:**
  - ButtonInput = „+“

- **Erwartete Reaktion:**
  - Leistungsstufe = 4
  - Reaktionszeit ≤ 100 ms

- **Klasse:** UIHandler  
- **Requirement:** R1.3

***

### UT3 – Temperaturmessung: stabiler Wert

- **Ziel:**  
  Sicherstellen, dass der Temperatursensor stabile Messwerte liefert.

- **Ausgangszustand:**
  - Gerät = EIN
  - Leistungsstufe = 5
  - Topf mit Wasser

- **Eingabe:**
  - Sensorwert = 78 °C

- **Erwartete Reaktion:**
  - Korrekte Übernahme des Temperaturwertes
  - Keine Messsprünge

- **Klasse:** TempSensorReader  
- **Requirement:** R3.1

***

## 🔹 Integrationstests

***

### IT1 – UI-Eingabe steuert Heizleistung

- **Ziel:**  
  Überprüfung des Zusammenspiels zwischen UI, Steuerlogik und Hardware.

- **Ausgangszustand:**
  - Gerät = EIN
  - Leistungsstufe = 2

- **Ereignis:**  
  - Benutzer drückt „+“

- **Erwartete Reaktion:**
  - UI erkennt Eingabe
  - PowerController erhöht Leistungsstufe
  - Heizleistung wird angepasst
  - Anzeige aktualisiert sich

- **Erwarteter Folgezustand:**
  - Leistungsstufe = 3
  - Heizspule aktiv

- **Beteiligte Komponenten:**  
  UIHandler → PowerController → HardwareAbstraction → Display

- **Requirement:** R1.1, R1.2, R2.2

***

### IT2 – Ein-/Ausschaltung des Systems

- **Ziel:**  
  Sicherstellen, dass das System zuverlässig ein- und ausgeschaltet werden kann.

- **Ausgangszustand:**
  - Gerät = AUS

- **Ereignis:**  
  - Benutzer drückt Ein-/Aus-Taste

- **Erwartete Reaktion:**
  - System startet
  - Anzeige aktiviert sich
  - Heizleistung bleibt aus

- **Erwarteter Folgezustand:**
  - Gerät = EIN
  - Leistungsstufe = 0

- **Requirement:** R4.1, R2.2

***

### IT3 – Temperaturregelung mit Anzeige

- **Ziel:**  
  Test der geschlossenen Regelkette.

- **Ausgangszustand:**
  - Gerät = EIN
  - Leistungsstufe = 6
  - Topf mit Wasser

- **Ereignis:**  
  - Temperatur steigt über Sollwert

- **Erwartete Reaktion:**
  - Heizleistung wird reduziert
  - Anzeige bleibt konsistent
  - System bleibt stabil

- **Requirement:** R3.1, R2.2

***
