# Test

## 1. Ziel des Tests
Das Ziel des Tests ist die Verifikation und Validierung des Induktionskochfeldes hinsichtlich funktionaler Korrektheit, Benutzerfreundlichkeit sowie robuster Systemreaktion auf externe und interne Eingaben. Die Tests stellen sicher, dass:

- Temperaturmessung (R3.1):  
  Prüfen, ob der Sensor Temperatur korrekt misst (leer/voll, kaltes Wasser, verschiedene Topfpositionen/Materialien) und stabil bleibt.

- Grundsteuerung Leistungsstufen (R1.1, R1.2):  
  Sicherstellen, dass jede Stufe die erwartete Leistung liefert, beim Hoch-/Herunterschalten keine Sprünge auftreten und Min/Max-Stufe sinnvoll funktionieren.

- UI-Basisfunktion (Tasten/Drehknopf/Touch):  
  Testen, ob Eingaben zuverlässig erkannt werden (auch bei nassen Fingern) und die richtige Stufe aktiviert wird, auch im Sperrmodus.

- Reaktionszeit der UI (R1.3, R2.3):  
  Messen, wie schnell Eingaben verarbeitet werden und ob das System bei schnellen Tastendrücken oder Topfwechsel nicht hängt.

- Sichtbare Statusanzeige (R2.2):  
  Prüfen, dass Leistungsstufe, Betriebszustand (Ein/Aus, Topf erkannt, Restwärme) klar angezeigt und unter verschiedenen Lichtverhältnissen lesbar sind.

- Ein-/Ausschaltung (R4.1):  
  Validieren, dass Ein-/Ausschalttaste zuverlässig funktioniert, nach Stromausfall nicht automatisch einschaltet und im Sperrmodus noch abschalten kann.

- Zuverlässigkeit bei verschmutzten Fingern (R1.4):  
  Eingaben müssen auch bei leicht verschmutzten Fingern (Fett, Mehl) zuverlässig erkannt werden.

- Lebensdauer der LED-Anzeige (R1.5):  
  Die LED-Anzeige muss mindestens 500 h kontinuierlich leuchten, ohne merkliche Helligkeitsminderung oder Ausfall.

- Unterscheidbare Taste „P“ (R2.4):  
  Die Taste „P“ (z. B. für Pause/Power) muss sich optisch (Form oder Farbe) deutlich von anderen Tasten unterscheiden.

- Funktion mit Selbstabschaltung (R2.5):  
  Eine definierte Funktion (z. B. Boost, Timer) muss 10 Minuten laufen und sich danach selbstständig deaktivieren.

- Haltbarkeit des Schalters (R4.2):  
  Der Ein-/Ausschalter muss ≥ 100 000 Betätigungen ohne Defekt überstehen.

- Zeitbasierte Abschaltung (R5.3):  
  Eine Zeitfunktion (z. B. Timer) muss die Zeit korrekt herunterzählen und die Kochzone am Ende sicher abschalten.

---

## 2. Testarten und Abdeckung

### 2.1 Unit‑Test (Komponenten-/Modultest)

- Temperaturmessung (R3.1)  
  Prüfen, ob der Sensor korrekte und stabile Temperaturwerte liefert (leer, Wasser, Öl, schnelle Änderungen).

- Grundsteuerung Leistungsstufen (R1.1, R1.2)  
  Jede Leistungsstufe aktiviert die erwartete Heizleistung; Rampen beim Hoch‑/Herunterschalten funktionieren ohne Sprünge.

- Reaktionszeit der UI (R1.3, R2.3)  
  Eingabe (Taste/Drehknopf/Touch) führt innerhalb definiertem Zeitlimit zur Zustandsänderung im Steuermodul.

- Funktion mit Selbstabschaltung (R2.5)  
  Prüfen, ob die Funktion nach 10 Minuten zuverlässig deaktiviert wird.

- Zeitbasierte Abschaltung (R5.3)  
  Validieren, dass der Timer die Zeit korrekt herunterzählt und die Kochzone am Ende abschaltet.

### 2.2 Usability‑Test (Benutzerfreundlichkeit)

- UI‑Basisfunktion (Tasten/Drehknopf/Touch)  
  Bedienelemente sind intuitiv, funktionieren zuverlässig (auch bei nassen Fingern) und vermeiden unbeabsichtigte Eingaben.

- Zuverlässigkeit bei verschmutzten Fingern (R1.4)  
  Testen, ob Tasten/Touch auch bei leicht verschmutzten Fingern (Fett, Mehl) korrekt reagieren.

- Unterscheidbare Taste „P“ (R2.4)  
  Prüfen, ob die Taste „P“ sich optisch (Form oder Farbe) deutlich von anderen Tasten unterscheidet und leicht erkennbar ist.

- Sichtbare Statusanzeige (R2.2)  
  Leistungsstufe, Betriebszustand (Ein/Aus, Topf erkannt, Restwärme) sind klar, verständlich und gut lesbar.

- Ein‑/Ausschaltung (R4.1)  
  Ein‑/Ausschalttaste ist leicht zu finden und zu bedienen, auch im Sperrmodus (z. B. Kindersicherung).

### 2.3 Black‑Box‑/Systemtest (Gesamtsystem)

- Temperaturmessung + Regelung (R3.1)  
  System hält die eingestellte Solltemperatur stabil, reagiert korrekt auf Topfwechsel und bleibt im sicheren Bereich.

- Grundsteuerung + UI (R1.1, R1.2, R1.3, R2.3)  
  Eingabe über UI führt zu korrekter Leistungsstufe, Reaktionszeit liegt im akzeptablen Bereich, auch bei wiederholten Eingaben.

- Sichtbare Statusanzeige (R2.2)  
  Anzeige zeigt aktuelle Leistung und Zustände (Topf erkannt, Fehler, Restwärme) korrekt und zeitnah an.

- Ein‑/Ausschaltung (R4.1)  
  System lässt sich zuverlässig ein‑/ausschalten, bleibt nach Stromausfall aus und kann im Sperrmodus noch abgeschaltet werden.

- Funktion mit Selbstabschaltung (R2.5)  
  Die Funktion läuft 10 Minuten und deaktiviert sich selbstständig, ohne dass die Kochzone weiterheizt.

- Zeitbasierte Abschaltung (R5.3)  
  Der Timer zählt die Zeit korrekt herunter und schaltet die Kochzone am Ende sicher ab.

---

## 3. Teststrategie

### Automatisierte Tests

- Unit‑Tests für Temperaturmessung (Sensorik), Leistungsstufen, UI‑Logik, Timer‑ und Selbstabschaltfunktion (R2.5, R5.3) werden automatisiert (z. B. mit Testframework).  
- Laufen in der CI‑Pipeline bei jedem Commit, um schnelle Rückmeldung zu geben.

### Manuelle Tests

- Usability‑Tests: Bedienung (Tasten/Drehknopf/Touch), Lesbarkeit der Anzeige, Ein‑/Ausschaltung, Funktion bei verschmutzten Fingern (R1.4), optische Unterscheidbarkeit der Taste „P“ (R2.4).  
- Systemtests: Verhalten bei Topfwechsel, Fehlerfälle, Restwärme, Kindersicherung, Timer‑ und Selbstabschaltfunktion.

### Iterative Tests

- Nach jeder Inkrementierung (neue Regelung, UI‑Änderung, Timer‑Logik) werden Unit‑ und Systemtests erneut ausgeführt.  
- Sicherstellung, dass neue Funktionen korrekt integriert sind und Fehler früh erkannt werden.

### Regressionstests

- Definiertes Set kritischer Systemtests (Leistungsstufen, Temperaturstabilität, Statusanzeigen, Ein‑/Ausschaltung, Timer, Selbstabschaltung) wird regelmäßig wiederholt.  
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

- Zuverlässigkeit bei verschmutzten Fingern (R1.4)  
  Eingaben müssen auch bei leicht verschmutzten Fingern (Fett, Mehl) zuverlässig erkannt werden.

- Lebensdauer der LED-Anzeige (R1.5)  
  Die LED-Anzeige muss mindestens 500 h kontinuierlich leuchten, ohne merkliche Helligkeitsminderung oder Ausfall.

- Unterscheidbare Taste „P“ (R2.4)  
  Die Taste „P“ muss sich optisch (Form oder Farbe) deutlich von anderen Tasten unterscheiden.

- Funktion mit Selbstabschaltung (R2.5)  
  Eine definierte Funktion (z. B. Boost, Timer) muss 10 Minuten laufen und sich danach selbstständig deaktivieren.

- Haltbarkeit des Schalters (R4.2)  
  Der Ein-/Ausschalter muss ≥ 100 000 Betätigungen ohne Defekt überstehen.

- Zeitbasierte Abschaltung (R5.3)  
  Eine Zeitfunktion (z. B. Timer) muss die Zeit korrekt herunterzählen und die Kochzone am Ende sicher abschalten.

### Out of Scope

- Energieeffizienz‑Messungen (z. B. kWh‑Verbrauch pro Kochvorgang).  
- Langzeitstabilität über mehrere Monate oder 1000+ Betriebsstunden.  
- Funktion mit nicht induktionsfähigen Kochgeschirr (z. B. Aluminium, Glas).  
- Netzwerkkommunikation, App‑Steuerung oder Cloud‑Funktionen.  
- Mechanische Haltbarkeit (z. B. Kratzer, Tropffestigkeit, Reinigung).  
- EMV‑ und Sicherheitszertifizierungen (z. B. CE, EMC, Überhitzungsschutz nach Norm).
