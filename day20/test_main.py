import pytest

from day20.main import Tile, Borders


@pytest.fixture
def tile_2311():
    return Tile([
        'Tile 2311:',
        '..##.#..#.',
        '##..#.....',
        '#...##..#.',
        '####.#...#',
        '##.##.###.',
        '##...#.###',
        '.#.#.#..##',
        '..#....#..',
        '###...#.#.',
        '..###..###',
    ])


@pytest.fixture
def tile_1951():
    return Tile([
        'Tile 1951:',
        '#.##...##.',
        '#.####...#',
        '.....#..##',
        '#...######',
        '.##.#....#',
        '.###.#####',
        '###.##.##.',
        '.###....#.',
        '..#.#..#.#',
        '#...##.#..',
    ])


def test_create_tile(tile_2311):
    assert tile_2311.id == 2311
    assert tile_2311.borders == Borders(
        top='..##.#..#.',
        right='...#.##..#',
        bottom='..###..###',
        left='.#####..#.'
    )


def test_borders_inequality(tile_2311):
    assert tile_2311.borders != Borders(
        top='..##.#..#.',
        right='...#.##..#',
        bottom='..###X.###',
        left='.#####..#.'
    )


def test_can_be_neighbours(tile_2311, tile_1951):
    assert tile_2311.can_be_neighbours(tile_1951)
