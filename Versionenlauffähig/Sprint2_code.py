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

    def druecke_p(self):
        self.touch_controller.press_p()


class PowerSwitch:
    def __init__(self):
        self.status = False
        self.toggle_count = 0  # Lebensdauerprüfung

    def toggle(self):
        self.toggle_count += 1
        if self.toggle_count > 100000:
            messagebox.showerror("Fehler", "Power-Schalter defekt!")
            return self.status
        self.status = not self.status
        return self.status


class LEDDisplay:
    def __init__(self, status_label, level_label, temp_label, timer_label):
        self.status_label = status_label
        self.level_label = level_label
        self.temp_label = temp_label
        self.timer_label = timer_label
        self.operating_seconds = 0  # LED Lebensdauer

    def update_status(self, power_on):
        self.status_label.config(text=f"Status: {'Ein' if power_on else 'Aus'}")

    def update_level(self, level):
        self.level_label.config(text=f"Leistungsstufe: {level}")

    def update_temp(self, temp):
        self.temp_label.config(text=f"Temperatur: {int(temp)}°C")

    def update_timer(self, seconds):
        if seconds > 0:
            self.timer_label.config(text=f"P-Timer: {seconds//60:02}:{seconds%60:02}")
        else:
            self.timer_label.config(text="P-Timer: --")

    def tick_lifetime(self):
        self.operating_seconds += 1
        if self.operating_seconds >= 500 * 3600:
            messagebox.showwarning("Warnung", "LED-Lebensdauer erreicht (500h)")


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
    def __init__(self, power_switch, power_manager, led_display, finger_sensor):
        self.power_switch = power_switch
        self.power_manager = power_manager
        self.led_display = led_display
        self.finger_sensor = finger_sensor
        self.p_active = False
        self.p_time_left = 0


    def toggle_power(self):
        power_on = self.power_switch.toggle()
        if not power_on:
            self.power_manager.level = 0
            self.p_active = False
            self.p_time_left = 0
        self.update_display()
        return power_on
    def adjust_power(self, direction, duration=0):
        if not self.power_switch.status:
            messagebox.showwarning("Warnung", "Kochfeld ist aus!")
            return

        # 🔒 Verschmutzte Finger
        if self.finger_sensor.is_dirty():
            if duration < 1:
                messagebox.showwarning(
                    "Touch gesperrt",
                    "Finger verschmutzt – bitte länger drücken!"
                )
                return

        # Normale Logik
        if duration >= 3:
            if direction == "up":
                self.power_manager.set_max()
            else:
                self.power_manager.set_min()
        else:
            if direction == "up":
                self.power_manager.increase()
            else:
                self.power_manager.decrease()

        self.update_display()


    def press_p(self):
        if not self.power_switch.status:
            messagebox.showwarning("Warnung", "Kochfeld ist aus!")
            return

        if self.finger_sensor.is_dirty():
            messagebox.showwarning(
                "Touch gesperrt",
                "P-Modus bei verschmutzten Fingern deaktiviert!"
            )
            return

        self.p_active = True
        self.p_time_left = 600
        self.power_manager.set_max()
        self.update_display()

    def update_display(self):
        self.led_display.update_status(self.power_switch.status)
        self.led_display.update_level(self.power_manager.level)
        self.led_display.update_timer(self.p_time_left)



class FingerSensor:
    def __init__(self):
        self.dirty = False  # False = sauber, True = verschmutzt

    def set_dirty(self, state: bool):
        self.dirty = state

    def is_dirty(self):
        return self.dirty


class TempSensor:
    def __init__(self):
        self.temp = 25

    def get_temp(self):
        return self.temp

    def set_temp(self, temp):
        self.temp = temp


class TempController:
    MAX_TEMPERATURES = {
        1: 28, 2: 56, 3: 83, 4: 111, 5: 139,
        6: 167, 7: 194, 8: 222, 9: 250
    }

    def __init__(self, temp_sensor, power_manager):
        self.temp_sensor = temp_sensor
        self.power_manager = power_manager

    def update_temperature(self):
        current_temp = self.temp_sensor.get_temp()
        level = self.power_manager.level

        if level > 0:
            max_temp = self.MAX_TEMPERATURES[level]
            current_temp = min(current_temp + level * 0.5, max_temp)
        elif current_temp > 25:
            current_temp -= 0.5

        self.temp_sensor.set_temp(current_temp)
        return current_temp


class Mikrocontroller:
    def __init__(self, temp_controller, led_display, touch_controller):
        self.temp_controller = temp_controller
        self.led_display = led_display
        self.touch_controller = touch_controller

    def run(self, root):
        temp = self.temp_controller.update_temperature()
        self.led_display.update_temp(temp)
        self.led_display.tick_lifetime()

        if self.touch_controller.p_active:
            self.touch_controller.p_time_left -= 1
            if self.touch_controller.p_time_left <= 0:
                self.touch_controller.toggle_power()
            else:
                self.led_display.update_timer(self.touch_controller.p_time_left)

        root.after(1000, lambda: self.run(root))


# --- GUI Setup --- #
root = tk.Tk()
root.title("Induktionskochfeld mit P-Automatik")

status_label = tk.Label(root, text="Status: Aus")
status_label.grid(row=0, column=0, columnspan=3)

level_label = tk.Label(root, text="Leistungsstufe: 0")
level_label.grid(row=1, column=0, columnspan=3)

temp_label = tk.Label(root, text="Temperatur: 25°C")
temp_label.grid(row=2, column=0, columnspan=3)

timer_label = tk.Label(root, text="P-Timer: --")
timer_label.grid(row=3, column=0, columnspan=3)

power_switch = PowerSwitch()
power_manager = PowerManager()
led_display = LEDDisplay(status_label, level_label, temp_label, timer_label)
finger_sensor = FingerSensor()
touch_controller = TouchController(
    power_switch, power_manager, led_display, finger_sensor
)
temp_sensor = TempSensor()
temp_controller = TempController(temp_sensor, power_manager)
mikrocontroller = Mikrocontroller(temp_controller, led_display, touch_controller)
benutzer = Benutzer(touch_controller)

power_btn = tk.Button(root, text="Ein/Aus", command=benutzer.druecke_power)
power_btn.grid(row=4, column=1)

plus_btn = tk.Button(root, text="+", width=5)
plus_btn.grid(row=5, column=0)

minus_btn = tk.Button(root, text="-", width=5)
minus_btn.grid(row=5, column=2)

# Oranger P-Kreis
canvas = tk.Canvas(root, width=50, height=50, highlightthickness=0)
canvas.grid(row=5, column=1)
circle = canvas.create_oval(5, 5, 45, 45, fill="orange")
text = canvas.create_text(25, 25, text="P", font=("Arial", 14, "bold"))

canvas.bind("<Button-1>", lambda e: benutzer.druecke_p())

press_start = {"plus": 0, "minus": 0}

def start_press(btn):
    press_start[btn] = time.time()

def end_press(btn):
    duration = time.time() - press_start[btn]
    if btn == "plus":
        benutzer.druecke_plus(duration)
    else:
        benutzer.druecke_minus(duration)

plus_btn.bind("<ButtonPress-1>", lambda e: start_press("plus"))
plus_btn.bind("<ButtonRelease-1>", lambda e: end_press("plus"))
minus_btn.bind("<ButtonPress-1>", lambda e: start_press("minus"))
minus_btn.bind("<ButtonRelease-1>", lambda e: end_press("minus"))

mikrocontroller.run(root)
root.mainloop()
