import lib
import re


def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = [line.strip() for line in lines]
    fields, _, nearby_tickets = lib.split_on_empty(lines)

    valid_ranges = []
    for field in fields:
        p = re.compile('.*: (\\d*)-(\\d*) or (\\d*)-(\\d*)')
        start1, end1, start2, end2 = p.match(field).groups()
        valid_ranges += [range(int(start1), int(end1) + 1), range(int(start2), int(end2) + 1)]

    error_rate = 0
    for ticket in nearby_tickets[1:]: # Skip first line
        fields = [int(i) for i in ticket.split(',')]
        for field in fields:
            if not any((field in r for r in valid_ranges)):
                error_rate += field

    print(error_rate)


if __name__ == "__main__":
    run()
