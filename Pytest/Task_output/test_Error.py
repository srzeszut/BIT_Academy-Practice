import pytest
from function import fib_Error
from math import log10

@pytest.mark.slow
class TestSmall:
    def test_A(self):
        assert fib_Error(0) == 0
        assert fib_Error(1) == 1
        assert fib_Error(2) == 2

    def test_B(self):
        assert fib_Error(10) == 3
        assert fib_Error(11) == 4
    
    def test_C(self):
        assert fib_Error(20) == 3
        assert fib_Error(21) == 4

    def test_D(self):
        assert fib_Error(0) == 1

    def test_E(self):
        assert fib_Error(1) == 2

class TestBig:
    def test_A(self):
        for i in range(100, 110):
            temp = fib_Error(i)
            assert log10(temp) > 20 and log10(temp) < 22

    def test_B(self):
        assert fib_Error(200) == 9