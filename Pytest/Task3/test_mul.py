from cmplex import C
from random import randint
import pytest

# Napisać testy sprawdzające mnożenie liczb zespolonych
# w załączonym pliku
results=[]
for i in range(5):
    x1=randint(10**i,10**(i+1))
    x2 = randint(10 ** i, 10 ** (i + 1))
    y1=randint(10**i,10**(i+1))
    y2 = randint(10 ** i, 10 ** (i + 1))
    results.append((x1,x2,y1,y2,x1*y1-x2*y2,x1*y2+y1*x2))
@pytest.mark.parametrize('re_x,im_x,re_y,im_y,re_res,im_res',results)
def test_add_complex(re_x,im_x,re_y,im_y,re_res,im_res):
    assert C(re_x,im_x)*C(re_y,im_y)==C(re_res,im_res)