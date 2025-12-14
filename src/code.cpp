#include <iostream>
#include <chrono>
#include <thread>
#include <optional>

using namespace std::chrono;

enum class PowerLevel { Off = 0, L1, L2, L3, L4, L5, L6, L7, L8, L9 };
enum class UiEvent   { None, TouchLevel, KnobLevel, ButtonLevel,
                       ButtonOnOff, ButtonP, TimerSet };
enum class CookState { Idle, Cooking, PowerBoost, TimedCooking };

struct TempSensor {
    double currentTemp = 25.0;
    void   update(double power) {
        currentTemp += power * 0.1;  // sehr vereinfachtes Modell
    }
};

struct PowerController {
    PowerLevel level      = PowerLevel::Off;
    bool       isOn       = false;
    bool       coilActive = false;

    void setLevel(PowerLevel l) {
        level      = l;
        coilActive = (l != PowerLevel::Off) && isOn;
    }

    void setOn(bool on) {
        isOn       = on;
        coilActive = (level != PowerLevel::Off) && isOn;
    }

    double currentPower() const {
        return static_cast<int>(level);   // 0–9 als „Leistungsstufen“
    }
};

struct TimerController {
    std::optional<minutes> remaining;
    time_point<steady_clock> lastTick = steady_clock::now();

    void start(minutes m) { remaining = m; lastTick = steady_clock::now(); }
    void clear()          { remaining.reset(); }

    // reagiert mit ≤ 500 ms Verzögerung (modelliert durch Aufruffrequenz im main‑Loop)
    bool tick() {
        if (!remaining) return false;
        auto now  = steady_clock::now();
        auto diff = duration_cast<seconds>(now - lastTick);
        if (diff.count() >= 1) {
            lastTick = now;
            if (*remaining > minutes(0))
                *remaining -= minutes(1);
        }
        return remaining && *remaining <= minutes(0);
    }
};

struct UIHandler {
    bool   ledOnOff   = false;
    bool   ledP       = false;
    int    shownLevel = 0;
    int    shownTime  = 0;

    void showLevel(PowerLevel lvl) {
        shownLevel = static_cast<int>(lvl);
    }

    void showTimer(minutes m) {
        shownTime = static_cast<int>(m.count());
    }

    void setOnOffState(bool on) {
        ledOnOff = on;
    }

    void setPState(bool active) {
        ledP = active;
    }
};

// Gesamtsystem
struct CooktopController {
    CookState       state   = CookState::Idle;
    PowerController power;
    TimerController timer;
    TempSensor      temp;
    UIHandler       ui;

    // Reaktionszeit ≤ 100 ms für Leistungsstufen:
    void handleLevelInput(int level) {
        if (level < 0) level = 0;
        if (level > 9) level = 9;
        power.setLevel(static_cast<PowerLevel>(level));
        ui.showLevel(power.level);
    }

    void handleOnOff() {
        bool newState = !power.isOn;
        power.setOn(newState);
        ui.setOnOffState(newState);
        if (!newState) {
            state = CookState::Idle;
            power.setLevel(PowerLevel::Off);
            timer.clear();
            ui.setPState(false);
        }
    }

    // Taste „P“: 10 Minuten Boost, dann Auto‑Off der Funktion
    void handlePowerBoost() {
        if (!power.isOn) return;
        if (state != CookState::PowerBoost) {
            state = CookState::PowerBoost;
            power.setLevel(PowerLevel::L9);
            timer.start(minutes(10));
            ui.setPState(true);
        }
    }

    // Einstellbare Kochzeit 1–20 Minuten
    void handleTimerSet(int minutesSet) {
        if (!power.isOn) return;
        if (minutesSet < 1)  minutesSet = 1;
        if (minutesSet > 20) minutesSet = 20;
        timer.start(minutes(minutesSet));
        ui.showTimer(minutes(minutesSet));
        state = CookState::TimedCooking;
    }

    // Zyklischer Aufruf (z.B. alle 50–100 ms in Main‑Loop)
    void update() {
        if (!power.isOn) return;

        // Temperaturüberwachung
        temp.update(power.currentPower());

        bool timerElapsed = timer.tick();
        if (timerElapsed) {
            // Abschalten der Kochzone bei abgelaufenem Timer
            power.setLevel(PowerLevel::Off);
            ui.showLevel(PowerLevel::Off);
            ui.setPState(false);

            if (state == CookState::PowerBoost || state == CookState::TimedCooking)
                state = CookState::Idle;

            timer.clear();
        }
    }
};

int main() {
    CooktopController ctl;

    // Einfacher Testablauf: Ein, Leistungsstufe 5, Timer 3 min, Boost
    ctl.handleOnOff();          // Ein-/Aus-Schalter
    ctl.handleLevelInput(5);    // Leistungsstufe
    ctl.handleTimerSet(3);      // Kochzeit 3 Minuten

    for (int i = 0; i < 5; ++i) {
        ctl.update();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    ctl.handlePowerBoost();     // Taste „P“

    // „Laufe“ 11 Minuten im schnellen Simulationsmodus
    for (int i = 0; i < 11 * 10; ++i) { // 10 Updates pro „Minute“
        ctl.update();
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    std::cout << "OnOff LED: "   << ctl.ui.ledOnOff
              << ", P LED: "     << ctl.ui.ledP
              << ", Level: "     << ctl.ui.shownLevel
              << ", Timer: "     << ctl.ui.shownTime << " min\n";
}
