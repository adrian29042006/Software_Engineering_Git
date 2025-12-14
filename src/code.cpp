class PowerController;
class TimerController;
class TempController;
class PowerManager;
class Heizelemente;
class TimerManager;
class TempSensor;
class LEDDisplay;

class UIHandler {
private:
    PowerController* powerController;
    TimerController* timerController;
    TempController* tempController;

public:
    void selectPowerLevel(int level) {            // R1.1, R1.2, R1.3
        powerController->setPowerLevel(level);
    }

    void pressPowerButton() {                     // R4.1, R2.2, R2.3, R4.2
        powerController->toggleMainPower();
    }

    void pressPButton() {                         // R2.1, R2.4, R2.5
        powerController->enableBoostMode();
        timerController->startBoostTimer(10 * 60);
    }

    void setCookingTime(int minutes) {           // R5.1, R5.2
        timerController->setCookingTime(minutes);
    }
};

class PowerController {
private:
    PowerManager* powerManager;
    Heizelemente* heizelemente;
    class TempSensorReader* tempSensorReader;
    bool mainOn;

public:
    void setPowerLevel(int level) {              // R1.1, R1.3
        powerManager->setLevel(level);
        heizelemente->applyPower(level);
    }

    void toggleMainPower() {                     // R4.1
        mainOn = !mainOn;
        heizelemente->setEnabled(mainOn);
    }

    void enableBoostMode() {                     // R2.5
        powerManager->setBoost(true);
        heizelemente->enableBoost();
    }

    void updateWithTemperature() {               // R3.1, R5.3
        double temp = tempSensorReader->read();
        // Regellogik, ggf. Abschalten
    }
};

class TimerController {
private:
    TimerManager* timerManager;
    PowerController* powerController;

public:
    void startBoostTimer(int seconds) {          // R2.5
        // In C++ statt Lambda hier z.B. Funktionszeiger oder std::function
        timerManager->start(seconds, [this]() {
            powerController->enableBoostMode();
        });
    }

    void setCookingTime(int minutes) {           // R5.1
        timerManager->start(minutes * 60, [this]() {
            shutdownZone();
        });
    }

    void shutdownZone() {                        // R5.3
        powerController->toggleMainPower();
    }
};

class TempSensorReader {
private:
    TempSensor* sensor;

public:
    double read() {                              // R3.1
        return sensor->readTemperature();
    }
};

class LEDDisplay {
public:
    void showPowerLevel(int level) {             // R1.1, R3.2
        // Anzeige der Stufe
    }

    void showTimer(int seconds) {                // R5.2
        // Anzeige der Restzeit
    }

    void showPowerState(bool on) {               // R2.2
        // Ein-/Aus-Symbol
    }

    void showPButtonState(bool active) {         // R2.1, R2.4
        // Hervorgehobene P-Anzeige
    }
};

class Button {
public:
    template<typename Callable>
    void onPress(Callable action) {
        action();                                // R2.2, R2.3, R4.1, R4.2
    }
};

