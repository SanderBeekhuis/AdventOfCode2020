import lib
from day20.borders import Borders


def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = [line.strip() for line in lines]
    tiles = [Tile(strings) for strings in lib.split_on_empty(lines)]

    for tile in tiles:
        print(tile)
        for other_tile in tiles:
            if tile is other_tile:
                continue

            if len(tile.can_be_neighbours(other_tile)) > 0:
                print(f'- {other_tile}')


class Tile:
    def __init__(self, tile):
        title, rows = tile[0], tile[1:]
        self.id = int(title[5:9])

        self.borders = Borders.create_from_tile(rows)
        self.border_states = {
            'normal': self.borders,
            'horizontal_flip': self.borders.create_horizontal_flipped(),
            'vertical_flip': self.borders.create_vertical_flipped(),
            'rotated': self.borders.create_rotated()
        }

    def __str__(self):
        return f'{self.__class__.__name__}(id={self.id})'

    def can_be_neighbours(self, other):
        options = []

        for state, borders in self.border_states.items():
            for other_state, other_borders in other.border_states.items():
                if overlap := borders.overlap_directions(other_borders):
                    options.append((state, other_state, overlap))

        return options


if __name__ == "__main__":
    run()
