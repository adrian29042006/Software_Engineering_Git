***
# 🧪 Testfälle – Sprint 2
***

## Projektinformationen

- **Projekt:** Induktionskochfeld
- **Sprint:** 2
- **Abgedeckte Requirements:** R1.1, R1.2, R1.4, R1.5, R2.2, R2.4, R2.5, R3.1, R4.1, R4.2, R5.3

***

## 🔹 Unit-Tests

***

### UT4 – Temperaturmessung: stabiler Wert (R3.1)

- **Ziel:**  
  Prüfen, ob der Temperatursensor unter verschiedenen Bedingungen korrekte und stabile Werte liefert.

- **Ausgangszustand:**
  - Gerät = EIN
  - Leistungsstufe = 5
  - Topf mit Wasser

- **Eingabe:**
  - Sensorwert = 80 °C

- **Erwartete Reaktion:**
  - Temperaturwert korrekt übernommen
  - Keine Sprünge oder Ausreißer

- **Klasse:** TempSensorReader  
- **Requirement:** R3.1

***

### UT5 – UI-Reaktion bei verschmutzten Fingern (R1.4)

- **Ziel:**  
  Eingaben werden auch bei leicht verschmutzten Fingern korrekt erkannt.

- **Ausgangszustand:**
  - Gerät = EIN
  - Leistungsstufe = 3

- **Eingabe:**
  - ButtonInput = „+“ mit fettiger/mehliger Hand

- **Erwartete Reaktion:**
  - Leistungsstufe erhöht sich korrekt
  - Reaktionszeit ≤ 100 ms

- **Klasse:** UIHandler  
- **Requirement:** R1.4

***

### UT6 – Timer mit Selbstabschaltung (R2.5, R5.3)

- **Ziel:**  
  Verifikation der zeitbasierten Abschaltung nach 10 Minuten.

- **Ausgangszustand:**
  - Gerät = EIN
  - Funktion „Boost“ gestartet
  - Timer = 10 Minuten

- **Eingabe:**  
  - Timer läuft ab

- **Erwartete Reaktion:**
  - Kochzone wird abgeschaltet
  - Funktion deaktiviert sich automatisch

- **Klasse:** PowerController / Timer  
- **Requirement:** R2.5, R5.3

***

## 🔹 Integrationstests

***

### IT4 – UI-Eingabe steuert Heizleistung inkl. verschmutzte Finger

- **Ziel:**  
  Test des Zusammenspiels von UI, Steuerlogik und Hardware bei verschmutzten Fingern.

- **Ausgangszustand:**
  - Gerät = EIN
  - Leistungsstufe = 2

- **Eingabe:**  
  - ButtonInput = „+“ mit leicht verschmutzten Fingern

- **Erwartete Reaktion:**
  - UI erkennt Eingabe korrekt
  - PowerController erhöht Leistungsstufe
  - Heizleistung passt sich an
  - Display aktualisiert sich

- **Beteiligte Komponenten:**  
  UIHandler → PowerController → HardwareAbstraction → Display

- **Requirement:** R1.2, R1.4, R2.2

***

### IT5 – Timerfunktion + Selbstabschaltung

- **Ziel:**  
  Prüfen des Zusammenspiels von Timer, PowerController und Anzeige bei Selbstabschaltung.

- **Ausgangszustand:**
  - Gerät = EIN
  - Boost-Funktion aktiviert
  - Timer = 10 Minuten

- **Eingabe:**  
  - Timer läuft ab

- **Erwartete Reaktion:**
  - Kochzone wird abgeschaltet
  - Funktion deaktiviert sich
  - Display zeigt korrekten Status

- **Beteiligte Komponenten:**  
  Timer → PowerController → Display

- **Requirement:** R2.5, R5.3

***

### IT6 – Ein-/Ausschaltung inkl. Schalterhaltbarkeit

- **Ziel:**  
  Integrationstest für Ein-/Ausschaltung und Schalterhaltbarkeit ≥ 100.000 Betätigungen.

- **Ausgangszustand:**
  - Gerät = AUS

- **Eingabe:**  
  - Benutzer drückt Ein-/Aus-Taste wiederholt

- **Erwartete Reaktion:**
  - Gerät startet und stoppt korrekt
  - Keine Fehlfunktionen nach ≥100.000 Betätigungen

- **Beteiligte Komponenten:**  
  UI → PowerController → HardwareAbstraction → Display

- **Requirement:** R4.1, R4.2

***
