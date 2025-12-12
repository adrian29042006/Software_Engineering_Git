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
---
### Schritt 2: Architektur

[Architektur](Architektur1.md)

---

### Schritt 3: Design

[Design1](https://github.com/adrian29042006/Software_Engineering_Git/blob/main/docs/Sprint1/Design%201.md)


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
WICHTIG: Diese Beiden Befehle kann man kombinieren!
Das Sequenzdiagramm startet beim UIHandler der ein Interrupt auslöst, dieses vom PowerController verarbeitet wird. Das Interrupt ist eine Änderung der Leistungsstufen. Dieser PowerController gibt dem TempSensorReader den Befehl gettemperature(), dieser dann die Temperatur zurückgibt um die weitere Verarbeitung zu ermöglichen. Der PowerController stellt dann mithilfe des Temperaturwertes die Heizelemnte passend dazu ein und gibt zu guter letzt ein Update auf den Display zurück im Sinne von das ein anderer Leistungsstufenwert angezeigt wird.

Das Kommunikationsdiagramm: Der Benutzer schaltet das System ein, nach dem Auslösen eines ersten Befehls Interface löst der KochfeldControlelr aus dieser dann die Heizelmente passend einstellt und startet. Falls fehler im System auftauchen sollten Überwacht die Fehlerüberwachung den KochfeldController und zeigt falls Fehler bestehen sollten dem Interface diese.

---

### Schritt 4: Implementierung:
Nach der Design-Phase mit Sequenzdiagrammen, Klassendiagrammen und weiteren UML-Diagrammen folgt die Implementierung als zentraler Zwischenpart, in dem die geplanten Modelle in ausführbaren Code übersetzt werden. Hier entsteht der geschriebene Quellcode schrittweise, indem Klassenstrukturen, Attribute, Methodensignaturen und Algorithmen direkt aus den Diagrammen in C++ umgesetzt werden, um Objektinteraktionen und Datenflüsse präzise zu realisieren.​
Der Prozess beginnt mit der Deklaration der Klassen und Methoden gemäß dem Klassendiagramm, gefolgt von der Ausformulierung der Logik in Schleifen, Bedingungen und Aufrufen, die den Sequenzdiagrammen entsprechen. 
Die Implementierung endet mit dem vollständigen, versionierten Quellcode, der nun in der Testphase auf Korrektheit, Funktionalität und Robustheit geprüft wird.
docs/Sprint1/Test1.md
[Test](https://github.com/adrian29042006/Software_Engineering_Git/blob/main/docs/Sprint1/Test1.md )

---

### Schritt 5: Testphase
Nach der Implementierungsphase folgt die Testphase, in der die entwickelte Software systematisch überprüft wird. Ziel dieser Phase ist es zu kontrollieren, ob alle zuvor definierten Anforderungen erfüllt werden und ob die Anwendung stabil und fehlerfrei funktioniert.

In der Testphase werden zunächst einzelne Komponenten der Software mittels Unit-Tests geprüft, um sicherzustellen, dass jede Klasse und Methode das gewünschte Verhalten zeigt. Anschließend werden Integrationstests durchgeführt, bei denen das Zusammenspiel mehrerer Module getestet wird, um Schnittstellenprobleme und unerwartete Wechselwirkungen zu erkennen.

Darauf aufbauend folgen Systemtests, bei denen das Gesamtsystem in einer möglichst realistischen Umgebung getestet wird, um typische Nutzungsszenarien, Randfälle und Fehlersituationen abzudecken. Die Ergebnisse der Tests werden dokumentiert, gefundene Fehler werden analysiert, priorisiert und in weiteren Iterationen behoben, bis ein stabiler Stand erreicht ist. Nach Abschluss der Testphase bildet dieser geprüfte Stand die Grundlage für die anschließende Review- und Retrospektiven-Phase.

### Schritt 6: Rewies und Retroperspektive
Nach der Testphase von Sprint 1, in der der Code umfassend geprüft und stabilisiert wurde, folgt die Retrospektive als reflektierender Abschluss dieses Schritts. Hier analysiere ich den gesamten Ablauf von Design über Implementierung bis Testing, um Erfolge zu würdigen, Probleme zu identifizieren und konkrete Verbesserungen für Sprint 2 zu definieren.​



Was lief nicht so gut?
- Alle Anforderungen wurden umgesetzt
- gute Design Diagramme führten zu fehlerfreier Code Implementierung
- gute Nachverfolgbarkeit durch GitHub-Links, die schnelle Reproduzierbarkeit ermöglichten.
- Die Tests wurden erfolgreich umgesetzt
- Recherche zu beginn hat Einstieg vereinfacht
- erfolgreich Sprint 1 geschafft

  
Was nicht gut lief?
- Zeitplan wurde nicht eingehalten
- unnötige Schreibfehler die erst Später aufgefallen sind 
- Schwierig von 0 anzufangen
- Zu lange gebraucht bei den Diagrammen
- Manuelle Testevaluation war Zeitaufwendig
- Startpunkt hat gefehlt (ohne vorher genauen Plan zu haben)

Was werde ich im Nächsten Sprint anders machen
- Mir genaue Ziele setzten was ich vorhabe und vorher einen Plan schreiben um es so gut es geht zu strukturieren
- Mehr Zeit investieren (andere Fächer wurden vorgezogen, um den Leistungsnachweis in der mitte des Semesters zu bestehen)
- nciht rechtzeitige Abgabe
  
Lessons Learned:
- Aufgaben Zeitfristig abgegeben um dann optimal für die Vorlesung vorbereitet zu sein
- ich habe außerdem gelernt, dass die Vielzahl an Anforderungen keine großartige Überforderung darstellen soll
- die richtigen Tools (Perplexity Pro) ermöglichen es, effizient zu arbeiten und ein großartigen Sprint 1 zu entwerfen
- Leider wurde die Barrierefreiheit nicht eingehalten, also keine Lösung von blinden Personen die den Touch bildschirm erkennen können um damit die Leistungskontrolle durchzuführen (würde aber dieses Projekt einen enormen Anstieg an dem Komplex-Grad herbeiführen)

  

