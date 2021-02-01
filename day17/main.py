import itertools
from collections import defaultdict


def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = [line.strip() for line in lines]

    cg = ConwayGrid(lines)
    for _ in range(6):
        cg.update_generation()
    print(f'Part 1: {cg.active_count()}')


class ConwayGrid:

    def __init__(self, lines):
        self.z_bounds = range(1)
        self.y_bounds = range(len(lines))
        self.x_bounds = range(len(lines[0]))
        self.is_active = defaultdict(lambda: False)  # Grid defaults as inactive

        for x, y in itertools.product(self.x_bounds, self.y_bounds):
            self.is_active[x, y, 0] = lines[y][x] == '#'

    def active_count(self):
        # Abuse that True=1 and False=0
        return sum(self.is_active.values())

    def update_generation(self):
        self.x_bounds = expand_range(self.x_bounds)
        self.y_bounds = expand_range(self.y_bounds)
        self.z_bounds = expand_range(self.z_bounds)

        new_is_active = defaultdict(lambda: False)

        for x, y, z in itertools.product(self.x_bounds, self.y_bounds, self.z_bounds):
            neighbours = list(filter(lambda n: n != (x, y, z),
                                     itertools.product(range(x - 1, x + 2), range(y - 1, y + 2), range(z - 1, z + 2))))

            active_neighbours = sum(self.is_active[n] for n in neighbours)
            new_is_active[x, y, z] = active_neighbours == 3 or (self.is_active[x, y, z] and active_neighbours == 2)

        self.is_active = new_is_active


def expand_range(r):
    """
    Returns a range that's 1 larger on both sides

    >>> expand_range(range(0, 2))
    range(-1, 3)
    """
    return range(min(r) - 1, max(r) + 2)


if __name__ == "__main__":
    run()
