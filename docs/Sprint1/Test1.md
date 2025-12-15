# Test

## 1. Ziel des Tests
Das Ziel des Tests ist die Verifikation und Validierung des Induktionskochfeldes hinsichtlich funktionaler Korrektheit, Benutzerfreundlichkeit sowie robuster Systemrekation auf externe und interne Eingaben. Die Tests stellen sicher, dass:
- Temperaturmessung (R3.1):
Prüfen, ob der Sensor Temperatur korrekt misst (leer/voll, kaltes Wasser, verschiedene Topfpositionen/Materialien) und stabil bleibt.​
- Grundsteuerung Leistungsstufen (R1.1, R1.2):
Sicherstellen, dass jede Stufe die erwartete Leistung liefert, beim Hoch-/Herunterschalten keine Sprünge auftreten und Min/Max-Stufe sinnvoll funktionieren.​
- UI-Basisfunktion (Tasten/Drehknopf/Touch):
Testen, ob Eingaben zuverlässig erkannt werden (auch bei nassen Fingern) und die richtige Stufe aktiviert wird, auch im Sperrmodus.​
- Reaktionszeit der UI (R1.3, R2.3):
Messen, wie schnell Eingaben verarbeitet werden und ob das System bei schnellen Tastendrücken oder Topfwechsel nicht hängt.​
- Sichtbare Statusanzeige (R2.2):
Prüfen, dass Leistungsstufe, Betriebszustand (Ein/Aus, Topf erkannt, Restwärme) klar angezeigt und unter verschiedenen Lichtverhältnissen lesbar sind.​
- Ein-/Ausschaltung (R4.1):
Validieren, dass Ein-/Ausschalttaste zuverlässig funktioniert, nach Stromausfall nicht automatisch einschaltet und im Sperrmodus noch abschalten kann.

## 2. Testarten und Abdeckung

## 2.1 Unit‑Test (Komponenten-/Modultest)

- **Temperaturmessung (R3.1)**  
  Prüfen, ob der Sensor korrekte und stabile Temperaturwerte liefert (leer, Wasser, Öl, schnelle Änderungen).

- **Grundsteuerung Leistungsstufen (R1.1, R1.2)**  
  Jede Leistungsstufe aktiviert die erwartete Heizleistung; Rampen beim Hoch‑/Herunterschalten funktionieren ohne Sprünge.

- **Reaktionszeit der UI (R1.3, R2.3)**  
  Eingabe (Taste/Drehknopf/Touch) führt innerhalb definiertem Zeitlimit zur Zustandsänderung im Steuermodul.

## 2.2 Usability‑Test (Benutzerfreundlichkeit)

- **UI‑Basisfunktion (Tasten/Drehknopf/Touch)**  
  Bedienelemente sind intuitiv, funktionieren zuverlässig (auch bei nassen Fingern) und vermeiden unbeabsichtigte Eingaben.

- **Sichtbare Statusanzeige (R2.2)**  
  Leistungsstufe, Betriebszustand (Ein/Aus, Topf erkannt, Restwärme) sind klar, verständlich und gut lesbar.

- **Ein‑/Ausschaltung (R4.1)**  
  Ein‑/Ausschalttaste ist leicht zu finden und zu bedienen, auch im Sperrmodus (z. B. Kindersicherung).

## 2.3 Black‑Box‑/Systemtest (Gesamtsystem)

- **Temperaturmessung + Regelung (R3.1)**  
  System hält die eingestellte Solltemperatur stabil, reagiert korrekt auf Topfwechsel und bleibt im sicheren Bereich.

- **Grundsteuerung + UI (R1.1, R1.2, R1.3, R2.3)**  
  Eingabe über UI führt zu korrekter Leistungsstufe, Reaktionszeit liegt im akzeptablen Bereich, auch bei wiederholten Eingaben.

- **Sichtbare Statusanzeige (R2.2)**  
  Anzeige zeigt aktuelle Leistung und Zustände (Topf erkannt, Fehler, Restwärme) korrekt und zeitnah an.

- **Ein‑/Ausschaltung (R4.1)**  
  System lässt sich zuverlässig ein‑/ausschalten, bleibt nach Stromausfall aus und kann im Sperrmodus noch abgeschaltet werden.













# Testfälle auf Modulebene

***Testfall 1: Sensorwert innerhalb normaler Temperatur***
  - Vorbedinung: Sensor ist kalibriert, Kochfeld ist eingeschaltet, Temerpatur auf 100°C eingestellt.
  - Aktion: Sensor liest aktuellen Temperaturwert
  - Erwartetes Ergebnis: Sensorwert soll mit maximal 3°C Abweichung den Sollwert ensprechen
 -  Nachbedingung: Sensor leifert korrekte Werte, Kochfeld reagiert normal auf Steuerung

***Testfall 2: Sensorwert außerhalb Grenzbereich***
- Vorbedingung: Sensor ist kalibriert, Kochfeld eingeschaltet, Extremteperatur 300°C simuliert
- Aktion: Sensor liest aktuellen Temperaturwert
- Erwartetes Ergebnis: Sensor meldet Fehlercode
- Nachbedingung; Kochfeld schaltet ggf. ab, Sicherheitsprotokoll aktiviert

***Testfall 3: Sensor liefert fehlerhafte Werte(Simulaiton von HW-Fehler)***
- Vorbedingung: Sensor simuliert Ausfall(Kommunikation wurde unterbrochen)
- Aktion: Sensor liest Temperatur
- Erwartetes Ergebnis: Sensor meldet Fehler, keine Falschen Temperaturen an Steuerung
- Nachbedingung: Kochfeld geht in Sicherheitsmodus


---

# Testfälle auf Integrationsebene

***Testfall 4: Sensor + Kochfeldsteuerung normale Kommunikation***
  - Vorbedingung: Sensor ist kalibriert, Steuerung des Kochfeldes ist aktiv
  - Aktion: Steuerung fragt Temperatur ab, Steuerung passt Heizleistung an
  - Erwartetes Ergebnis: Temperatur korrekt an Steuerung übertragen, Heizleistng angepasst
  - Nachbedingung: Kochfeld reagiert korrekt auf aktuellen Temperatur

***Testfall 5: Sensor + Kochfeldsteuerung Ausfall Sensor***
  - Vorbedingung: Sensor fällt während Betrieb aus
  - Aktion: Steuerung fordert Temperaturwert an
  - Erwartetes Ergebnis: Steuerung erkennt Kommunikationsfehler, gibt Fehler aus
  - Nachbedingung: Kochfeld schaltet ggf. in Sicherheitsmodus, Warnmeldung angezeigt

***Testfall 6: Sensor + Kochfeldsteuerung Grenzwerttemperatur***
  - Vorbedinung: Kochfeld auf maximale Temperatur eingestellt(z.b. 300°C). Sensor ist aktiv
  - Aktion: Steuerung liest Sensorwert, prüft Soll/ist-Differenz
  - Erwartetes Ergebnis: Steuerung begrenz Heizleistung, überschreitet max. Temperatur nicht
  - Nachbedingung: Kochfeld erreicht max. Temperatur, überschreitet Sicherheitsgrenze nicht
