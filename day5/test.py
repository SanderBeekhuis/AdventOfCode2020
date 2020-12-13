import pytest

import main

def test_row():
    assert main.row('FBFBBFF') == 44

def test_collumn():
    assert main.collumn('RLR') == 5

@pytest.mark.parametrize(
    "input,expected", [
        ("BFFFBBFRRR", 567),
        ("FFFBBBFRRR", 119)
    ]
)
def test_seat_id(input, expected):
    assert main.seat_id(input) == expected