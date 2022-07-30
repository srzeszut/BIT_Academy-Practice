class robotStatus:
    ALIVE = 0
    DEAD  = 1
    CRASH = 2
    WATER = 3

BATTERY_VAL = 10
class robot:
    # mapa, x, y, bateria
    def __init__(self, T, x, y, b):
        pass

    def left(self, val = 1):
        pass
    def right(self, val = 1):
        pass
    def up(self, val = 1):
        pass
    def down(self, val = 1):
        pass

    def get_status(self):
        pass
    def get_battery(self):
        pass
    def get_map(self):
        pass
    def get_x(self):
        pass
    def get_y(self):
        pass
