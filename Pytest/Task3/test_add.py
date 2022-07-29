from cmplex import C
from random import randint

def test_A():
    assert C(1, 2) + C(3, 4) == C(4, 6)

def test_B():
    assert C(-2, -1) + C(2, 1) == C(0, 0)

MAGIC_NUMB = 10 ** 9
def gen_rand(x):
    return randint(-x, x)

def test_C():
    for _ in range(10 ** 6):
        a, b, c, d = gen_rand(MAGIC_NUMB), gen_rand(MAGIC_NUMB), gen_rand(MAGIC_NUMB), gen_rand(MAGIC_NUMB)
        assert C(a, b) + C(c, d) == C(a + c, b + d)