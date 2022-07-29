from function import square
import pytest
from random import randint

# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie

class Test:
    def test_A(self):
        assert square(0) == 0
        assert square(1) == 1
        assert square(-1) == 1

    def test_B(self):
        for _ in range(5):
            number = randint(-10, 10)
            assert square(number) == number ** 2

class Test_small:
    def test_A(self):
        for _ in range(50):
            number = randint(-1000, 1000)
            assert square(number) == number ** 2

class Test_medium:
    def test_A(self):
        for _ in range(500):
            number = randint(10**4, 10**6)
            assert square(number) == number ** 2
            
class Test_big:
    @pytest.mark.dependency(depends=["Test_medium::test_A"])
    def test_A(self):
        for _ in range(500):
            number = randint(10**12, 10**13)
            assert square(number) == number ** 2