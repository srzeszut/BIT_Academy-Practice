import pytest
from robot import robot, robotStatus
from map_gen import IN_MAP_SET, OUT_MAP_SET

FULL_BATTERY  = 10 ** 6
EMPTY_BATTERY = 2
ZERO_BATTERY  = 0

@pytest.mark.dependency(depends=["BATE"], scope="session")
def test_MAPA():
    robot_t = robot(IN_MAP_SET[0], 0, 0, FULL_BATTERY)
    robot_t.right().right().left().down(3).up()
    assert robot_t.get_map() == OUT_MAP_SET[0]

@pytest.mark.dependency(depends=["BATE"], scope="session")
def test_MAPB():
    robot_t = robot(IN_MAP_SET[1], 3, 0, FULL_BATTERY)
    robot_t.up().right().up().right()
    assert robot_t.get_map() == OUT_MAP_SET[1]

@pytest.mark.dependency(depends=["BATE"], scope="session")
def test_MAPC():
    robot_t = robot(IN_MAP_SET[2], 0, 0, FULL_BATTERY)
    robot_t.down().right(2).up()
    assert robot_t.get_map() == OUT_MAP_SET[2]

@pytest.mark.dependency(depends=["BATE"], scope="session")
def test_MAPD():
    robot_t = robot(IN_MAP_SET[3], 1, 1, FULL_BATTERY)
    robot_t.down(2).up().up().left().up().right()
    assert robot_t.get_map() == OUT_MAP_SET[3]

@pytest.mark.dependency(depends=["BATE"], scope="session")
def test_MAPE():
    robot_t = robot(IN_MAP_SET[4], 0, 1, FULL_BATTERY)
    robot_t.down(2).up().up().left().up().right()
    assert robot_t.get_map() == OUT_MAP_SET[4]

@pytest.mark.dependency(depends=["BATE"], scope="session")
def test_MAPF():
    robot_t = robot(IN_MAP_SET[5], 0, 1, EMPTY_BATTERY)
    robot_t.right(3).left(2).right(2).left(2).right(2).left(2).right(2).left(3)
    assert robot_t.get_map() == OUT_MAP_SET[5]

@pytest.mark.dependency(depends=["BATE"], scope="session")
def test_MAPG():
    robot_t = robot(IN_MAP_SET[6], 0, 0, FULL_BATTERY)
    robot_t.right(2137)
    assert robot_t.get_map() == OUT_MAP_SET[6]

@pytest.mark.dependency(depends=["BATE"], scope="session")
def test_MAPH():
    robot_t = robot(IN_MAP_SET[7], 0, 0, ZERO_BATTERY)
    assert robot_t.get_map()     == OUT_MAP_SET[7]
    assert robot_t.get_status()  == robotStatus.DEAD
    assert robot_t.get_battery() == 0