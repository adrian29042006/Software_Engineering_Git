#ifndef INDUCTION_HOB_CONTROLLER_HPP
#define INDUCTION_HOB_CONTROLLER_HPP

#include "State.hpp"
#include "TemperatureSensor.hpp"
#include "PowerController.hpp"
#include "LedController.hpp"

// Hauptcontroller, der Requirements R1.*, R2.*, R3.*, R4.*, R5.* abdeckt
class InductionHobController {
public:
    InductionHobController();

    void loop(int deltaMs);              // zyklisch aufrufen (R1.3)
    void handleInput(const InputEvent&); // Benutzer-Eingaben (R1.2)

private:
    void handleOnOffButton();            // R4.1, R2.2
    void handlePButton();                // R2.1, R2.4, R2.5
    void changePowerLevel(int delta);    // R1.1
    void changeTimer(int deltaSeconds);  // R5.1
    void updateTimer(int deltaMs);       // R5.3, R2.5
    void readTemperature();              // R3.1
    void updateOutputs();                // Anzeige + Power (R2.2, R5.2)

    State state;
    int   powerLevel;
    int   cookTimeSeconds;
    int   timerAccumulatorMs;
    int   pModeRemainingMs;
    float currentTemperature;

    TemperatureSensor tempSensor;
    PowerController   powerCtrl;
    LedController     led;
};

#endif // INDUCTION_HOB_CONTROLLER_HPP
