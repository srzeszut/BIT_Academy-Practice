from function import is_prime
from random import randint
import pytest

class TestMini:
    # Napisać testy sprawdzające funkcję is_prime dla liczb
    # z przedziału <-1, 6>
   primes_mini=[(-1,True),
           (0,False),
           (1,False),
           (2,True),
           (3,True),
           (4,False),
           (5,True),
           (6,False),]

   @pytest.mark.parametrize('number,prime',primes_mini)
   def test_mini_primes(self,number,prime):
       assert is_prime(number)==prime



class TestMid:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # liczb z przedziału <10 ** 4, 10 ** 5>
    primes_mid = [(-1, True),
              (0, False),
              (1, False),
              (2, True),
              (3, True)]

    @pytest.mark.parametrize('number,prime', primes_mid)
    def test_mini_primes(self, number, prime):
        assert is_prime(number) == prime


class TestMaxi:
    # Napisać 5 testów sprawdzających funkcję is_prime dla losowych
    # z przedziału <10 ** 12, 10 ** 13>, a następnie
    # naprawić funkcję is_prime aby testy wykonywały się szybciej
    # niż dla aktualnej funkcji
    primes_maxi = [(-1, True),
                  (0, False),
                  (1, False),
                  (2, True),
                  (3, True)]

    @pytest.mark.parametrize('number,prime', primes_maxi)
    def test_mini_primes(self, number, prime):
        assert is_prime(number) == prime