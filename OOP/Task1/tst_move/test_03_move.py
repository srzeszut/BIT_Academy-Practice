import pytest
from robot import robot, robotStatus
from map_gen import MAP_SET, DIV_SET

FULL_BATTERY = 10 ** 6

set_MVA = [# Right
          (robot(DIV_SET[0],  0, 0, FULL_BATTERY).right(), (0, 1), robotStatus.WATER),
          (robot(DIV_SET[1],  0, 0, FULL_BATTERY).right(), (0, 0), robotStatus.CRASH),
          (robot(DIV_SET[2],  0, 0, FULL_BATTERY).right(), (0, 1), robotStatus.ALIVE),
          (robot(DIV_SET[3],  0, 0, FULL_BATTERY).right(), (0, 0), robotStatus.CRASH),
          # Left
          (robot(DIV_SET[4],  0, 1, FULL_BATTERY).left(),  (0, 0), robotStatus.WATER),
          (robot(DIV_SET[5],  0, 1, FULL_BATTERY).left(),  (0, 1), robotStatus.CRASH),
          (robot(DIV_SET[6],  0, 1, FULL_BATTERY).left(),  (0, 0), robotStatus.ALIVE),
          (robot(DIV_SET[7],  0, 0, FULL_BATTERY).left(),  (0, 0), robotStatus.CRASH),
          # Down
          (robot(DIV_SET[8],  0, 0, FULL_BATTERY).down(),  (1, 0), robotStatus.WATER),
          (robot(DIV_SET[9],  0, 0, FULL_BATTERY).down(),  (0, 0), robotStatus.CRASH),
          (robot(DIV_SET[10], 0, 0, FULL_BATTERY).down(),  (1, 0), robotStatus.ALIVE),
          (robot(DIV_SET[11], 0, 0, FULL_BATTERY).down(),  (0, 0), robotStatus.CRASH),
          # Up
          (robot(DIV_SET[12], 1, 0, FULL_BATTERY).up(),    (0, 0), robotStatus.WATER),
          (robot(DIV_SET[13], 1, 0, FULL_BATTERY).up(),    (1, 0), robotStatus.CRASH),
          (robot(DIV_SET[14], 1, 0, FULL_BATTERY).up(),    (0, 0), robotStatus.ALIVE),
          (robot(DIV_SET[15], 0, 0, FULL_BATTERY).up(),    (0, 0), robotStatus.CRASH),]
@pytest.mark.dependency(
    name="MVA",
    depends=[
        "D_UU",
        "U_UU",
        "L_UU",
        "R_UU"],
    scope="session")
@pytest.mark.parametrize("robot_t, cord_t, status_t", set_MVA)
def test_MVA(robot_t, cord_t, status_t):
    assert (robot_t.get_x(), robot_t.get_y()) == cord_t
    assert robot_t.get_status() == status_t

MVB_CORD_START = (3, 2)
MVB_CORD_END   = (2, 1)
@pytest.mark.dependency(name="MVB", depends=["MVA"], scope="session")
def test_MVB():
    robot_t = robot(MAP_SET[0], MVB_CORD_START[0], MVB_CORD_START[1], FULL_BATTERY)
    for _ in range(10000):
        robot_t.left().right().right().left()
    assert robot_t.get_status() == robotStatus.ALIVE
    assert (robot_t.get_x(), robot_t.get_y()) == MVB_CORD_START

    for _ in range(10000):
        robot_t.left(2).right(2)
    assert robot_t.get_status() == robotStatus.ALIVE
    assert (robot_t.get_x(), robot_t.get_y()) == MVB_CORD_START

    robot_t.left().up().right().up()
    assert robot_t.get_status() == robotStatus.CRASH
    assert (robot_t.get_x(), robot_t.get_y()) == MVB_CORD_END

MVC_CORD_START = (0, 0)
MVC_CORD_END   = (1, 1)
@pytest.mark.dependency(name="MVC", depends=["MVA"], scope="session")
def test_MVC():
    robot_t = robot(MAP_SET[1], MVC_CORD_START[0], MVC_CORD_START[1], FULL_BATTERY)
    for _ in range(10000):
        robot_t.right(3).left(3).down(3).up(3)
    
    assert robot_t.get_status() == robotStatus.ALIVE
    assert (robot_t.get_x(), robot_t.get_y()) == MVC_CORD_START

    for _ in range(10000):
        robot_t.down(3).right(3).up(3).left(3)
    
    assert robot_t.get_status() == robotStatus.ALIVE
    assert (robot_t.get_x(), robot_t.get_y()) == MVC_CORD_START

    robot_t.down().right().up().left()

    assert robot_t.get_status() == robotStatus.WATER
    assert (robot_t.get_x(), robot_t.get_y()) == MVC_CORD_END

    for _ in range(10000):
        robot_t.right(3).down(3).left(3).up(3)

    assert robot_t.get_status() == robotStatus.WATER
    assert (robot_t.get_x(), robot_t.get_y()) == MVC_CORD_END

    for _ in range(10000):
        robot_t.down(3).right(3).up(3).left(3)
    
    assert robot_t.get_status() == robotStatus.WATER
    assert (robot_t.get_x(), robot_t.get_y()) == MVC_CORD_END
