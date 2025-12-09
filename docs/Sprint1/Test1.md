# Testfälle auf Modulebene

***Testfall 1: Sensorwert innerhalb normaler Temperatur***
  - Vorbedinung: Sensor ist kalibriert, Kochfeld ist eingeschaltet, Temerpatur auf 100°C eingestellt.
  - Aktion: Sensor liest aktuellen Temperaturwert
  - Erwartetes Ergebnis: Sensorwert soll mit maximal 3°C Abweichung den Sollwert ensprechen
 -  Nachbedingung: Sensor leifert korrekte Werte, Kochfeld reagiert normal auf Steuerung

***Testfall 2: Sensorwert außerhalb Grenzbereich***
- Vorbedingung: Sensor ist kaliriert, Kochfeld eingeschaltet, Extremteperatur 300°C simuliert
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
