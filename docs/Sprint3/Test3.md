
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


