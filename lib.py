from functools import reduce


def split_on_empty(lines):
    return reduce(_add_line_or_start_new_list, lines, [[]])


def _add_line_or_start_new_list(acc: list, line: str) -> list:
    if line == '':
        acc.append([])
    else:
        acc[-1].append(line)
    return acc
