from function import square
# Napisać cztery testy z dla funckji square dla 0, 1, -1 i 100
def test1():
    assert square(0)==0

def test2():
    assert square(1)==1

def test3():
    assert square(-1)==1

def test4():
    assert square(100)==10000