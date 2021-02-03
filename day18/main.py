def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = [line.strip() for line in lines]

    print(f'Part 1: {sum(map(compute, lines))}')
    print(f'Part 2: {sum(map(compute_advanced, lines))}')


def compute(line):
    acc = 0
    next_op = None
    while line:
        if line[0] in '*+':
            next_op = line[0]
            line = line[2:]

        if line[0] == '(':
            i = matching_bracket_index(line)
            head, line = line[1:i], line[i+1:]
            head = compute(head)
            line = line.strip()
        else:  # Start with an integer
            if ' ' in line:
                head, line = line.split(' ', maxsplit=1)
                head = int(head)
            else:
                head, line = int(line), ''

        if next_op == '*':
            acc *= head
        elif next_op == '+':
            acc += head
        else:
            acc = head

    return acc


def compute_advanced(line):
    acc = 0
    next_op = None
    while line:
        line = line.strip()

        if line[0] in '*+':
            next_op = line[0]
            line = line[2:]

        if next_op == '*':
            if i := matching_top_level_star(line):
                head, line = line[0:i], line[i + 1:]
                head = compute_advanced(head)
            else:
                head, line = compute_advanced(line), ''
        elif line[0] == '(':
            i = matching_bracket_index(line)
            head, line = line[1:i], line[i+1:]
            head = compute_advanced(head)

        else:
            if ' ' in line:
                head, line = line.split(' ', maxsplit=1)
                head = int(head)
            else:
                head, line = int(line), ''

        if next_op == '*':
            acc *= head
        elif next_op == '+':
            acc += head
        else:
            acc = head

    return acc


def matching_top_level_star(line):
    """
    Finds the index of the first matching star not enclosed in brackets
    """

    # Find matching close:
    open_brackets = 0
    for i, c in enumerate(line):
        if c == '(':
            open_brackets += 1
        if c == ')':
            open_brackets -= 1
        if c == '*' and open_brackets == 0:
            return i

    return None


def matching_bracket_index(line):
    """
    Finds the index of the first top level closing bracket of `line`
    """

    # Find matching close:
    open_brackets = 0
    for i, c in enumerate(line):
        if c == '(':
            open_brackets += 1
        if c == ')':
            open_brackets -= 1
            if open_brackets == 0:
                return i

    assert False, "NoMatchingBracketFound"


if __name__ == "__main__":
    run()
