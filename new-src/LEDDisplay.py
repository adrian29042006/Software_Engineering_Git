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
