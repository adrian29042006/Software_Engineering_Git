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

--- 

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

---
## 3. Teststrategie
### Automatisierte Tests

- Unit‑Tests für Temperaturmessung (Sensorik), Leistungsstufen und UI‑Logik werden automatisiert (z. B. mit Testframework).  
- Laufen in der CI‑Pipeline bei jedem Commit, um schnelle Rückmeldung zu geben.

### Manuelle Tests

- Usability‑Tests: Bedienung (Tasten/Drehknopf/Touch), Lesbarkeit der Anzeige, Ein‑/Ausschaltung.  
- Systemtests: Verhalten bei Topfwechsel, Fehlerfälle, Restwärme, Kindersicherung.

### Iterative Tests

- Nach jeder Inkrementierung (neue Regelung, UI‑Änderung) werden Unit‑ und Systemtests erneut ausgeführt.  
- Sicherstellung, dass neue Funktionen korrekt integriert sind und Fehler früh erkannt werden.

### Regressionstests

- Definiertes Set kritischer Systemtests (Leistungsstufen, Temperaturstabilität, Statusanzeigen, Ein‑/Ausschaltung) wird regelmäßig wiederholt.  
- Ziel: Bestehende Funktionen bleiben stabil, auch nach Codeänderungen.

---

## 4. Testumfang

### In Scope

- Temperaturmessung mit Sensorik (R3.1)  
  Prüfung der Temperaturerfassung bei verschiedenen Lasten (leer, Wasser, Öl) und Topfpositionen/Materialien.

- Grundsteuerung der Leistungsstufen (R1.1, R1.2)  
  Funktion und Zuordnung der Leistungsstufen, Rampen beim Hoch-/Herunterschalten, Min-/Max‑Verhalten.

- UI‑Basisfunktionen (Tasten/Drehknopf/Touch)  
  Zuverlässige Eingabe, korrekte Zuordnung zur Leistungsstufe, Funktion im Sperrmodus.

- Reaktionszeit der UI (R1.3, R2.3)  
  Reaktionszeit auf Eingaben und Zustandsänderungen (z. B. Topf erkannt/verloren).

- Sichtbare Statusanzeige (R2.2)  
  Anzeige von Leistungsstufe, Betriebszustand (Ein/Aus, Topf erkannt, Restwärme, Fehler) und Lesbarkeit.

- Ein‑/Ausschaltung des Kochfelds (R4.1)  
  Funktion der Ein‑/Ausschalttaste, Verhalten nach Stromausfall und im Sperrmodus.

### Out of Scope

- Energieeffizienz‑Messungen (z. B. kWh‑Verbrauch pro Kochvorgang).  
- Langzeitstabilität über mehrere Monate oder 1000+ Betriebsstunden.  
- Funktion mit nicht induktionsfähigen Kochgeschirr (z. B. Aluminium, Glas).  
- Netzwerkkommunikation, App‑Steuerung oder Cloud‑Funktionen.  
- Mechanische Haltbarkeit (z. B. Kratzer, Tropffestigkeit, Reinigung).  
- EMV‑ und Sicherheitszertifizierungen (z. B. CE, EMC, Überhitzungsschutz nach Norm).
