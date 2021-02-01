from day17.main import ConwayGrid


def test_active_count():
    cg = ConwayGrid(['.#.', '..#', '###'])
    assert cg.active_count() == 5
