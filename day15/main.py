def run_naive(arg=(18, 11, 9, 0, 5, 1)):
    history = list(arg)

    while len(history) < 2020:
        history.append(answer(history))

    return history


def answer(history):
    try:
        second_last_idx = max(idx for idx, val in enumerate(history[:-1]) if val == history[-1])
        return len(history) - 1 - second_last_idx
    except ValueError:
        return 0


def run_fast(arg=(18, 11, 9, 0, 5, 1), goal=30_000_000):
    last_occurrence = {}

    # Init values
    for i, n in enumerate(arg):
        last_occurrence[n] = i+1

    turn = len(arg)
    last_spoken = arg[-1]

    print(last_occurrence)

    # Algorithm
    while turn < goal:
        new_spoken = turn - last_occurrence.get(last_spoken, turn)

        # Advance time
        last_occurrence[last_spoken] = turn
        last_spoken = new_spoken
        turn += 1

        if turn % 10_000 == 0:
            print(turn)

    return last_spoken


if __name__ == "__main__":
    print("Part 1: ", run_naive()[2019])
    print("Part 2: ", run_fast())
