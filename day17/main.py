import itertools
from collections import defaultdict


def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = [line.strip() for line in lines]

    cg = ConwayGrid(lines)
    cg4d = ConwayGrid(lines, dimensions=4)

    for _ in range(6):
        cg.update_generation()
        cg4d.update_generation()

    print(f'Part 1: {cg.active_count()}')
    print(f'Part 2: {cg4d.active_count()}')


class ConwayGrid:
    def __init__(self, initialization, dimensions=3):
        """
        @param initialization: A 2D-text grid representing initial state

        """
        assert dimensions >= 2, "Algorithms break down in less then two dimensions"

        self.bounds = [range(len(initialization[0])), range(len(initialization))] + [range(1)] * (dimensions-2)
        self.is_active = defaultdict(lambda: False)  # Grid defaults as inactive

        for x, y in itertools.product(*self.bounds[:2]):
            self.is_active[(x, y) + (0,) * (dimensions-2)] = initialization[y][x] == '#'

    def active_count(self):
        # Abuse that True=1 and False=0
        return sum(self.is_active.values())

    def update_generation(self):
        self.bounds = list(map(expand_range, self.bounds))

        new_is_active = defaultdict(lambda: False)

        for cube in itertools.product(*self.bounds):

            neighbours = filter(lambda n: n != cube, itertools.product(*[range(c - 1, c + 2) for c in cube]))

            active_neighbours = sum(self.is_active[n] for n in neighbours)
            new_is_active[cube] = active_neighbours == 3 or (self.is_active[cube] and active_neighbours == 2)

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
