import math


def rotate(point, angle):
    """
    Rotate a point counterclockwise by a given angle.

    The angle should be given in degrees.
    """
    px, py = point
    angle = math.radians(angle)

    qx = math.cos(angle) * px - math.sin(angle) * py
    qy = math.sin(angle) * px + math.cos(angle) * py
    return round(qx), round(qy)


class Ship:
    def __init__(self):
        self.direction = 0
        self.x = 0
        self.y = 0

    def north(self, arg):
        self.y += arg

    def south(self, arg):
        self.y -= arg

    def east(self, arg):
        self.x += arg

    def west(self, arg):
        self.x -= arg

    def right(self, arg):
        self.direction = (self.direction + arg) % 360

    def left(self, arg):
        self.direction = (self.direction - arg) % 360

    def forward(self, arg):
        if self.direction == 0:
            self.east(arg)
        elif self.direction == 90:
            self.south(arg)
        elif self.direction == 180:
            self.west(arg)
        elif self.direction == 270:
            self.north(arg)
        else:
            assert False, f'Unexpected direction {self.direction}'

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


class WaypointShip:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.waypoint_x = 10
        self.waypoint_y = 1

    def north(self, arg):
        self.waypoint_y += arg

    def south(self, arg):
        self.waypoint_y -= arg

    def east(self, arg):
        self.waypoint_x += arg

    def west(self, arg):
        self.waypoint_x -= arg

    def right(self, arg):
        self.left(-arg)

    def left(self, arg):
        self.waypoint_x, self.waypoint_y = rotate((self.waypoint_x, self.waypoint_y), arg)

    def forward(self, arg):
        self.x += arg * self.waypoint_x
        self.y += arg * self.waypoint_y

    def manhattan_distance(self):
        return abs(self.x) + abs(self.y)


def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = map(lambda l: l.strip(), lines)
    lines = list(lines)

    ship = Ship()
    move_ship(lines, ship)
    print('Part1:', ship.manhattan_distance())

    ship = WaypointShip()
    move_ship(lines, ship)
    print('Part2:', ship.manhattan_distance())


def move_ship(lines, ship):
    for line in lines:
        cmd, arg = line[0], int(line[1:])
        if cmd == 'N':
            ship.north(arg)
        elif cmd == 'E':
            ship.east(arg)
        elif cmd == 'W':
            ship.west(arg)
        elif cmd == 'S':
            ship.south(arg)
        elif cmd == 'F':
            ship.forward(arg)
        elif cmd == 'R':
            ship.right(arg)
        elif cmd == 'L':
            ship.left(arg)
        else:
            assert False, f"Unknown command {cmd}"


if __name__ == "__main__":
    run()
