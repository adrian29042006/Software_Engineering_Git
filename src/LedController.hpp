// LedController.hpp
#ifndef LED_CONTROLLER_HPP
#define LED_CONTROLLER_HPP

#include "State.hpp"

// Anzeige-Controller: LED/Display (R2.2, R5.2, R2.1, R2.4)
class LedController {
public:
    void showOnOff(State s);          // Zustand Ein/Aus
    void showPowerLevel(int level);   // 1..9
    void showTimer(int secondsLeft);  // Timeranzeige
    void showPMode(bool active);      // P-Taste hervorheben
};

#endif // LED_CONTROLLER_HPP
