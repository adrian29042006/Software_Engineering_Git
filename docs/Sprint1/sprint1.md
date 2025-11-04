# Sprint 1

### Sprint-Plan

Zu Beginn des ersten Sprint habe ich die relevanten Requirements ausgewählt. Der Fokus lag dabei auf der Implementierung grundlegender Teilfunktionalitäten, die für den weiteren Projektverlauf essenziell sind. Konkret wurden folgende Kernfunktionen identifiziert und berücksichtigt:

- Leistungsstufen um die Temperatur einzustellen

- Reaktionszeit des UI

- Sichtbare Statusanzeige

- Ein/Aus-Schaltung des Kochfeldes


Sprint Zeitraum: 30.10.25 - 6.11.25

Sprintziel:
1. Hardwarekomponenten
2. User Interface
3. Logik

### Schritt 2: Architektur

[Architektur](Architektur1.md)

### Schritt 3: Design
---

[Design1](https://github.com/adrian29042006/Software_Engineering_Git/blob/main/docs/Sprint1/Design%201.md)

---
Nachdem die Architektur abgeschlossen war, wurde der Sprint 1 erstellt mit den Diagrammen dazu die in Übungsaufgabe #4 gefordert waren. 
Die Requirements die ich für diesen Sprint ausgewählt habe sind: 
## Requierements

- R1.1:	9 klar unterscheidbare Leistungsstufen
- R1.2:	Auswahl der Leistungsstufen über Touch, Drehknopf oder Tasten
- R1.3:	Reaktionszeit ≤ 100 ms
- R2.1:	Taste „P“ muss klar erkennbar sein
- R2.2:	Zustand der Taste (Ein/Aus) muss sichtbar sein
- R2.3:	Reaktionszeit beim Betätigen ≤ 500 ms
- R3.1:	Temperatur in der Pfanne wird kontinuierlich überwacht
- R4.1: Gerät verfügt über einen Ein-/Aus-Schalter

Diese wurden anschließend in der Traceability Matrix nochmal genauer beschrieben. 


Das Klassendiagramm habe ich in 3 Layer aufgeteilt weil dieses für mich am sinnvollsten erscheint. Der erste Layer, User Interface mit den Klassen: Buttton, TouchController, LED und LED-Display. Wenn ein Benutzer etwas in dem UI auslöst, dann wird dieser Trigger im Control Layer weiterverarbeitet, sodass dieser den entsprechnenden Auffoderungen aggiert. Diese kann etwa ein Timer Einstellung oder eine Temperatureinstellung sein, der Control Layer leitet somit den weiteren Befehl den Hardware Abstraction Layer, den dritten Layer weiter, bei dem der Mikrokontroller die nötige Hardware Komponente mitteilt, was zu machen ist. Das kann beispielsweise der InductionCoil sein. Der Safety Controller überwacht den Mikrokontroller, falls Fehler auftauchen sollten.

Das Zustandsdiagramm mit Knopfinteraktion läuft so ab:
Vormerkung: Der Benutzer kann entweder Lang oder Kurz den Triggern, bei einer Spanne von 0-2s löst es wie ein kurzes halten aus, ab 2 löst das lange halten aus. Auf der linken Seite ist ein Tochpad zur besseren Nachvollziehbarkeit vorhanden, die Zahl oben steht für die jeweilige Leistungsstufe.
- Kurzes-Halten: Jedes Mal wenn der Benutzer das + klickt, geht es zur nächsten Leistungsstufe bis es bei 9 die maximale Leistungsstufe erreicht hat. Dieses fängt von 1 an, der EIN-AUS-Schalter ist ein anderes Bauteil und dieses wird nicht von + und - beeinflusst. Wenn der Benutzer - klickt geht es eine Leistungsstufe nach unten bis man auf die 1 Leistungsstufe ankommt.
- langes-Halten: Jedes Mal wenn der Benutzer das + hält, geht es auf die Leistungsstufe 9, egal welche Leistungsstufe man vorher war, es wird sofort auf 9 gestellt. Das ermöglicht ein effizientes Handling. Falls der Benutzer lange auf - bleibt, so ist es nun umgekehrt und geht auf 1 wieder auf die niedrigste Leistungsstufe.

# WICHTIG: Diese Beiden Befehle kann man kombinieren!

Das Sequenzdiagramm startet beim UIHandler der ein Interrupt auslöst, dieses vom PowerController verarbeitet wird. Das Interrupt ist eine Änderung der Leistungsstufen. Dieser PowerController gibt dem TempSensorReader den Befehl gettemperature(), dieser dann die Temperatur zurückgibt um die weitere Verarbeitung zu ermöglichen. Der PowerController stellt dann mithilfe des Temperaturwertes die Heizelemnte passend dazu ein und gibt zu guter letzt ein Update auf den Display zurück im Sinne von das ein anderer Leistungsstufenwert angezeigt wird.

Das Kommunikationsdiagramm: Der Benutzer schaltet das System ein, nach dem Auslösen eines ersten Befehls Interface löst der KochfeldControlelr aus dieser dann die Heizelmente passend einstellt und startet. Falls fehler im System auftauchen sollten Überwacht die Fehlerüberwachung den KochfeldController und zeigt falls Fehler bestehen sollten dem Interface diese.
