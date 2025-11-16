#include <iostream>
using namespace std;

// =====================================================
// BENUTZER
// =====================================================
class Benutzer {
private:
    string name;
    int alter;
    bool EIN_AUS_SCHALTER = false;

public:
    Benutzer(string n, int a) : name(n), alter(a) {}

    void anzeigen() {
        cout << "Name: " << name << ", Alter: " << alter << endl;
    }

    void schalterUmlegen() {
        EIN_AUS_SCHALTER = !EIN_AUS_SCHALTER;
        cout << "Schalter ist jetzt " 
             << (EIN_AUS_SCHALTER ? "AN" : "AUS") << endl;
    }

    bool istAn() const {
        return EIN_AUS_SCHALTER;
    }
};

// =====================================================
// TEMPERATURREGLER (0–9 Stufen)
// =====================================================
class Temperaturregler {
private:
    int stufe = 0;

public:
    void setStufe(int neueStufe) {
        if (neueStufe < 0) neueStufe = 0;
        if (neueStufe > 9) neueStufe = 9;
        stufe = neueStufe;

        cout << "[Temperaturregler] Stufe gesetzt auf: " << stufe << endl;
    }

    int getStufe() const {
        return stufe;
    }
};

// =====================================================
// INDUKTIONS-SPULE (Leistung vom PowerController)
// =====================================================
class Induktionsspule {
private:
    int aktuelleLeistung = 0;

public:
    void setLeistung(int watt) {
        aktuelleLeistung = watt;
        cout << "[Induktionsspule] Heizleistung: "<< aktuelleLeistung << " W\n";
    }

    int getLeistung() const {
        return aktuelleLeistung;
    }
};

// =====================================================
// POWER CONTROLLER — steuert Induktionsspule direkt
// =====================================================
class PowerController {
private:
    bool powerState = false;

    // feste 9 Leistungsstufen
    int leistungsTabelle[10] = {
        0,    // Stufe 0
        200,  // Stufe 1
        400,  // Stufe 2
        600,  // Stufe 3
        800,  // Stufe 4
        1000, // Stufe 5
        1200, // Stufe 6
        1500, // Stufe 7
        1800, // Stufe 8
        2100  // Stufe 9
    };

public:
    void setPowerState(bool state) {
        powerState = state;
    }

    // HIER PASSIERT DIE WICHTIGE STELLUNGNAHME:
    // PowerController wählt die Leistung aus UND gibt sie der Spule
    void steuereSpule(Induktionsspule &coil, int stufe) {
        if (!powerState) {
            coil.setLeistung(0);
            return;
        }

        int leistung = leistungsTabelle[stufe];
        coil.setLeistung(leistung);
    }
};

// =====================================================
// LED
// =====================================================
class LED {
public:
    void zeigeStufe(int stufe) {
        cout << "[LED] Anzeige Stufe: " << stufe << endl;
    }
};

// =====================================================
// HAUPTPROGRAMM
// =====================================================
int main() {
    Benutzer benutzer("Max", 25);
    Temperaturregler regler;
    PowerController controller;
    Induktionsspule spule;
    LED led;

    benutzer.anzeigen();
    benutzer.schalterUmlegen();                 // Gerät an
    controller.setPowerState(benutzer.istAn());

    // Stufe 6 setzen
    regler.setStufe(6);
    led.zeigeStufe(regler.getStufe());

    // PowerController steuert Spule
    controller.steuereSpule(spule, regler.getStufe());

    // Stufe 9 setzen
    regler.setStufe(9);
    led.zeigeStufe(regler.getStufe());
    controller.steuereSpule(spule, regler.getStufe());

    // Gerät AUS
    benutzer.schalterUmlegen();
    controller.setPowerState(benutzer.istAn());
    controller.steuereSpule(spule, regler.getStufe());

    return 0;
}
