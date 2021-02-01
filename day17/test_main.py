from day17.main import ConwayGrid

import  pytest

@pytest.fixture
def cg():
    """"
    Creates basic ConwayGrid
    """
    return ConwayGrid(['.#.', '..#', '###'])


def test_active_count(cg):
    assert cg.active_count() == 5


def test_update_generation(cg):
    cg.update_generation()
    assert cg.active_count() == 11

    for _ in range(5):
        cg.update_generation()

    assert cg.active_count() == 112
