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
