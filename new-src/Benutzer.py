class Benutzer:
    def __init__(self, touch_controller):
        self.touch_controller = touch_controller

    def druecke_power(self):
        self.touch_controller.toggle_power()

    def druecke_plus(self, duration=0):
        self.touch_controller.adjust_power("up", duration)

    def druecke_minus(self, duration=0):
        self.touch_controller.adjust_power("down", duration)

    def druecke_p(self):
        self.touch_controller.press_p()
