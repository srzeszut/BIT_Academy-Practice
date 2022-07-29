from random import randint
from function import is_prime
from random import randint 
class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
    def test_A(self):
        assert is_prime(-1) == False
    def test_B(self):
        assert is_prime(0) == False
    def test_C(self):
        assert is_prime(1) == False
    def test_D(self):
        assert is_prime(2) == True
    def test_E(self):
        assert is_prime(3) == True
    def test_F(self):
        assert is_prime(4) == False
    def test_G(self):
        assert is_prime(5) == True
    def test_H(self):
        assert is_prime(6) == False

class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    def test_A(self):
        A = [3001, 1613, 3769, 2551, 5743, 8713, 7043, 6827, 7351, 2711]
        for x in A:
            assert is_prime(x) == True
            
    def test_B(self):
        A = [9420, 6493, 1445, 2093, 7519]
        for x in A:
            assert is_prime(x) == False

class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
    def test_A(self):
        A = [556370881039, 805469181901, 735493327391]
        for x in A:
            assert is_prime(x) == True
    def test_B(self):
        A = [235389759301, 261333307679, 663012434137, 877538745143, 205409137831, 222222222222]
        for x in A:
            assert is_prime(x) == False
