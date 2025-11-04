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

| **Requirement-ID** | **Kurzbeschreibung** | **Zugeordnete Komponente(n)** | **Test / Verifikation** |
|--------------------|----------------------|--------------------------------|------------------------|
| **R1.1** | 9 klar unterscheidbare Leistungsstufen | `PowerController`, `UIHandler`, `Heizelemente`| Unit-Test: Stufen 1–9 schalten korrekt |
| **R1.2** | Auswahl über Touch / Drehknopf / Tasten | `UIHandler` | UI-Test: Eingaben erkannt |
| **R1.3** | Reaktionszeit ≤ 100 ms | `UIHandler`, `PowerController`, `Heizelemente`| Performance-Test (Timing ≤100 ms) |
| **R3.1** | Temperatur in Pfanne wird kontinuierlich überwacht | `TempSensorReader`, `PowerController`, `Heizelemente` | Unit-Test: Sensorwerte plausibel |
| **R4.1** | Gerät verfügt über Ein-/Aus-Schalter | `UIHandler`, `PowerController`,  `Heizelemente` | Integrationstest: Ein/Aus-Zyklus |
| **R2.2** | Zustand der Taste sichtbar (Ein/Aus) | `UIHandler` | Sichtprüfung: LED/Display-Feedback |
| **R2.3** | Reaktionszeit beim Betätigen ≤ 500 ms | `UIHandler`, `PowerController`, `Heizelemente` | Reaktionszeitmessung |

---

## Klassendiagramm

<img width="1119" height="1269" alt="image" src="https://github.com/user-attachments/assets/73d98317-08e6-4edf-929f-2c90edf59d4d" />

---

## Zustandsdiagramm Knopfinteraktion

<img width="1920" height="1080" alt="EINAus-Schalter" src="https://github.com/user-attachments/assets/8fb90c5a-ca70-4152-8d4d-5a241abe46eb" />


---

## Sequenzdiagramm

![Kopie von Kopie von User](https://github.com/user-attachments/assets/481a4372-17d7-4f5b-9bb0-5e4d74e17226)

---

## Kommunikationsdiagramm



1. Benutzer → BenutzerInterface : einschalten()
2. BenutzerInterface → KochfeldController : handleEinschalten()
3. KochfeldController → Heizelement : startHeating()
4. Heizelement → KochfeldController : heatingStarted()
5. (Parallel / optional) FehlerÜberwachung → KochfeldController : checkError()
6. Wenn Fehler: KochfeldController → FehlerÜberwachung : getErrorStatus()
7. FehlerÜberwachung → KochfeldController : errorDetected()
8. KochfeldController → BenutzerInterface : zeigeFehler()


