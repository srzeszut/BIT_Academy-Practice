from cmplex import C
from random import randint

def test_C():
    for _ in range(10 ** 6):
        a, b, c, d = randint(-10 ** 9, 10 ** 9), randint(-10 ** 9, 10 ** 9), randint(-10 ** 9, 10 ** 9), randint(-10 ** 9, 10 ** 9)
        assert C(a, b) - C(c, d) == C(a - c, b - d)