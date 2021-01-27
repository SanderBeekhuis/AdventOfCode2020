from day15.main import run_naive, run_fast


def test_run():
    assert run_naive([0, 3, 6])[:10] == [0, 3, 6, 0, 3, 3, 1, 0, 4, 0]


def test_run_fast():
    assert run_fast([0, 3, 6], goal=4) == 0
    assert run_fast([0, 3, 6], goal=5) == 3
    assert run_fast([0, 3, 6], goal=9) == 4
