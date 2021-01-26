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


def compute_masks(arg):
    ones_mask = int(arg.replace('X', '0'), base=2)
    zeros_mask = int(arg.replace('1', 'X').replace('0', '1').replace('X', '0'), base=2)

    return ones_mask, zeros_mask


def mask(x, ones_mask, zeros_mask):
    return (x | ones_mask) - (x & zeros_mask)


if __name__ == "__main__":
    run()
