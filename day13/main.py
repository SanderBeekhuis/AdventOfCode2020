def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = map(lambda l: l.strip(), lines)
    lines = list(lines)

    time = int(lines[0])
    busses = lines[1].split(',')
    busses = [int(b) for b in busses if b != 'x']

    wait_times = [b - (time % b) for b in busses]
    print(busses)
    print(wait_times)

    wait_time = min(wait_times)
    bus_id = busses[wait_times.index(wait_time)]

    print("Part1: ", wait_time * bus_id)


if __name__ == "__main__":
    run()
