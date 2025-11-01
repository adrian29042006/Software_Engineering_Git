# 🛠️ Pflichtenheft – Temperatursensor für ein Induktionskochfeld


---

## 1. Digitale Leistungsstufen

Implementierung von 9 Leistungsstufen, steuerbar über Drehregler oder LED-Touch-Display.

Jede Stufe entspricht einer festgelegten Heizleistung in Watt.

LED-Anzeige zeigt die aktuelle Leistungsstufe.

Mikrocontroller liest die Eingabe vom Drehregler/Touch-Display und steuert die Leistungsmodulation über das Induktionsfeld.


---

## 2. Power-Boost-Funktion

Taste „P“ aktiviert Boost.
Mikrocontroller setzt Boost-Leistung für 10 Minuten.

Nach Ablauf automatisch Rückkehr auf Stufe 9.

Bei erneutem Betätigen während Boost: sofortige Deaktivierung.

LED-Taste „P“ zeigt Boost-Aktiv oder Boost-Inaktiv an.


---

## 3. Bratsensor-Automatik

Temperaturfühler im Kochfeld (z. B. Infrarot- oder Thermoelement) misst Pfannenboden.

Mikrocontroller steuert Leistung, um konstante Temperatur zu halten.

Benutzer wählt über Touch-Display zwischen 3 Temperaturstufen (160 °C, 180 °C, 200 °C).

---

## 4. Ein-/Aus-Schalter

Ein- / Ausschalt-Taster

Mikrocontroller schaltet Steuerung und Induktionsmodul ein/aus

LED-Anzeige zeigt Ein- oder Aus-Zustand

---

## 5. Timer

Benutzer stellt Kochzeit über Drehregler oder Touch-Display ein (1–20 Minuten)

Mikrocontroller zählt die Zeit herunter

Nach Ablauf schaltet Induktionsfeld aus und signalisiert Ende (akustisch oder LED)



