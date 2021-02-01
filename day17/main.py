from collections import defaultdict


def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = [line.strip() for line in lines]

    cg = ConwayGrid(lines)


class ConwayGrid:

    def __init__(self, lines):
        self.z_bounds = range(1)
        self.y_bounds = range(len(lines))
        self.x_bounds = range(len(lines[0]))
        self.is_active = defaultdict(lambda _ : False) # Grid defaults as inactive

        for x in self.x_bounds:
            for y in self.y_bounds:
                self.is_active[x, y, 0] = lines[y][x] == '#'

    def active_count(self):
        # Abuse that True=1 and False=0
        return sum(self.is_active.values())


if __name__ == "__main__":
    run()
