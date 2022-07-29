import pytest
from robot import robot, robotStatus
from map_gen import BASIC_MAP

FULL_BATTERY = 10 ** 6

set_R = [(robot(BASIC_MAP(1)[0], 0, 0, FULL_BATTERY), robotStatus.ALIVE),
         (robot(BASIC_MAP(1)[1], 0, 0, FULL_BATTERY), robotStatus.WATER),
         (robot(BASIC_MAP(1)[2], 0, 0, FULL_BATTERY), robotStatus.CRASH)]
@pytest.mark.dependency(name="constructor", scope="session")
@pytest.mark.parametrize("input_t, output_t", set_R)
def test_R(input_t, output_t):
    assert input_t.get_status() == output_t
