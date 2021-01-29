from itertools import chain

import lib
import re


def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = [line.strip() for line in lines]
    fields, my_ticket, nearby_tickets = lib.split_on_empty(lines)

    field_values = {}
    for field in fields:
        p = re.compile('(.*): (\\d*)-(\\d*) or (\\d*)-(\\d*)')
        field, start1, end1, start2, end2 = p.match(field).groups()
        field_values[field] = list(chain(
            range(int(start1), int(end1) + 1),
            range(int(start2), int(end2) + 1)
        ))

    error_rate = 0
    valid_tickets = []
    for ticket in nearby_tickets[1:]:  # Skip first line
        fields = [int(i) for i in ticket.split(',')]
        valid = True
        for field in fields:
            if not any(field in r for r in field_values.values()):
                error_rate += field
                valid = False
        if valid:
            valid_tickets.append(fields)

    print("Part 1:", error_rate)

    possible_fields = []
    for i in range(len(valid_tickets[0])):
        values = [ticket[i] for ticket in valid_tickets]
        possible_fields.append([field for field in field_values if all(v in field_values[field] for v in values)])

    certain_fields = {}
    found = True
    while found:
        found = False
        for i, fields in enumerate(possible_fields):
            if len(fields) == 1:
                found = True
                chosen_field = fields[0]
                certain_fields[chosen_field] = i
                for fields in possible_fields:
                    try:
                        fields.remove(chosen_field)
                    except ValueError:
                        pass
                break

    my_ticket = [int(i) for i in my_ticket[1].split(',')]
    print(
        "Part 2:",
        my_ticket[certain_fields['departure location']] *
        my_ticket[certain_fields['departure station']] *
        my_ticket[certain_fields['departure platform']] *
        my_ticket[certain_fields['departure track']] *
        my_ticket[certain_fields['departure date']] *
        my_ticket[certain_fields['departure time']]
    )


if __name__ == "__main__":
    run()
