// PowerController.hpp
#ifndef POWER_CONTROLLER_HPP
#define POWER_CONTROLLER_HPP

// R1.1: 9 Leistungsstufen
class PowerController {
public:
    void setPowerLevel(int level);  // 1..9
    void enableCoil(bool on);       // steuert InductionCoil

private:
    int currentLevel {0};
};

#endif // POWER_CONTROLLER_HPP
