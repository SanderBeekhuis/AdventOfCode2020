import pytest

import day10.main


@pytest.mark.parametrize('line,expected',
                         [
                             ([0, 1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19, 22], 8),
                         ]
                         )
def test_part2(line, expected):
    assert expected == day10.main.part_2(line)
