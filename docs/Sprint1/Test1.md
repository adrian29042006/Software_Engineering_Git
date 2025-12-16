# Test
[Hier der Link zu den ganzen Testfällen](../../Testen)

# Testkonzept – Temperatursensor Induktionskochfeld

## 1. Ziel der Tests
Das Ziel der Tests ist die Verifikation und Validierung der Temperaturmessung und -regelung des Induktionskochfelds. Die Tests stellen sicher, dass:  

- Die Pfannentemperatur kontinuierlich korrekt erfasst wird (R3.1)  
- Die Steuerung der Leistungsstufen auf Basis der Temperaturdaten zuverlässig erfolgt (R1.1, R1.2)  
- Reaktionszeiten der UI bei Eingaben ≤100 ms (R1.3) und ≤500 ms bei Funktionstasten (R2.3) eingehalten werden  
- Sicherheitsrelevante Bedingungen (Überhitzung, Gerät ausschalten) erkannt und korrekt verarbeitet werden  
- Statusanzeigen in UI und Aktuatoren korrekt dargestellt werden  

---

## 2. Testarten und Abdeckung

### 2.1 Unit Tests
**Ziel:** Überprüfung einzelner Komponentenmethoden in Steuerung/Logik und Sensorik.

Beispielsweise getestet:  

- `readTemperature()` → liefert Temperaturwert in °C  
- `setPowerLevel(level)` → steuert Heizung basierend auf Leistungsstufe  
- `updateUIStatus()` → Anzeige der Temperatur und Leistungsstufe  
- Grenzwertprüfung der Temperatur → Notabschaltung bei Überschreitung  

### 2.2 Integration Tests
**Ziel:** Überprüfung der Zusammenarbeit von Sensorik, Steuerung, Sicherheitsmodul und UI.

Beispielsweise getestet:  

- Temperaturanstieg → Steuerung regelt Leistungsstufe → UI zeigt aktuelle Stufe + Temperatur  
- Überhitzung → Sicherheitsmodul löst Abschaltung aus → Aktuatoren stoppen Heizfeld → UI meldet Alarm  
- Benutzerbedienung (Tasten/Drehknopf/Touch) → Steuerung reagiert innerhalb ≤100 ms → Leistungsstufe angepasst  
- Simulation von Fehlwerten (z. B. Sensor defekt) → Sicherheitsmodul meldet Fehler → Zyklus gestoppt  

---

## 3. Teststrategie
- Kombination aus automatisierten Unit-Tests (JUnit für Steuerung/Logik) und manuellen Integrationstests  
- Iterative Tests nach Anpassungen der Temperatursensorlogik  
- Regressionstests nach Änderungen der UI oder Sicherheitsmodule  
- Testumgebung:  
  - Simulierte Temperaturwerte (Sensor-Simulator)  
  - Timer-Service zur Messung von Reaktionszeiten  
  - Logging- und Timing-Tools zur Prüfung der Sensorreaktionen und UI-Darstellung  

---

## 4. Testumfang

**In-Scope:**  
- Temperaturmessung (R3.1)  
- Steuerung der Leistungsstufen (R1.1, R1.2)  
- UI-Basisfunktionen: Tasten/Drehknopf/Touch (R1.2, R1.3, R2.1, R2.2, R2.3)  
- Sicherheitsabschaltung bei Überhitzung (Sicherheitsmodul)  
- Reaktionszeiten (≤100 ms für UI, ≤500 ms für Taste „P“)  

**Out-of-Scope:**  
- Hardwarefehler des Sensors  
- Langzeitverhalten der Heizelemente  
- Vakuum- und Sealing-Manager  
