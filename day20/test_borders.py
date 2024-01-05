import pytest

from day20.borders import OverlapDirections
from day20.main import Borders


def create_border():
    # a b
    # c d
    return Borders.create_from_tile(['ab', 'cd'])


@pytest.fixture()
def border():
    return create_border()



def test_rotate_border(border):
    # Goal:
    # d c
    # b a
    assert border.create_rotated() == Borders.create_from_tile(['dc', 'ba'])


def test_horizontal_flip(border):
    # Goal:
    # c d
    # a b
    assert border.create_horizontal_flipped() == Borders.create_from_tile(['cd', 'ab'])


def test_vertical_flip(border):
    # Goal:
    # b a
    # d c
    assert border.create_vertical_flipped() == Borders.create_from_tile(['ba', 'dc'])


def test_rotation_and_flip_twice_is_identity(border):
    assert border == border.create_horizontal_flipped().create_horizontal_flipped()
    assert border == border.create_vertical_flipped().create_vertical_flipped()
    assert border == border.create_rotated().create_rotated()


def test_order_of_flip_operations_invariant(border):
    vertical_horizontal_flipped = border.create_vertical_flipped().create_horizontal_flipped()
    horizontal_vertical_flipped = border.create_horizontal_flipped().create_vertical_flipped()
    assert vertical_horizontal_flipped == horizontal_vertical_flipped


def test_rotation_equals_two_flips(border):
    assert border.create_rotated() == border.create_vertical_flipped().create_horizontal_flipped()


@pytest.mark.parametrize('other_border, expected_overlap', [
        (create_border(), []),
        (create_border().create_vertical_flipped(), [OverlapDirections.EAST, OverlapDirections.WEST]),
        (create_border().create_horizontal_flipped(), [OverlapDirections.NORTH, OverlapDirections.SOUTH]),
        (Borders.create_from_tile(['xy', 'ab']), [OverlapDirections.NORTH]),
    ]
)
def test_overlap_directions(border, other_border, expected_overlap):
    assert border.overlap_directions(other_border) == expected_overlap

