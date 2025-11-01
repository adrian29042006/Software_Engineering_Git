# 🧩 Traceability Matrix – Sprint 1  
**Projekt:** Induktionskochfeld – Temperaturregelung  
**Ziel:** Implementierung der Grundfunktionen (Sensorik, Leistungssteuerung, UI-Bedienung)

---

Umfang:

- Temperaturmessung mit Sensorik (R3.1)  
- Grundsteuerung der Leistungsstufen (R1.1, R1.2)  
- UI-Basisfunktion: Eingabe über Tasten/Drehknopf/Touch  
- Reaktionszeit der UI (R1.3, R2.3)  
- Sichtbare Statusanzeige (R2.2)  
- Ein-/Ausschaltung des Kochfelds (R4.1)
  
---

## 📋 Traceability Matrix

| **Requirement-ID** | **Kurzbeschreibung** | **Zugeordnete Komponente(n)** | **Design-Element(e)** | **Test / Verifikation** |
|--------------------|----------------------|--------------------------------|------------------------|--------------------------|
| **R1.1** | 9 klar unterscheidbare Leistungsstufen | `PowerController`, `UIHandler` | Funktion `setPowerLevel(level)`, Enum `PowerLevel` | Unit-Test: Stufen 1–9 schalten korrekt |
| **R1.2** | Auswahl über Touch / Drehknopf / Tasten | `UIHandler` | Eventhandler `onInputChange()` | UI-Test: Eingaben erkannt |
| **R1.3** | Reaktionszeit ≤ 100 ms | `UIHandler`, `PowerController` | ISR-basiertes Event-Handling, Scheduler-Loop | Performance-Test (Timing ≤100 ms) |
| **R3.1** | Temperatur in Pfanne wird kontinuierlich überwacht | `TempSensorReader`, `PowerController` | Funktion `readTemperature()`, Sensor-Loop | Unit-Test: Sensorwerte plausibel |
| **R4.1** | Gerät verfügt über Ein-/Aus-Schalter | `UIHandler`, `PowerController` | Zustandsmaschine (Idle ↔ Heating) | Integrationstest: Ein/Aus-Zyklus |
| **R2.2** | Zustand der Taste sichtbar (Ein/Aus) | `UIHandler` | Funktion `updateDisplay(status)` | Sichtprüfung: LED/Display-Feedback |
| **R2.3** | Reaktionszeit beim Betätigen ≤ 500 ms | `UIHandler` | Event-Callback → Display-Update | Reaktionszeitmessung mit Stopwatch |

---

## Klassendiagramm

<img width="819" height="751" alt="Kopie von User" src="https://github.com/user-attachments/assets/05dd5eb9-e8fa-4443-b0f5-9ed03908a764" />

---

## Zustandsdiagramm

<img width="956" height="726" alt="Kopie von User (1)" src="https://github.com/user-attachments/assets/29636f87-04c0-4e19-bc0e-90838addd052" />

---

## Sequenzdiagramm

![Kopie von Kopie von User](https://github.com/user-attachments/assets/481a4372-17d7-4f5b-9bb0-5e4d74e17226)

---
