import pytest
from function import fib_OK
from math import log10

@pytest.mark.slow
class TestSmall:
    def test_A(self):
        assert fib_OK(0) == 0
        assert fib_OK(1) == 1
        assert fib_OK(2) == 1

    def test_B(self):
        assert fib_OK(10) == 55
        assert fib_OK(11) == 89
    
    def test_C(self):
        assert fib_OK(20) == 6765
        assert fib_OK(21) == 10946

class TestBig:
    def test_A(self):
        for i in range(100, 110):
            temp = fib_OK(i)
            assert log10(temp) < 25 and log10(temp) > 20

    def test_B(self):
        assert fib_OK(199) == 173402521172797813159685037284371942044301