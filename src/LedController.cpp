// LedController.cpp
#include "LedController.hpp"
#include <iostream>

void LedController::showOnOff(State s) {
    // Platzhalter für echte LED-Logik
    std::cout << "State: " << (s == State::Off ? "Off" : "On/P") << '\n';
}

void LedController::showPowerLevel(int level) {
    std::cout << "Power level: " << level << '\n';
}

void LedController::showTimer(int secondsLeft) {
    std::cout << "Timer: " << secondsLeft << " s\n";
}

void LedController::showPMode(bool active) {
    std::cout << "P mode: " << (active ? "ON" : "OFF") << '\n';
}
