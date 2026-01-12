class Mikrocontroller:
    def __init__(self, temp_controller, led_display):
        self.temp_controller = temp_controller
        self.led_display = led_display

    def run(self, root):
        temp = self.temp_controller.update_temperature()
        self.led_display.update_temp(temp)
        root.after(500, lambda: self.run(root))
