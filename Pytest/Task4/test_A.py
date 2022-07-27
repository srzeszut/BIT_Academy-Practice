import pytest
from function import square
from random import randint


# Napisać 4 klasy funkcji square
# Pierwsza zawiera kilka testów dla losowych liczb z przedziału <-10, 10>
# Druga zawiera kilka testów dla losowych liczb z przedziału <-1000, 1000>
# Trzecia zawiera kilka testów dla losowych liczb z przedziału <10 ** 4, 10 ** 6>
# Czwarta zawiera kilka testów dla losowych liczb z przedziału <10 ** 12, 10 ** 13>
# oraz marker skipif, który po wykonaniu uniemożliwi wykonanie testów z czwartej klasy
# ze względu na niepoprawne działanie funkcji w trzeciej klasie

class TestFirst:
    result = []
    for i in range(5):
        x = randint(-10, 10)
        result.append((x, x ** 2))

    @pytest.mark.parametrize('number,solution', result)
    def test_first(self, number, solution):
        assert square(number) == solution


class TestSecond:
    result = []
    for i in range(5):
        x = randint(-1000, 1000)
        result.append((x, x ** 2))

    @pytest.mark.parametrize('number,solution', result)
    def test_second(self, number, solution):
        assert square(number) == solution


class TestThird:
    result = []
    for i in range(5):
        x = randint(10 ** 4, 10 ** 6)
        result.append((x, x ** 2))

    @pytest.mark.parametrize('number,solution', result)
    def test_third(self, number, solution):
        assert square(number) == solution

@pytest.mark.skipif(reason="niepoprawne działanie funkcji w trzeciej klasie")
class TestFourth:

    result = []
    for i in range(5):
        x = randint(10 ** 12, 10 ** 13)
        result.append((x, x ** 2))

    @pytest.mark.parametrize('number,solution', result)
    def test_fourth(self, number, solution):
        assert square(number) == solution
