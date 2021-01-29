def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = [line.strip() for line in lines]


if __name__ == "__main__":
    run()
