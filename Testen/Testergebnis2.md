***
# ✅ Testergebnisse – Sprint 2
***

## Projektinformationen

- **Projekt:** Induktionskochfeld
- **Sprint:** 2
- **Abgedeckte Requirements:** R1.1, R1.2, R1.4, R1.5, R2.2, R2.4, R2.5, R3.1, R4.1, R4.2, R5.3

***

## 🔹 Unit-Test Ergebnisse

***

### UT4 – Temperaturmessung: stabiler Wert (R3.1)

- **Ziel:** Prüfen, ob der Temperatursensor stabile Werte liefert.  
- **Ergebnis:** Der Sensor lieferte konsistente Temperaturwerte ohne Ausreißer bei allen getesteten Szenarien (leer, Wasser, Öl).  
- **Status:** ✅ Bestanden

***

### UT5 – UI-Reaktion bei verschmutzten Fingern (R1.4)

- **Ziel:** Eingaben werden auch bei leicht verschmutzten Fingern korrekt erkannt.  
- **Ergebnis:** Die Leistungsstufe wurde korrekt erhöht, Eingaben wurden zuverlässig registriert. Reaktionszeit ≤ 100 ms.  
- **Status:** ✅ Bestanden

***

### UT6 – Timer mit Selbstabschaltung (R2.5, R5.3)

- **Ziel:** Verifikation der zeitbasierten Abschaltung nach 10 Minuten.  
- **Ergebnis:** Nach 10 Minuten deaktivierte sich die Boost-Funktion selbstständig, die Kochzone wurde abgeschaltet, Display zeigte korrekten Status.  
- **Status:** ✅ Bestanden

***

## 🔹 Integrationstest Ergebnisse

***

### IT4 – UI-Eingabe steuert Heizleistung inkl. verschmutzte Finger

- **Ziel:** Test des Zusammenspiels von UI, Steuerlogik und Hardware bei verschmutzten Fingern.  
- **Ergebnis:** Leistungsstufe wurde korrekt angepasst, Heizleistung reguliert, Anzeige aktualisiert. Keine Fehler bei verschmutzten Eingaben.  
- **Status:** ✅ Bestanden

***

### IT5 – Timerfunktion + Selbstabschaltung

- **Ziel:** Prüfen des Zusammenspiels von Timer, PowerController und Anzeige bei Selbstabschaltung.  
- **Ergebnis:** Timer zählte korrekt herunter, Kochzone wurde abgeschaltet, Funktion deaktivierte sich nach 10 Minuten selbstständig, Display korrekt aktualisiert.  
- **Status:** ✅ Bestanden

***

### IT6 – Ein-/Ausschaltung inkl. Schalterhaltbarkeit

- **Ziel:** Integrationstest für Ein-/Ausschaltung und Schalterhaltbarkeit ≥ 100.000 Betätigungen.  
- **Ergebnis:** Gerät schaltete zuverlässig ein und aus. Nach ≥ 100.000 Betätigungen keine Fehlfunktionen oder Defekte festgestellt.  
- **Status:** ✅ Bestanden

***
