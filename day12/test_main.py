from day12.main import Ship, rotate, WaypointShip


def test_ship():
    ship = Ship()
    ship.forward(10)
    assert ship.x == 10
    ship.north(3)
    assert ship.y == 3
    ship.forward(7)
    assert ship.x == 17
    ship.right(90)
    assert ship.direction == 90
    ship.forward(11)
    assert ship.y == -8

    assert ship.manhattan_distance() == 25


def test_waypoint_ship():
    ship = WaypointShip()
    ship.forward(10)
    assert ship.x == 100
    assert ship.y == 10
    ship.north(3)
    assert ship.waypoint_y == 4
    ship.forward(7)
    assert (10, 4) == (ship.waypoint_x, ship.waypoint_y)
    ship.right(90)
    assert (4, -10) == (ship.waypoint_x, ship.waypoint_y)
    ship.forward(11)
    assert ship.x == 214
    assert ship.y == -72
    assert ship.waypoint_x == 4
    assert ship.waypoint_y == -10
    assert ship.manhattan_distance() == 286

def test_rotate():
    assert rotate((1, 0), 90) == (0, 1)
    assert rotate((1, 0), 180) == (-1, 0)

