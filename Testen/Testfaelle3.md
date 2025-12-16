# Sprint 3 – Testfälle

## Projektinformationen
- Projekt: Induktionskochfeld
- Sprint: 3
- Abgedeckte Requirements: R1.3, R2.3, R3.2, R5.1, R5.2

---

## 🔹 Unit-Tests

**UT8 – Reaktionszeit Steuerung (R1.3)**  
- Ziel: Prüfen, ob die Steuerung auf Eingaben ≤ 100 ms reagiert  
- Ausgangszustand:
    - Gerät = EIN
    - Leistungsstufe = 3
- Eingabe:
    - Leistungsstufe ändern (Taste/Drehknopf/Touch)
- Erwartete Reaktion:
    - Steuerung reagiert innerhalb ≤ 100 ms
- Klasse: PowerController
- Requirement: R1.3

**UT9 – Reaktionszeit UI (R2.3)**  
- Ziel: Prüfen, ob die UI auf Tasteneingaben ≤ 500 ms reagiert  
- Ausgangszustand:
    - Gerät = EIN
    - Leistungsstufe = 2
- Eingabe:
    - ButtonInput = „+“/„-“ mit normalem oder leicht verschmutztem Finger
- Erwartete Reaktion:
    - Leistungsstufe korrekt angepasst
    - Reaktionszeit ≤ 500 ms
- Klasse: UIHandler
- Requirement: R2.3

**UT10 – Anzeigeverzögerung (R3.2)**  
- Ziel: Prüfen, ob Anzeigeänderungen innerhalb ≤ 500 ms sichtbar werden  
- Ausgangszustand:
    - Gerät = EIN
    - Leistungsstufe = 3
- Eingabe:
    - Leistungsstufe ändern, Timer starten/stoppen
- Erwartete Reaktion:
    - Anzeige zeigt Änderungen innerhalb ≤ 500 ms
- Klasse: Display
- Requirement: R3.2

---

## 🔹 Integrationstests

**IT7 – Timer einstellen (R5.1, R5.2)**  
- Ziel: Prüfen, ob Timer korrekt auf 1–20 Minuten eingestellt werden kann und Anzeige max. 500 ms Verzögerung hat  
- Ausgangszustand:
    - Gerät = EIN
    - Timer = 5 Minuten
- Eingabe:
    - Timer ändern auf 1–20 Minuten
- Erwartete Reaktion:
    - Timer wird korrekt eingestellt
    - Timeranzeige reagiert innerhalb 500 ms
- Beteiligte Komponenten:
    - UIHandler → Timer → Display
- Requirement: R5.1, R5.2

**IT8 – Schnelle Bedienung Leistungsstufe + Anzeige (R1.3, R2.3, R3.2)**  
- Ziel: Prüfen von Steuerungs- und UI-Reaktionszeiten inkl. Anzeigeverzögerung  
- Ausgangszustand:
    - Gerät = EIN
    - Leistungsstufe = 3
- Eingabe:
    - Mehrfache schnelle Eingaben (Tasten/Drehknopf)
- Erwartete Reaktion:
    - Steuerung reagiert ≤ 100 ms
    - UI reagiert ≤ 500 ms
    - Anzeige aktualisiert sich ≤ 500 ms
- Beteiligte Komponenten:
    - UIHandler → PowerController → Display
- Requirement: R1.3, R2.3, R3.2

**IT9 – Timer + Leistungsstufe kombiniert (R1.3, R2.3, R3.2, R5.1, R5.2)**  
- Ziel: Prüfen der korrekten Funktion bei gleichzeitiger Bedienung von Timer und Leistungsstufe  
- Ausgangszustand:
    - Gerät = EIN
    - Leistungsstufe = 2
    - Timer = 10 Minuten
- Eingabe:
    - Leistungsstufe ändern
    - Timer starten/stoppen
- Erwartete Reaktion:
    - Steuerung ≤ 100 ms
    - UI ≤ 500 ms
    - Anzeige ≤ 500 ms
    - Timer korrekt eingestellt (1–20 Min)
    - Timeranzeige reagiert ≤ 500 ms
- Beteiligte Komponenten:
    - UIHandler → PowerController → Timer → Display
- Requirement: R1.3, R2.3, R3.2, R5.1, R5.2
