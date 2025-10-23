# 🛠️ Pflichtenheft – Temperatursensor für ein Induktionskochfeld

> Ziel: Technische Umsetzung der Anforderungen aus dem Lastenheft

---

## 1. Digitale Leistungsstufen

Das System soll innerhalb von **Millisekunden** reagieren.  
Die Leistungsstufeneinstellung erfolgt über eine digitale Anzeige, **Drehknopf** oder **Tastenfeld**.

| Nr. | Typ | Beschreibung |
|-----|-----|---------------|
| R1.1 | Funktional | 9 klar unterscheidbare Leistungsstufen |
| R1.2 | Funktional | Auswahl der Leistungsstufen über Touch, Drehknopf oder Tasten |
| R1.3 | Nicht-Funktional | Reaktionszeit ≤ 100 ms |
| R1.4 | Nicht-Funktional | Zuverlässige Funktion auch bei verschmutzten Fingern |
| R1.5 | Nicht-Funktional | Lebensdauer der LED-Anzeige ≥ 500 h |

---

## 2. Power-Boost-Funktion

Das System bietet eine **Taste „P“** zur verfügung, die für „Power“ steht.  
Diese aktiviert eine doppelte Leistung für 10 Minuten und deaktiviert sich danach automatisch.  
Ein erneutes Drücken während der Aktivierungsphase deaktiviert die Funktion.

| Nr. | Typ | Beschreibung |
|-----|-----|---------------|
| R2.1 | Funktional | Taste „P“ muss klar erkennbar sein |
| R2.2 | Nicht-Funktional | Zustand der Taste (Ein/Aus) muss sichtbar sein |
| R2.3 | Nicht-Funktional | Reaktionszeit beim Betätigen ≤ 500 ms |
| R2.4 | Nicht-Funktional | Taste „P“ muss sich in Form oder Farbe von anderen unterscheiden |

---

## 3. Bratsensor-Automatik

Ein **Temperatursensor** misst kontinuierlich die Pfannenbodentemperatur und übermittelt die Daten an den Mikrocontroller.

| Nr. | Typ | Beschreibung |
|-----|-----|---------------|
| R3.1 | Funktional | Temperatur in der Pfanne wird kontinuierlich überwacht |
| R3.2 | Nicht-Funktional | Anzeigeverzögerung ≤ 500 ms |

---

## 4. Ein-/Aus-Schalter

| Nr. | Typ | Beschreibung |
|-----|-----|---------------|
| R4.1 | Funktional | Gerät verfügt über einen Ein-/Aus-Schalter |
| R4.2 | Nicht-Funktional | Schalter hält ≥ 100 000 Betätigungen ohne Defekt |

---

## 5. Timer

Die Timer-Funktion wird über **Tasten, Drehknopf oder Touchfeld** eingestellt.  
Der Mikrocontroller zählt die Zeit herunter und regelt bei Ablauf automatisch die Abschaltung der Kochzone.

| Nr. | Typ | Beschreibung |
|-----|-----|---------------|
| R5.1 | Funktional | Einstellbare Kochzeit von 1–20 Minuten |
| R5.2 | Nicht-Funktional | Timeranzeige reagiert mit max. 500 ms Verzögerung |
