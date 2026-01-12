
## 1. Ziel der Tests
Ziel der Tests ist die Verifikation und Validierung der Benutzerinteraktion, Reaktionszeiten und Timerfunktion des Induktionskochfelds. Die Tests sollen sicherstellen, dass:  

- Die UI reagiert innerhalb ≤100 ms auf Benutzeraktionen (R1.3)  
- Funktionstasten (z. B. „P“) reagieren innerhalb ≤500 ms (R2.3)  
- Temperaturanzeige, Leistungsstufen und Timeranzeige haben maximale Verzögerung ≤500 ms (R3.2, R5.2)  
- Timer kann von 1–20 Minuten eingestellt werden und steuert die Kochzone korrekt (R5.1)  
- Sicherheitsabschaltungen und UI-Feedback funktionieren zuverlässig  

---

## 2. Testarten und Abdeckung

### 2.1 Unit Tests
**Ziel:** Überprüfung einzelner Methoden der Steuerung/Logik, UI und Timerfunktionen.

**Beispiele:**  
- `readUserInput()` → Reaktionszeit ≤100 ms bei Leistungsstufenwahl (R1.3)  
- `pressPButton()` → Timer startet, Reaktionszeit ≤500 ms (R2.3)  
- `updateTimerDisplay()` → Anzeige reagiert ≤500 ms (R5.2)  

### 2.2 Integration Tests
**Ziel:** Überprüfung der Zusammenarbeit von UI, Steuerung/Logik, Timer und Aktuatoren.

**Beispiele:**  
- Benutzer wählt Leistungsstufe → Steuerung setzt Level → UI zeigt sofort, Temperaturanzeige ≤500 ms verzögert (R1.3, R3.2)  
- Timer auf 1–20 Minuten einstellen → Steuerung startet Countdown → Kochzone schaltet nach Ablauf ab, Timeranzeige reagiert ≤500 ms (R5.1, R5.2, R5.3)  
- Taste „P“ gedrückt → Timer startet → UI zeigt Countdown korrekt, Kochzone reagiert (R2.3, R5.2, R5.3)  

---

## 3. Teststrategie
- Kombination aus automatisierten Unit-Tests (JUnit) und manuellen Integrationstests  
- Iterative Tests nach Änderungen der UI-Reaktionslogik und Timersteuerung  
- Regressionstests nach Anpassungen der Sicherheitsabschaltungen  
- Testumgebung:  
  - Simulierte Benutzereingaben (Touch, Drehknopf, Tasten)  
  - Timer-Service zur Messung von Countdown-Funktion und Anzeigeverzögerungen  
  - Logging- und Timing-Tools zur Messung von UI- und Timer-Reaktionszeiten  

---

## 4. Testumfang

**In-Scope:**  
- UI-Reaktionszeiten (R1.3, R2.3, R3.2, R5.2)  
- Timerfunktion 1–20 Minuten und Abschaltung der Kochzone (R5.1, R5.2, R5.3)  
- Leistungsstufensteuerung inkl. Reaktionszeiten (R1.3)  
- Sicherheitsabschaltungen und UI-Feedback  

**Out-of-Scope:**  
- Hardwarefehler der Sensorik oder Aktuatoren  
- Langzeitverhalten der LEDs oder Schaltermechanismen  
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

[zu den Test](../../Testen)


## 6. Nachweis der abgeschlossenen Testfälle für Sprint 2

Alle im Sprint 2 definierten Testfälle wurden erfolgreich durchgeführt und abgeschlossen. Die Ergebnisse stimmen mit den geplanten Anforderungen überein.

| Testfall | Abgeschlossen | Bemerkung |
|----------|---------------|-----------|
| UT4 – UI-Reaktion bei verschmutzten Fingern | ✅ | Eingaben zuverlässig erkannt, Leistungsstufe korrekt angepasst |
| UT5 – Lebensdauer LED-Anzeige | ✅ | LED-Anzeige blieb ≥ 500 h stabil, keine Helligkeitsminderung |
| UT6 – Timer mit Selbstabschaltung | ✅ | Kochzone nach 10 Minuten zuverlässig deaktiviert, Display korrekt |
| UT7 – Schalterhaltbarkeit | ✅ | Ein-/Ausschalter überstand 100.000 Betätigungen ohne Defekt |
| IT4 – UI + verschmutzte Finger steuert Heizleistung | ✅ | Leistungsstufe korrekt erhöht, Display synchron |
| IT5 – Timerfunktion + Selbstabschaltung | ✅ | Timer und Boost-Funktion korrekt deaktiviert, Display zeigt Status |
| IT6 – Ein-/Ausschaltung inkl. Schalterhaltbarkeit | ✅ | Schalter funktionierte zuverlässig, Gerät schaltet ein/aus |

**Fazit:**  
- Alle Testfälle von Sprint 2 wurden erfolgreich abgeschlossen.  
- Die Requirements R1.4, R1.5, R2.5, R4.2 und R5.3 sind nachweislich erfüllt.  
- Keine offenen Fehler oder Blocker vorhanden.  

[zu den Test](../../Testen)

