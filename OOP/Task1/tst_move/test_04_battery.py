import pytest
from robot import robot, robotStatus
from map_gen import MAP_SET, BASIC_MAP

BATTERY_A_START_VAL = 13
@pytest.mark.dependency(name="BATA", depends=["MVB", "MVC"], scope="session")
def test_BATA():
    robot_t = robot(BASIC_MAP(20)[0], 0, 0, BATTERY_A_START_VAL)
    for i in range(1, 13):
        robot_t.right()
        assert robot_t.get_battery() == BATTERY_A_START_VAL - i
        assert robot_t.get_status()  == robotStatus.ALIVE
    
    for i in range(20):
        robot_t.right()
        assert robot_t.get_battery() == 0
        assert robot_t.get_status()  == robotStatus.DEAD

    assert (robot_t.get_x(), robot_t.get_y()) == (0, 13)

BATTERY_B_START_VAL = 2
BATTERY_B_PICK_VAL  = 11
BATTERY_B_END_VAL   = 9
@pytest.mark.dependency(name="BATB", depends=["MVB", "MVC"], scope="session")
def test_BATB():
    robot_t = robot(MAP_SET[2], 3, 0, BATTERY_B_START_VAL)
    robot_t.up()
    assert robot_t.get_battery() == BATTERY_B_PICK_VAL
    
    for _ in range(20):
        robot_t.right(2).left(2)

    assert robot_t.get_battery() == BATTERY_B_END_VAL
    assert robot_t.get_status()  == robotStatus.CRASH
    
BATTERY_C_START_VAL = 2
BATTERY_C_END_VAL   = 8
@pytest.mark.dependency(name="BATC", depends=["MVB", "MVC"], scope="session")
def test_BATC():
    robot_t = robot(MAP_SET[3], 2, 1, BATTERY_C_START_VAL)
    robot_t.left().down().up().right()

    assert robot_t.get_status()  == robotStatus.ALIVE
    assert robot_t.get_battery() == BATTERY_C_END_VAL

LOOP_D_CONST        = 49
BATTERY_D_START_VAL = 10 ** 4
MAP_SIZE            = 10 ** 2
BATTERY_D_END_VAL   = 100000
def f(val): return val == BATTERY_D_START_VAL
def g(val): return val > BATTERY_D_START_VAL
set_BATD = [(robot(BASIC_MAP(MAP_SIZE)[1], 0, 0, BATTERY_D_START_VAL), f, robotStatus.WATER, robotStatus.WATER),
            (robot(BASIC_MAP(MAP_SIZE)[2], 0, 0, BATTERY_D_START_VAL), f, robotStatus.CRASH, robotStatus.CRASH),
            (robot(BASIC_MAP(MAP_SIZE)[3], 0, 0, BATTERY_D_START_VAL), g, robotStatus.ALIVE, robotStatus.CRASH)]
@pytest.mark.dependency(name="BATD", depends=["BATA", "BATB", "BATC"], scope="session")
@pytest.mark.parametrize("robot_t, func_t, status_ta, status_tb", set_BATD)
def test_BATD(robot_t, func_t, status_ta, status_tb):
    for _ in range(LOOP_D_CONST):
        robot_t.right(MAP_SIZE - 1).down().left(MAP_SIZE - 1).down()
        assert func_t(robot_t.get_battery())
        assert robot_t.get_status() == status_ta
    robot_t.right(MAP_SIZE - 1).down().left(MAP_SIZE - 1).down()
    assert robot_t.get_status() == status_tb
    if status_ta == robotStatus.ALIVE:
        assert robot_t.get_battery() == BATTERY_D_END_VAL
        assert (robot_t.get_x(), robot_t.get_y()) == (MAP_SIZE - 1, 0)

LOOP_E_CONST        = 50
BATTERY_E_START_VAL = 10 ** 5
BATTERY_E_END_VAL   = 90001
@pytest.mark.dependency(name="BATE", depends=["BATD"], scope="session")
def test_BATE():
    robot_t = robot(BASIC_MAP(MAP_SIZE)[0], 0, 0, BATTERY_E_START_VAL)
    for i in range(1, LOOP_E_CONST):
        robot_t.right(MAP_SIZE - 1).down().left(MAP_SIZE - 1).down()
        assert robot_t.get_battery() == BATTERY_E_START_VAL - 2 * (i * MAP_SIZE)
        assert robot_t.get_status()  == robotStatus.ALIVE

    robot_t.right(MAP_SIZE - 1).down().left(MAP_SIZE - 1)
    assert robot_t.get_battery() == BATTERY_E_END_VAL
    assert robot_t.get_status()  == robotStatus.ALIVE
