import sympy.ntheory.modular


def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = map(lambda l: l.strip(), lines)
    lines = list(lines)

    time = int(lines[0])
    busses = lines[1].split(',')
    known_busses = [int(b) for b in busses if b != 'x']

    wait_times = [b - (time % b) for b in known_busses]

    wait_time = min(wait_times)
    bus_id = known_busses[wait_times.index(wait_time)]

    print("Part1: ", wait_time * bus_id)

    print("Part2: ", part_2(busses))


def part_2(busses):
    """Use sympy's Chines reaminder theorem implementation to solve a system of equations

    time + offset_i = 0 mod bus_id

    We rewite this to the expected form of:
    time = v[i] mod m[i]
    like:
    time = -offset_i mod bus_id
    """

    m = []
    v = []
    offset = -1
    for bus in busses:
        offset += 1
        if bus == 'x':
            continue
        m.append(int(bus))
        v.append(-offset)
    time, _ = sympy.ntheory.modular.crt(m, v)
    return time


if __name__ == "__main__":
    run()
