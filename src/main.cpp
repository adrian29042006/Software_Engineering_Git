#include "InductionHobController.hpp"
#include <thread>
#include <chrono>

int main() {
    InductionHobController hob;

    // Beispiel: Gerät einschalten und ein bisschen laufen lassen
    hob.handleInput({InputType::OnOffButton});

    for (int i = 0; i < 50; ++i) {
        hob.loop(100); // 100 ms
        std::this_thread::sleep_for(std::chrono::milliseconds(100));
    }

    return 0;
}
