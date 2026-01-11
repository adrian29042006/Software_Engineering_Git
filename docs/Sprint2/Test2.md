
## 1. Ziel der Tests
Ziel der Tests ist die Verifikation und Validierung der Temperaturmessung, Leistungsstufensteuerung, UI-Funktionen und Sicherheitsabschaltungen unter Berücksichtigung der neuen Anforderungen. Die Tests sollen sicherstellen, dass:

- Pfannentemperatur kontinuierlich korrekt überwacht wird (R3.1)  
- Leistungsstufen zuverlässig eingestellt und angezeigt werden (R1.1, R1.2, R1.4, R1.5)  
- UI reagiert auf Eingaben ≤100 ms (R1.3) und ≤500 ms bei Taste „P“ (R2.3)  
- Taste „P“ ist erkennbar und unterscheidet sich in Form/Farbe (R2.1, R2.4)  
- Timerfunktion läuft korrekt 10 Minuten und schaltet die Kochzone ab (R2.5, R5.3)  
- Ein-/Aus-Schalter hält ≥100.000 Betätigungen (R4.2)  
- Sicherheitsabschaltungen bei Überhitzung funktionieren korrekt  

---

## 2. Testarten und Abdeckung

### 2.1 Unit Tests
**Ziel:** Prüfung einzelner Methoden der Steuerung/Logik, Sensorik und UI-Komponenten.

**Beispiele:**  
- `readTemperature()` → Überprüfung der korrekten Temperaturerfassung (R3.1)  
- `setPowerLevel(level)` → Steuerung und Anzeige der Leistungsstufen, inkl. Reaktion bei verschmutzten Fingern (R1.1, R1.2, R1.4)  
- `startTimer(duration)` → Timer startet 10 Minuten korrekt, Countdown wird überwacht, Kochzone schaltet ab (R2.5, R5.3)  

### 2.2 Integration Tests
**Ziel:** Sicherstellen der Zusammenarbeit mehrerer Module (Sensorik, Steuerung, UI, Sicherheitsmodul, Aktuatoren).

**Beispiele:**  
- Temperaturanstieg → Steuerung regelt Leistungsstufe → UI zeigt aktuelle Stufe + Temperatur → Sicherheitsmodul greift bei Überhitzung ein (R3.1, R1.1, R5.3)  
- Benutzer bedient Taste „P“ mit verschmutzten Fingern → Steuerung reagiert korrekt, Timer startet → Kochzone wird nach 10 Minuten abgeschaltet (R1.4, R2.5, R5.3)  
- LED-Anzeige über 500 h simuliert → Anzeige bleibt zuverlässig, UI zeigt aktuelle Statusinformationen korrekt (R1.5)  

---

## 3. Teststrategie
- Kombination aus automatisierten Unit-Tests (JUnit für Steuerung/Logik) und manuellen Integrationstests  
- Iterative Tests nach Anpassungen der UI, Timer-Logik oder LED-Anzeige  
- Regressionstests nach Änderungen der Sicherheitsabschaltungen  
- Testumgebung:  
  - Simulierte Temperaturwerte und Benutzereingaben (Tasten, Touch, Drehknopf)  
  - Timer-Service zur Überprüfung der Countdown-Funktion  
  - Logging- und Timing-Tools zur Messung von Reaktionszeiten  
  - Simulation von LED-Belastung (R1.5)  

---

## 4. Testumfang

**In-Scope:**  
- Temperaturmessung (R3.1)  
- Leistungsstufensteuerung und UI-Reaktion (R1.1–R1.5, R2.1–R2.5)  
- Timerfunktion 10 Minuten und Abschaltung (R2.5, R5.3)  
- Ein-/Aus-Schalter auf Lebensdauer (R4.2)  
- Sicherheitsabschaltungen bei Überhitzung  

**Out-of-Scope:**  
- Langzeitverhalten der Heizelemente (außer LED-Belastung)  
- Hardwarefehler des Sensors oder Schaltermechanismus (außer Test der spezifizierten Lebensdauer)  
- Vakuum- und Sealing-Manager

 ## 5. Nachweis der abgeschlossenen Testfälle für Sprint 1

Alle im Sprint 1 definierten Testfälle wurden erfolgreich durchgeführt und abgeschlossen. Die Ergebnisse stimmen mit den geplanten Anforderungen überein.

| Testfall | Abgeschlossen | Bemerkung |
|----------|---------------|-----------|
| UT1 – Leistungsstufen: Untergrenze | ✅ | Leistungsstufe fiel nicht unter 1, System stabil |
| UT2 – Reaktionszeit UI-Eingabe | ✅ | UI reagierte innerhalb ≤ 100 ms, Leistungsstufe korrekt angepasst |
| UT3 – Temperaturmessung: stabiler Wert | ✅ | Sensorwerte konstant, keine Ausreißer |
| IT1 – UI-Eingabe steuert Heizleistung | ✅ | Eingabe korrekt verarbeitet, Heizleistung angepasst, Anzeige synchron |
| IT2 – Ein-/Ausschaltung des Systems | ✅ | System lässt sich zuverlässig ein- und ausschalten |
| IT3 – Temperaturregelung mit Anzeige | ✅ | Heizleistung regelkonform angepasst, System stabil |

**Fazit:**  
- Alle Testfälle von Sprint 1 wurden erfolgreich abgeschlossen.  
- Die Requirements R1.1, R1.2, R1.3, R2.2, R3.1 und R4.1 sind nachweislich erfüllt.  
- Keine offenen Fehler oder Blocker vorhanden.  

