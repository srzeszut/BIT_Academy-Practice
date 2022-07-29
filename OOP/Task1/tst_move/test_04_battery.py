import pytest
from robot import robot, robotStatus
from map_gen import BASIC_MAP

# AREA_SIZE = 100

# set_SO = [(robot(BASIC_MAPS[AREA_SIZE][0]), 2)]
# @pytest.mark.dependency(depends=["test_down.py"], scope="session")
# @pytest.mark.parametrize("input_t, output_t", set_SO)
# def test_SO(input_t, output_t):
#     assert input_t == output_t