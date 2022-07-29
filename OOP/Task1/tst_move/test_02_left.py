import pytest
from robot import robot, robotStatus
from map_gen import BASIC_MAP

MIN_SIZE     = 3
MIN_CORD     = MIN_SIZE - 1
MID_SIZE     = 10
MID_CORD     = MID_SIZE - 1
MAX_SIZE     = 100
MAX_CORD     = MAX_SIZE - 1
FULL_BATTERY = 10 ** 6

set_UU = [(robot(BASIC_MAP(MIN_SIZE)[0], 2, 2, FULL_BATTERY).left(), robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], 1, 1, FULL_BATTERY).left(), robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], 0, 0, FULL_BATTERY).left(), robotStatus.CRASH)]
@pytest.mark.dependency(name="L_UU", depends=["constructor"], scope="session")
@pytest.mark.parametrize("input_t, output_t", set_UU)
def test_UU(input_t, output_t):
    assert input_t.get_status() == output_t

set_UM = [(robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).left(-100),  robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).left(-1),    robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).left(0),     robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).left(2),     robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).left(3),     robotStatus.CRASH),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).left(5),     robotStatus.CRASH),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).left(100),   robotStatus.CRASH)]
@pytest.mark.dependency(name="L_UM", depends=["L_UU"])
@pytest.mark.parametrize("input_t, output_t", set_UM)  
def test_UM(input_t, output_t):
    assert input_t.get_status() == output_t

set_MU = [(robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).left().left(),        robotStatus.ALIVE),
          (robot(BASIC_MAP(MIN_SIZE)[0], MIN_CORD, MIN_CORD, FULL_BATTERY).left().left().left(), robotStatus.CRASH)]
@pytest.mark.dependency(name="L_MU", depends=["L_UU"])
@pytest.mark.parametrize("input_t, output_t", set_MU)
def test_MU(input_t, output_t):
    assert input_t.get_status() == output_t

set_MM = [(robot(BASIC_MAP(MID_SIZE)[0], MID_CORD, MID_CORD, FULL_BATTERY).left(3).left(4),            robotStatus.ALIVE),
          (robot(BASIC_MAP(MID_SIZE)[0], MID_CORD, MID_CORD, FULL_BATTERY).left(7).left(5),            robotStatus.CRASH),
          (robot(BASIC_MAP(MAX_SIZE)[0], MAX_CORD, MAX_CORD, FULL_BATTERY).left(33).left(49),          robotStatus.ALIVE),
          (robot(BASIC_MAP(MAX_SIZE)[0], MAX_CORD, MAX_CORD, FULL_BATTERY).left(33).left(49).left(27), robotStatus.CRASH)]
@pytest.mark.dependency(name="L_MM", depends=["L_UM", "L_MU"], scope="session")
@pytest.mark.parametrize("input_t, output_t", set_MM)
def test_MM(input_t, output_t):
    assert input_t.get_status() == output_t
