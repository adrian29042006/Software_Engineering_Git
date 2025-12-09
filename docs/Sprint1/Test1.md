***Testfälle auf Modulebene***

## Testfall 1: Sensorwert innerhalb normaler Temperatur
Vorbedinung: Sensor ist kalibriert, Kochfeld ist eingeschaltet, Temerpatur auf 100°C eingestellt.
Aktion: Sensor liest aktuellen Temperaturwert
Erwartetes Ergebnis: Sensorwert soll mit maximal 3°C Abweichung den Sollwert ensprechen
Nachbedingung: Sensor leifert korrekte Werte, Kochfeld reagiert normal auf Steuerung

##Testfall 2: Sensorwert außerhalb Grenzbereich
Vorbedingung: Sensor ist kaliriert, Kochfeld eingeschaltet, Extremteperatur 300°C simuliert
Aktion: Sensor liest aktuellen Temperaturwert
Erwartetes Ergebnis: Sensor meldet Fehlercode
Nachbedingung; Kochfeld schaltet ggf. ab, Sicherheitsprotokoll aktiviert

##Testfall 3: Sensor liefert fehlerhafte Werte(Simulaiton von HW-Fehler)
Vorbedingung: Sensor simuliert Ausfall(Kommunikation wurde unterbrochen)
Aktion: Sensor liest Temperatur
Erwartetes Ergebnis: Sensor meldet Fehler, keine Falschen Temperaturen an Steuerung
Nachbedingung: Kochfeld geht in Sicherheitsmodus

---
