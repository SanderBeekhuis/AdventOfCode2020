import itertools


def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = map(lambda l: l.strip(), lines)
    lines = list(lines)

    masks = 0, 0
    mem = {}

    for line in lines:
        cmd, arg = line.split(' = ')

        if cmd == 'mask':
            masks = compute_masks(arg)
        else:
            index = int(cmd[4:-1])
            mem[index] = mask(int(arg), *masks)

    print(f'Part 1: {sum(mem.values())}')

    mem = {}
    masks = 0, []
    for line in lines:
        cmd, arg = line.split(' = ')

        if cmd == 'mask':
            masks = compute_part2_masks(arg)
        else:
            index = int(cmd[4:-1]) | masks[0]
            for float_mask in masks[1]:
                mem[index ^ float_mask] = int(arg)

    print(f'Part 2: {sum(mem.values())}')


def compute_masks(arg):
    ones_mask = int(arg.replace('X', '0'), base=2)
    zeros_mask = int(arg.replace('1', 'X').replace('0', '1').replace('X', '0'), base=2)

    return ones_mask, zeros_mask


def compute_part2_masks(arg):
    ones_mask = int(arg.replace('X', '0'), base=2)

    float_values = [2 ** i for i, arg in zip(reversed(range(36)), arg) if arg == 'X']
    permutations = itertools.product([True, False], repeat=len(float_values))
    float_masks = [sum([t for p, t in zip(per, float_values) if p]) for per in permutations]

    return ones_mask, float_masks


def mask(x, ones_mask, zeros_mask):
    return (x | ones_mask) - (x & zeros_mask)


if __name__ == "__main__":
    run()
