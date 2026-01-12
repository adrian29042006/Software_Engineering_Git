class TouchController:
    def __init__(self, power_switch, power_manager, led_display):
        self.power_switch = power_switch
        self.power_manager = power_manager
        self.led_display = led_display

    def toggle_power(self):
        power_on = self.power_switch.toggle()
        if not power_on:
            self.power_manager.level = 0
        self.update_display()
        return power_on

    def adjust_power(self, direction, duration=0):
        if not self.power_switch.status:
            messagebox.showwarning("Warnung", "Kochfeld ist aus!")
            return
        # Langes Drücken (>3s) → auf Max oder Min springen
        if duration >= 3:
            if direction == "up":
                self.power_manager.set_max()
            elif direction == "down":
                self.power_manager.set_min()
        else:
            if direction == "up":
                self.power_manager.increase()
            elif direction == "down":
                self.power_manager.decrease()
        self.update_display()

    def press_p(self):
        if self.power_switch.status:
            messagebox.showinfo("P-Taste", "Sonderfunktion P aktiviert!")
        else:
            messagebox.showwarning("Warnung", "Kochfeld ist aus!")

    def update_display(self):
        self.led_display.update_status(self.power_switch.status)
        self.led_display.update_level(self.power_manager.level)
