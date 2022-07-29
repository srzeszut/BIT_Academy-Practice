import pytest
from robot import robot, robotStatus
from map_gen import BASIC_MAP

MIN_SIZE     = 3
MIN_CORD     = 0
MID_SIZE     = 10
MID_CORD     = 0
MAX_SIZE     = 100
MAX_CORD     = 0
FULL_BATTERY = 10 ** 6

set_UU = [(robot(BASIC_MAP(MIN_SIZE)[0], 0, 0, FULL_BATTERY).down(), robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], 1, 1, FULL_BATTERY).down(), robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], 2, 2, FULL_BATTERY).down(), robotStatus.CRASH)]
@pytest.mark.dependency(name="D_UU", depends=["constructor"], scope="session")
@pytest.mark.parametrize("input_t, output_t", set_UU)
def test_UU(input_t, output_t):
    assert input_t.get_status() == output_t

set_UM = [(robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).down(-100),  robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).down(-1),    robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).down(0),     robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).down(2),     robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).down(3),     robotStatus.CRASH),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).down(5),     robotStatus.CRASH),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).down(100),   robotStatus.CRASH)]
@pytest.mark.dependency(name="D_UM", depends=["D_UU"])
@pytest.mark.parametrize("input_t, output_t", set_UM)  
def test_UM(input_t, output_t):
    assert input_t.get_status() == output_t

set_MU = [(robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).down().down(),        robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).down().down().down(), robotStatus.CRASH)]
@pytest.mark.dependency(name="D_MU", depends=["D_UU"])
@pytest.mark.parametrize("input_t, output_t", set_MU)
def test_MU(input_t, output_t):
    assert input_t.get_status() == output_t

set_MM = [(robot(BASIC_MAP(MID_SIZE)[0], MID_CORD, MID_CORD, FULL_BATTERY).down(3).down(4),            robotStatus.ALIVE),
          (robot(BASIC_MAP(MID_SIZE)[0], MID_CORD, MID_CORD, FULL_BATTERY).down(7).down(5),            robotStatus.CRASH),
          (robot(BASIC_MAP(MAX_SIZE)[0], MAX_CORD, MAX_CORD, FULL_BATTERY).down(33).down(49),          robotStatus.ALIVE),
          (robot(BASIC_MAP(MAX_SIZE)[0], MAX_CORD, MAX_CORD, FULL_BATTERY).down(33).down(49).down(27), robotStatus.CRASH)]
@pytest.mark.dependency(name="D_MM", depends=["D_UM", "D_MU"])
@pytest.mark.parametrize("input_t, output_t", set_MM)
def test_MM(input_t, output_t):
    assert input_t.get_status() == output_t
