from cmplex import C
import pytest

# Napisać testy sprawdzające dodawanie liczb zespolonych
# w załączonym pliku
results=[(1,2,3,4,4,6),
         (1,2,3,4,4,6),
         (1,2,3,4,4,6),
         (1,2,3,4,4,6),
         (1,2,3,4,4,6),]
@pytest.mark.parametrize('re_x,im_x,re_y,im_y,re_res,im_res',results)
def test_add_complex(re_x,im_x,re_y,im_y,re_res,im_res):
    assert C(re_x,im_x)+C(re_y,im_y)==C(re_res,im_res)
