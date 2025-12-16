# Sprint 1 – Testergebnisse

## 🔹 Unit-Tests

| Testfall | Status | Bemerkung |
|----------|--------|-----------|
| UT1 | ✅ Bestanden | Leistungsstufe wurde nicht unter 1 reduziert, System stabil |
| UT2 | ✅ Bestanden | UI-Eingaben wurden zuverlässig innerhalb ~40 ms verarbeitet, Leistungsstufe korrekt angepasst |
| UT3 | ✅ Bestanden | Temperaturwerte des Sensors konstant, keine Ausreißer |

---

## 🔹 Integrationstests

| Testfall | Status | Bemerkung |
|----------|--------|-----------|
| IT1 | ✅ Bestanden | UI-Eingabe steuert Heizleistung korrekt, Anzeige synchron |
| IT2 | ✅ Bestanden | Ein-/Ausschaltung funktioniert zuverlässig, kein automatisches Einschalten nach Reset |
| IT3 | ✅ Bestanden | Temperaturregelung passt Heizleistung korrekt an, System stabil |

---

## Zusammenfassung
- Alle Unit- und Integrationstests erfolgreich  
- Leistungsstufen korrekt begrenzt (R1.1, R1.2)  
- UI reagiert schnell und zuverlässig (≤ 100 ms, R1.3)  
- Temperatursensor liefert stabile Werte (R3.1)  
- System lässt sich zuverlässig ein- und ausschalten (R4.1)  
- Anzeige zeigt Leistungsstufen und Status korrekt (R2.2)

