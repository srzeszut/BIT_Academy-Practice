from cmplex import C
from random import randint

def test_A():
    for _ in range(10 ** 6):
        x, y = randint(-10 ** 9, 10 ** 9), randint(-10 ** 9, 10 ** 9)
        assert C(x, y) == C(x, y)