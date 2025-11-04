# Sprint 1

### Sprint-Plan

Zu Beginn des ersten Sprint habe ich die relevanten Requirements ausgewählt. Der Fokus lag dabei auf der Implementierung grundlegender Teilfunktionalitäten, die für den weiteren Projektverlauf essenziell sind. Konkret wurden folgende Kernfunktionen identifiziert und berücksichtigt:

- Leistungsstufen um die Temperatur einzustellen

- Reaktionszeit des UI

- Sichtbare Statusanzeige

- Ein/Aus-Schaltung des Kochfeldes

## Requierements

- R1.1:	9 klar unterscheidbare Leistungsstufen
- R1.2:	Auswahl der Leistungsstufen über Touch, Drehknopf oder Tasten
- R1.3:	Reaktionszeit ≤ 100 ms
- R2.1:	Taste „P“ muss klar erkennbar sein
- R2.2:	Zustand der Taste (Ein/Aus) muss sichtbar sein
- R2.3:	Reaktionszeit beim Betätigen ≤ 500 ms
- R3.1:	Temperatur in der Pfanne wird kontinuierlich überwacht
- R4.1: Gerät verfügt über einen Ein-/Aus-Schalter

Sprint Zeitraum: 30.10.25

Sprintziel:
1. Hardwarekomponennten
2. User Interface
3. Logik

### Schritt 1: Architektur

Nach Abschluss der Anforderungsanalyse und Informationsbeschaffung habe ich mich im nächsten Schritt mit der Softwarearchitektur des Projekts beschäftigt. Ziel war es, eine geeignete strukturelle Grundlage für die spätere Implementierung zu schaffen.

Zunächst habe ich verschiedene Architekturmuster analysiert und verglichen (z. B. Schichtenarchitektur, komponentenbasierte Architektur, Microservices). Basierend auf den funktionalen Anforderungen, der geplanten Skalierung sowie den nicht-funktionalen Anforderungen wie Wartbarkeit und Erweiterbarkeit fiel die Wahl auf ein geeignetes Architekturmuster, das diesen Kriterien am besten entspricht.

Auf Grundlage des gewählten Architekturmusters habe ich ein Komponentendiagramm erstellt, das die Struktur des Systems und die wichtigsten funktionalen Bausteine visualisiert. Die Darstellung zeigt die zentralen Komponenten sowie deren Abhängigkeiten und ermöglicht eine klare Abgrenzung der Verantwortlichkeiten innerhalb des Systems.

Im Anschluss wurden die notwendigen Schnittstellen zwischen den Komponenten definiert. Dabei wurde besonderer Wert auf eine saubere Trennung von Verantwortlichkeiten sowie auf klare, dokumentierte Kommunikationswege gelegt. Diese Schnittstellen bilden die Grundlage für eine modulare und gut wartbare Implementierung.

Abschließend habe ich den Technologiestack für das Projekt definiert. Dieser umfasst sowohl die Programmiersprachen und Frameworks als auch Entwicklungsumgebungen, Tools zur Versionskontrolle und ggf. Bibliotheken zur Umsetzung spezifischer Anforderungen. Die Auswahl erfolgte auf Basis von Projektzielen, persönlicher Erfahrung sowie der Eignung der Technologien für die geplante Systemarchitektur.

### Schritt 3: Design

Im Anschluss an die Architekturdefinition wurde der Entwurfsprozess auf Klassenebene fortgeführt. Ziel war es, zentrale
Klassen und deren Interaktionen zu identifizieren sowie die Systemlogik anhand geeigneter UML-Diagramme zu modellieren.

Basierend auf den zuvor definierten Anforderungen und Komponenten wurde ein erstes Klassendiagramm erstellt. Dabei
wurden die für die Umsetzung der Kernfunktionalitäten relevanten Klassen identifiziert und modelliert. Jede Klasse wurde
einer der zuvor definierten Komponenten zugeordnet, um eine klare Strukturierung und Wiedererkennbarkeit zur
Architekturebene zu gewährleisten.
Zudem wurden öffentliche Schnittstellen (Methoden und Attribute) zwischen den Klassen direkt im Diagramm aufgenommen, um
die Kommunikation und Datenflüsse zwischen den Klassen transparent darzustellen.

Für die Benutzerinteraktion mit dem System wurde ein Zustandsdiagramm erstellt, das den Ablauf und die Zustandswechsel
bei der Bedienung über einen Button beschreibt. Dieses Diagramm hilft, das Verhalten der Benutzerschnittstelle (UI)
nachvollziehbar zu machen und die zugrundeliegende Logik der Zustandsänderungen eindeutig zu definieren.

Zur Darstellung des internen Ablaufs – insbesondere vom Zeitpunkt der Spannungsmessung bis zur Anzeige des
Batteriestands – wurde ein Sequenzdiagramm entworfen. Es beschreibt die zeitliche Abfolge der Methodenaufrufe und
Interaktionen zwischen den beteiligten Objekten und zeigt, wie die Daten durch das System fließen.

Abschließend wurde überprüft, ob sich für einzelne Klassen oder Strukturmuster etablierte Design Patterns sinnvoll
anwenden lassen (z. B. Singleton, Factory, Observer). Dabei wurde besonderes Augenmerk auf Wiederverwendbarkeit,
Erweiterbarkeit und die Reduzierung von Kopplung gelegt. Mögliche Pattern wurden identifiziert und deren Einsatz
sorgfältig abgewogen, um die Struktur des Systems nachhaltig zu verbessern.

Bei allen Klassendiagrammen wurde bewusst auf die Kardinalitäten verzichtet. Hier handelt es sich lediglich um interne
Logik und das Ergänzen der Klassendiagramme um jegliche Kardinalitäten erzeugt einen enormen Overhead ohne wirklichen
Mehrwert im Verständnis.
