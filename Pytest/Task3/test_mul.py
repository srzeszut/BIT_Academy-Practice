from cmplex import C
from random import randint

MAGIC_NUM = 10
RUN_NUM = 3

def test_C():
    for _ in range(RUN_NUM):
        a, b, c, d = randint(-MAGIC_NUM, MAGIC_NUM), randint(-MAGIC_NUM, MAGIC_NUM), randint(-MAGIC_NUM, MAGIC_NUM), randint(-MAGIC_NUM, MAGIC_NUM)
        correct = C(a, b) * C(c, d)
        user = C((a * c) - (b * d), (a * d) + (b * c))
        assert correct == user