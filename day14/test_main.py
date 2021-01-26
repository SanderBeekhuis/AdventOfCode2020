import pytest

import day14.main


@pytest.mark.parametrize("x,expectation", [
    (11, 73),
    (101, 101),
    (0, 64)
])
def test_mask(x, expectation):
    assert day14.main.mask(x, ones_mask=64, zeros_mask=2) == expectation


def test_compute_masks():
    assert day14.main.compute_masks('XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == (64, 2)


def test_compute_part2_masks():
    ones_mask, float_masks =  day14.main.compute_part2_masks('000000000000000000000000000000X1001X')
    assert ones_mask == 18
    assert float_masks == [33, 32, 1, 0]
