#include "InductionHobController.hpp"

InductionHobController::InductionHobController()
    : state(State::Off),
      powerLevel(0),
      cookTimeSeconds(0),
      timerAccumulatorMs(0),
      pModeRemainingMs(0),
      currentTemperature(0.0f)
{}

// R1.3: Reaktionszeit <= 100 ms -> loop alle <=100 ms aufrufen
void InductionHobController::loop(int deltaMs) {
    readTemperature();      // R3.1
    updateTimer(deltaMs);   // R5.3, R2.5
    updateOutputs();
}

void InductionHobController::handleInput(const InputEvent& ev) {
    switch (ev.type) {
    case InputType::OnOffButton:
        handleOnOffButton();    // R4.1
        break;
    case InputType::PowerPlus:
        changePowerLevel(+1);   // R1.1
        break;
    case InputType::PowerMinus:
        changePowerLevel(-1);   // R1.1
        break;
    case InputType::PButton:
        handlePButton();        // R2.1, R2.4, R2.5
        break;
    case InputType::TimerPlus:
        changeTimer(+60);       // R5.1
        break;
    case InputType::TimerMinus:
        changeTimer(-60);       // R5.1
        break;
    }
}

void InductionHobController::handleOnOffButton() {
    if (state == State::Off) {
        state = State::On;
    } else {
        state = State::Off;
        cookTimeSeconds = 0;
        pModeRemainingMs = 0;
        powerLevel = 0;
    }
}

void InductionHobController::handlePButton() {
    if (state == State::Off) return;

    if (state == State::PowerModeP) {
        state = State::On;
        pModeRemainingMs = 0;
    } else {
        state = State::PowerModeP;
        pModeRemainingMs = 10 * 60 * 1000; // 10 min (R2.5)
        powerLevel = 9;                    // z.B. max Power
    }
}

void InductionHobController::changePowerLevel(int delta) {
    if (state == State::Off) return;
    powerLevel += delta;
    if (powerLevel < 1) powerLevel = 1;
    if (powerLevel > 9) powerLevel = 9;    // R1.1
}

void InductionHobController::changeTimer(int deltaSeconds) {
    if (state == State::Off) return;
    cookTimeSeconds += deltaSeconds;
    if (cookTimeSeconds < 60) cookTimeSeconds = 60;
    if (cookTimeSeconds > 20 * 60) cookTimeSeconds = 20 * 60; // R5.1
}

void InductionHobController::updateTimer(int deltaMs) {
    if (state != State::Off && cookTimeSeconds > 0) {
        timerAccumulatorMs += deltaMs;
        while (timerAccumulatorMs >= 1000) {
            timerAccumulatorMs -= 1000;
            --cookTimeSeconds;
            if (cookTimeSeconds <= 0) {
                state = State::Off;        // R5.3
                powerLevel = 0;
                cookTimeSeconds = 0;
                pModeRemainingMs = 0;
                break;
            }
        }
    }

    if (state == State::PowerModeP && pModeRemainingMs > 0) {
        pModeRemainingMs -= deltaMs;
        if (pModeRemainingMs <= 0) {
            state = State::On;             // R2.5
            pModeRemainingMs = 0;
        }
    }
}

void InductionHobController::readTemperature() {
    currentTemperature = tempSensor.readCelsius(); // R3.1
    // Hier könnte ein Regler kommen
}

void InductionHobController::updateOutputs() {
    led.showOnOff(state);                   // R2.2
    led.showTimer(cookTimeSeconds);         // R5.2
    led.showPMode(state == State::PowerModeP); // R2.1, R2.4
    led.showPowerLevel(powerLevel);         // R1.1

    if (state == State::Off) {
        powerCtrl.enableCoil(false);
        powerCtrl.setPowerLevel(0);
    } else {
        powerCtrl.enableCoil(true);
        powerCtrl.setPowerLevel(powerLevel);
    }
}
