from day17.main import ConwayGrid

import  pytest

@pytest.fixture
def cg():
    """"
    Creates basic ConwayGrid
    """
    return ConwayGrid(['.#.', '..#', '###'])

@pytest.fixture
def cg4d():
    """"
    Creates a 4dimensional ConwayGrid
    """
    return ConwayGrid(['.#.', '..#', '###'], dimensions=4)


def test_active_count(cg):
    assert cg.active_count() == 5


def test_update_generation(cg):
    cg.update_generation()
    assert cg.active_count() == 11

    for _ in range(5):
        cg.update_generation()

    assert cg.active_count() == 112


@pytest.mark.skip("slow")
def test_update_generation_4d(cg4d):
    for _ in range(6):
        cg4d.update_generation()

    assert cg4d.active_count() == 848
