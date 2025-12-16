
---

Umfang:

- Temperaturmessung mit Sensorik (R3.1)  
- Grundsteuerung der Leistungsstufen (R1.1, R1.2)  
- UI-Basisfunktion: Eingabe über Tasten/Drehknopf/Touch  
- Reaktionszeit der UI (R1.3, R2.3)  
- Sichtbare Statusanzeige (R2.2)  
- Ein-/Ausschaltung des Kochfelds (R4.1)
  

---

## Klassendiagramm

<img width="1920" height="1080" alt="press" src="https://github.com/user-attachments/assets/b1a5d5ff-f03f-4c97-82dc-3ba2704faf3f" />


---

## Zustandsdiagramm Knopfinteraktion


<img width="1920" height="1080" alt="EINAus-Schalter (1)" src="https://github.com/user-attachments/assets/12a1ecca-b7c3-4f6a-9e83-3d12051fd625" />


---

## Sequenzdiagramm


<img width="1920" height="1080" alt="Benutzer (1)" src="https://github.com/user-attachments/assets/1be04493-981c-49b9-b585-15f4b5358bcf" />


---

## Kommunikationsdiagramm

<img width="1920" height="1080" alt="Benutzer (2)" src="https://github.com/user-attachments/assets/72a17f76-2952-4ef4-9635-94c11f90f5a8" />

---

Schnittstellenübersicht Induktionskochfeld:

1. UI <-> PowerController
   - Steuerung der Leistungsstufen
   - Ein-/Aus-Funktion
   - Timersteuerung

2. PowerController <-> Heizelemente
   - Schalten der Kochzone
   - Temperaturregelung

3. UI <-> LED
   - Anzeige von Leistungsstufen, Sonderfunktionen, Timerzustand

4. TempSensor <-> PowerController
   - Temperaturüberwachung

5. TimerController <-> PowerController
   - Automatisches Abschalten nach Ablauf der Zeit

6. UI <-> Touchcontroller
   - Touch-Eingaben für Bedienung und Timer

7. TimerController <-> Heizelemente
   - Timer-basiertes Abschalten der Kochzone





