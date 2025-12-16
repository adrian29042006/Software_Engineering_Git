***
# 🧪 Testfälle – Sprint 2
***

## Projektinformationen

- **Projekt:** Induktionskochfeld
- **Sprint:** 2
- **Abgedeckte Requirements:** R1.4, R1.5, R2.4, R2.5, R4.2, R5.3

***

## 🔹 Unit-Tests

***

### UT4 – UI-Reaktion bei verschmutzten Fingern (R1.4)

- **Ziel:**  
  Sicherstellen, dass Tasten/Touch auch bei leicht verschmutzten Fingern (Fett, Mehl) korrekt reagieren.

- **Ausgangszustand:**
  - Gerät = EIN
  - Leistungsstufe = 3

- **Ereignis:**  
  - Kurzes Drücken der „+“-Taste bei verschmutzten Fingern

- **Eingabe:**
  - ButtonInput = „+“

- **Erwartete Reaktion:**
  - Leistungsstufe erhöht sich auf 4
  - Eingabe wird zuverlässig erkannt

- **Klasse:** UIHandler  
- **Requirement:** R1.4

***

### UT5 – Lebensdauer LED-Anzeige (R1.5)

- **Ziel:**  
  Prüfen, ob LED-Anzeige ≥ 500 h ohne merkliche Helligkeitsminderung leuchtet.

- **Ausgangszustand:**
  - Gerät = EIN
  - Display = aktiv

- **Ereignis:**  
  - Dauerbetrieb simulieren (500 h äquivalent in Testsimulation)

- **Erwartete Reaktion:**
  - LED bleibt stabil und leuchtet konstant
  - Keine Ausfälle oder Helligkeitsminderungen

- **Klasse:** LED_Display  
- **Requirement:** R1.5

***

### UT6 – Timer mit Selbstabschaltung (R2.5, R5.3)

- **Ziel:**  
  Timer läuft 10 Minuten und deaktiviert Kochzone selbstständig.

- **Ausgangszustand:**
  - Gerät = EIN
  - Boost-Funktion = aktiv

- **Ereignis:**  
  - Timer startet

- **Eingabe:**
  - Timer läuft auf 0 Minuten herunter

- **Erwartete Reaktion:**
  - Kochzone wird abgeschaltet
  - Display zeigt abgeschalteten Status
  - Funktion deaktiviert sich selbstständig

- **Klasse:** TimerController  
- **Requirement:** R2.5, R5.3

***

### UT7 – Schalterhaltbarkeit (R4.2)

- **Ziel:**  
  Prüfen, dass Ein-/Ausschalter ≥ 100.000 Betätigungen ohne Defekt übersteht.

- **Ausgangszustand:**
  - Gerät = AUS

- **Ereignis:**  
  - Simulierte 100.000 Schaltvorgänge

- **Eingabe:**
  - PowerButton = gedrückt

- **Erwartete Reaktion:**
  - Gerät schaltet zuverlässig ein/aus
  - Keine Fehlfunktionen

- **Klasse:** PowerController  
- **Requirement:** R4.2

***

## 🔹 Integrationstests

***

### IT4 – UI + verschmutzte Finger steuert Heizleistung

- **Ziel:**  
  Prüfen der Interaktion zwischen UI, PowerController und Hardware bei verschmutzten Fingern.

- **Ausgangszustand:**
  - Gerät = EIN
  - Leistungsstufe = 2

- **Ereignis:**  
  - Benutzer drückt „+“ bei leicht verschmutzten Fingern

- **Erwartete Reaktion:**
  - UI erkennt Eingabe
  - Leistungsstufe erhöht sich auf 3
  - Heizleistung angepasst
  - Display korrekt aktualisiert

- **Beteiligte Komponenten:** UIHandler → PowerController → HardwareAbstraction → Display  
- **Requirement:** R1.4

***

### IT5 – Timerfunktion + Selbstabschaltung

- **Ziel:**  
  Test des Zusammenspiels zwischen TimerController, PowerController und Display.

- **Ausgangszustand:**
  - Gerät = EIN
  - Boost-Funktion = aktiv

- **Ereignis:**  
  - Timer läuft auf 0 Minuten herunter

- **Erwartete Reaktion:**
  - Kochzone wird abgeschaltet
  - Boost-Funktion deaktiviert sich
  - Display zeigt abgeschalteten Status

- **Beteiligte Komponenten:** TimerController → PowerController → Display  
- **Requirement:** R2.5, R5.3

***

### IT6 – Ein-/Ausschaltung inkl. Schalterhaltbarkeit

- **Ziel:**  
  Integrationstest für Ein-/Ausschaltung und Belastungstest des Schalters.

- **Ausgangszustand:**
  - Gerät = AUS

- **Ereignis:**  
  - 100.000 simulierte Schaltvorgänge

- **Erwartete Reaktion:**
  - Gerät schaltet zuverlässig ein/aus
  - Keine Fehlfunktionen oder Defekte

- **Beteiligte Komponenten:** UIHandler → PowerController → HardwareAbstraction → Display  
- **Requirement:** R4.2

***

