import tkinter as tk
from tkinter import messagebox
import time

# --- Hardware/Software Komponenten --- #

class Benutzer:
    def __init__(self, touch_controller):
        self.touch_controller = touch_controller

    def druecke_power(self):
        self.touch_controller.toggle_power()

    def druecke_plus(self, duration=0):
        self.touch_controller.adjust_power("up", duration)

    def druecke_minus(self, duration=0):
        self.touch_controller.adjust_power("down", duration)

#    def druecke_p(self):
        #self.touch_controller.press_p()

class PowerSwitch:
    def __init__(self):
        self.status = False  # Aus

    def toggle(self):
        self.status = not self.status
        return self.status

class LEDDisplay:
    def __init__(self, status_label, level_label, temp_label):
        self.status_label = status_label
        self.level_label = level_label
        self.temp_label = temp_label

    def update_status(self, power_on):
        self.status_label.config(text=f"Status: {'Ein' if power_on else 'Aus'}")

    def update_level(self, level):
        self.level_label.config(text=f"Leistungsstufe: {level}")

    def update_temp(self, temp):
        self.temp_label.config(text=f"Temperatur: {int(temp)}°C")

class PowerManager:
    def __init__(self):
        self.level = 0

    def increase(self):
        if self.level < 9:
            self.level += 1

    def decrease(self):
        if self.level > 1:
            self.level -= 1

    def set_max(self):
        self.level = 9

    def set_min(self):
        self.level = 1

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

#    def press_p(self):
#        if self.power_switch.status:
#            messagebox.showinfo("P-Taste", "Sonderfunktion P aktiviert!")
#        else:
#            messagebox.showwarning("Warnung", "Kochfeld ist aus!")

    def update_display(self):
        self.led_display.update_status(self.power_switch.status)
        self.led_display.update_level(self.power_manager.level)

class TempSensor:
    def __init__(self):
        self.temp = 25

    def get_temp(self):
        return self.temp

    def set_temp(self, temp):
        self.temp = temp

class TempController:
    MAX_TEMPERATURES = {
        1: 28,
        2: 56,
        3: 83,
        4: 111,
        5: 139,
        6: 167,
        7: 194,
        8: 222,
        9: 250
    }

    def __init__(self, temp_sensor, power_manager):
        self.temp_sensor = temp_sensor
        self.power_manager = power_manager

    def update_temperature(self):
        current_temp = self.temp_sensor.get_temp()
        level = self.power_manager.level

        if level > 0:
            max_temp = self.MAX_TEMPERATURES[level]

            # Temperatur steigt weiter wie bisher …
            current_temp += level * 0.5

            # … darf aber den Maximalwert NICHT überschreiten
            if current_temp > max_temp:
                current_temp = max_temp
        else:
            # Abkühlen
            if current_temp > 25:
                current_temp -= 0.5

        self.temp_sensor.set_temp(current_temp)
        return current_temp


class InductionCoil:
    def __init__(self):
        pass

class Mikrocontroller:
    def __init__(self, temp_controller, led_display):
        self.temp_controller = temp_controller
        self.led_display = led_display

    def run(self, root):
        temp = self.temp_controller.update_temperature()
        self.led_display.update_temp(temp)
        root.after(500, lambda: self.run(root))

# --- GUI Setup --- #
root = tk.Tk()
root.title("Induktionskochfeld - Sprint 1 (+/- Buttons)")

# Labels
status_label = tk.Label(root, text="Status: Aus")
status_label.grid(row=0, column=0, columnspan=2, pady=5)
level_label = tk.Label(root, text="Leistungsstufe: 0")
level_label.grid(row=1, column=0, columnspan=2, pady=5)
temp_label = tk.Label(root, text="Temperatur: 25°C")
temp_label.grid(row=2, column=0, columnspan=2, pady=5)

# Komponenten erzeugen
power_switch = PowerSwitch()
power_manager = PowerManager()
led_display = LEDDisplay(status_label, level_label, temp_label)
touch_controller = TouchController(power_switch, power_manager, led_display)
temp_sensor = TempSensor()
temp_controller = TempController(temp_sensor, power_manager)
mikrocontroller = Mikrocontroller(temp_controller, led_display)
benutzer = Benutzer(touch_controller)
induction_coil = InductionCoil()

# Buttons
power_btn = tk.Button(root, text="Ein/Aus", width=10, command=benutzer.druecke_power)
power_btn.grid(row=3, column=0, padx=5, pady=5)

# p_btn = tk.Button(root, text="P", width=5, command=benutzer.druecke_p)
# p_btn.grid(row=3, column=1, padx=5, pady=5)

plus_btn = tk.Button(root, text="+", width=5)
plus_btn.grid(row=4, column=0, padx=5, pady=5)
minus_btn = tk.Button(root, text="-", width=5)
minus_btn.grid(row=4, column=1, padx=5, pady=5)

# Long press handling
press_start = {"plus": 0, "minus": 0}

def start_press(button):
    press_start[button] = time.time()

def end_press(button):
    duration = time.time() - press_start[button]
    if button == "plus":
        benutzer.druecke_plus(duration)
    else:
        benutzer.druecke_minus(duration)

plus_btn.bind("<ButtonPress-1>", lambda e: start_press("plus"))
plus_btn.bind("<ButtonRelease-1>", lambda e: end_press("plus"))

minus_btn.bind("<ButtonPress-1>", lambda e: start_press("minus"))
minus_btn.bind("<ButtonRelease-1>", lambda e: end_press("minus"))

# Start Mikrocontroller
mikrocontroller.run(root)
root.mainloop()
