from function import square
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100 
def test_A():
    assert square(0) == 0

def test_B():
    assert square(1) == 1

def test_C():
    assert square(-1) == 1

def test_D():
    assert square(100) == 10000