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
