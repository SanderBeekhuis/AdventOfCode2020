import functools

class InvalidNumberException(Exception): 
  pass

def run(file: str='input.txt'):
  lines = open(file, 'r').readlines()
  lines = map(lambda l: l.strip(), lines)
  lines = map(int, lines)
  lines = list(lines)

  index = 25 # Skip preamble
  weakness = 0 

  while True:
    if test_valid(lines, index):
      index += 1
    else:
      weakness = lines[index]
      print("Part 1:", weakness)
      break

  range_size = 2
  while True:
    for i in range(len(lines)-range_size):
      test_range = lines[i:i+range_size]
      if weakness == sum(test_range):
        print(f"Part 2: \n Max: {max(test_range)} \n Min: {min(test_range)} \n Solution: {max(test_range) + min(test_range)}")
        return

    range_size += 1


def test_valid(lines, index):
  for i in range(1, 26):
    for j in range(i):
      if lines[index-i] + lines[index - j] == lines[index]:
        return True

  return False

if __name__ == "__main__":
  run()