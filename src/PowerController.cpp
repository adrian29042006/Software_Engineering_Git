// PowerController.cpp
#include "PowerController.hpp"

void PowerController::setPowerLevel(int level) {
    currentLevel = level;
    // TODO: Hardware-Ansteuerung
}

void PowerController::enableCoil(bool on) {
    // TODO: Spule ein-/ausschalten
    (void)on;
}
