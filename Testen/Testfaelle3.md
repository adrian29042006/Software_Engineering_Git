# Sprint 3 – Testfälle

## Projektinformationen
- Projekt: Induktionskochfeld
- Sprint: 3
- Abgedeckte Requirements: R1.1, R1.2, R1.3, R1.4, R1.5, R2.2, R2.3, R2.4, R2.5, R3.1, R3.2, R4.1, R4.2, R5.1, R5.2, R5.3

---

## 🔹 Unit-Tests

**UT7 – Sensorwert innerhalb normaler Temperatur (R3.1)**  
- Ziel: Prüfen, ob der Temperatursensor stabile Werte liefert  
- Ausgangszustand: Gerät = EIN, Topf leer / Wasser / Öl  
- Eingabe: Sensorwert variiert zwischen 20–100 °C  
- Erwartete Reaktion: Temperaturwert korrekt übernommen, keine Ausreißer  
- Klasse: TempSensorReader  
- Requirement: R3.1

**UT8 – Sensorwert außerhalb Grenzbereich (R3.1, R2.5, R5.3 indirekt)**  
- Ziel: Prüfen, ob bei Grenzwerten Sicherheitsmaßnahmen greifen  
- Ausgangszustand: Gerät = EIN, Leistungsstufe = 5  
- Eingabe: Sensor meldet kritische Temperatur  
- Erwartete Reaktion: System reagiert korrekt, ggf. Abschaltung  
- Klasse: TempSensorReader / SafetyController  
- Requirement: R3.1, R2.5, R5.3

**UT9 – Sensor liefert fehlerhafte Werte (HW-Fehler) (R3.1, R2.5, R5.3 indirekt)**  
- Ziel: Prüfen, ob fehlerhafte Sensorwerte korrekt erkannt und Sicherheitsmodus aktiviert wird  
- Ausgangszustand: Gerät = EIN  
- Eingabe: Sensorwert fehlerhaft  
- Erwartete Reaktion: Sicherheitsabschaltung aktiviert  
- Klasse: TempSensorReader / SafetyController  
- Requirement: R3.1, R2.5, R5.3

---

## 🔹 Integrationstests (3 Tests)

**IT7 – Sensor + Kochfeldsteuerung normale Kommunikation (R3.1, R1.1, R1.2)**  
- Ziel: Prüfen der normalen Funktion der Sensor-Steuerung-Kombination  
- Ausgangszustand: Gerät = EIN, Leistungsstufe = 3  
- Eingabe: Topf auf Kochzone, Sensor meldet Temperatur  
- Erwartete Reaktion: Leistungsstufe korrekt angepasst, Anzeige aktualisiert  

**IT8 – Sensor + Kochfeldsteuerung Ausfall Sensor (R3.1, R2.5, R5.3)**  
- Ziel: Prüfen des Sicherheitsverhaltens bei Sensorausfall  
- Ausgangszustand: Gerät = EIN, Leistungsstufe = 5  
- Eingabe: Sensor fällt aus  
- Erwartete Reaktion: Kochzone abgeschaltet, Sicherheitsmodus aktiviert  

**IT9 – Sensor + Kochfeldsteuerung Grenzwerttemperatur (R3.1, R1.1, R2.5, R5.3)**  
- Ziel: Prüfen der Reaktion bei Grenzwerttemperaturen  
- Ausgangszustand: Gerät = EIN, Leistungsstufe = 5  
- Eingabe: Temperatur erreicht Grenzwert  
- Erwartete Reaktion: Leistung angepasst oder abgeschaltet, Anzeige korrekt  
