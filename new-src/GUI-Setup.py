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

p_btn = tk.Button(root, text="P", width=5, command=benutzer.druecke_p)
p_btn.grid(row=3, column=1, padx=5, pady=5)

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
