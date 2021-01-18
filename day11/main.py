import functools
import itertools
import copy
from pprint import pprint

def run(file: str='day11/input.txt'):
  lines = open(file, 'r').readlines()
  lines = map(lambda l: l.strip(), lines)
  lines = map(list, lines)
  lines = list(lines)

  changes = True
  while changes:
    new_lines = copy.deepcopy(lines)
    changes = False

    for i in range(len(lines)):
      for j in range(len(lines[i])):
        if lines[i][j] == '.':
          pass
        elif lines[i][j] == 'L':
          if seated_neighbours(lines, i, j) == 0:
            new_lines[i][j] = '#'
            changes = True
        elif lines[i][j] == '#':
          if seated_neighbours(lines, i, j) >= 4:
            new_lines[i][j] = 'L'
            changes=True
        else:
          assert False, "Unexpected seat character"

    lines = new_lines

    print(seated_count(lines))
    # pprint(list(map(lambda l: ''.join(l), lines)))

  return seated_count(lines)

def seated_neighbours(lines, i, j):
  acc = 0
  for di,dj in {(1,1), (1,0), (1, -1), (0,1), (0,-1), (-1, 1), (-1, 0), (-1, -1)}:
    try:
      if lines[i + di][j + dj] == '#' and i + di >= 0 and j + dj >= 0:
        acc += 1
    except IndexError:
      pass # If we are out of bounds we just don't increase the count of seated neighbours
  return acc

def seated_count(lines):
  return len([item for sublist in lines for item in sublist if item == '#'])
  

if __name__ == "__main__":
  run()