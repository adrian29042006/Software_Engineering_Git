#ifndef STATE_HPP
#define STATE_HPP

// R4.1: Ein-/Aus-Schalter Zustände
enum class State {
    Off,
    On,
    PowerModeP
};

// R1.2: Eingaben vom Benutzer
enum class InputType {
    OnOffButton,
    PowerPlus,
    PowerMinus,
    PButton,
    TimerPlus,
    TimerMinus
};

struct InputEvent {
    InputType type;
};

#endif // STATE_HPP
