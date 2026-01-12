class PowerSwitch:
    def __init__(self):
        self.status = False  # Aus

    def toggle(self):
        self.status = not self.status
        return self.status
