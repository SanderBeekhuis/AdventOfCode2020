import functools

def run(file: str='input.txt'):
  lines = open(file, 'r').readlines()
  lines = map(lambda l: l.strip(), lines)

  result = map(__, lines)
  return result


if __name__ == "__main__":
  print(run())