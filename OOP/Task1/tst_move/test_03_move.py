import pytest
from robot import robot, robotStatus
from map_gen import MAP_SET


@pytest.mark.dependency(depends=["D_MM",
                                 "U_MM",
                                 "L_MM",
                                 "R_MM"],
                        scope="session")
def test_UU():
    assert 1 == 2