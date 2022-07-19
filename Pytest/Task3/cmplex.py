class C:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return C(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return C(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        x = self.x * other.x - self.y * other.y
        y = self.x * other.y + self.y * other.x
        return C(x, y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
