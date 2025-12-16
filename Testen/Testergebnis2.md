# Sprint 2 – Testergebnisse

## 🔹 Unit-Tests

| Testfall | Status | Bemerkung |
|----------|--------|-----------|
| UT4 | ✅ Bestanden | Eingaben bei verschmutzten Fingern wurden zuverlässig erkannt, Leistungsstufe korrekt angepasst |
| UT5 | ✅ Bestanden | LED-Anzeige blieb ≥ 500 h stabil ohne Helligkeitsminderung |
| UT6 | ✅ Bestanden | Timerfunktion deaktivierte Kochzone nach 10 Minuten zuverlässig |
| UT7 | ✅ Bestanden | Ein-/Ausschalter überstand 100.000 Betätigungen ohne Defekt |

---

## 🔹 Integrationstests

| Testfall | Status | Bemerkung |
|----------|--------|-----------|
| IT4 | ✅ Bestanden | UI + verschmutzte Finger: Leistungsstufe korrekt erhöht, Display synchron |
| IT5 | ✅ Bestanden | Timer + Selbstabschaltung: Kochzone abgeschaltet, Funktion deaktiviert, Display korrekt |
| IT6 | ✅ Bestanden | Ein-/Ausschaltung + Belastungstest: Schalter funktionierte zuverlässig über 100.000 Vorgänge |

---

## Zusammenfassung
- Alle Unit- und Integrationstests erfolgreich  
- UI reagiert zuverlässig auch bei verschmutzten Fingern (R1.4)  
- LED-Anzeige über 500 h stabil (R1.5)  
- Timerfunktion läuft 10 Minuten und deaktiviert Kochzone automatisch (R2.5, R5.3)  
- Ein-/Ausschalter hält ≥ 100.000 Betätigungen ohne Defekt (R4.2)  
- Display zeigt Status korrekt und synchron zu Aktionen
