import functools
import lib

from pprint import pprint

def run(file: str='day6/input.txt'):
  lines = open(file, 'r').readlines()
  lines = map(lambda l: l.strip(), lines)

  groups = lib.split_on_empty(lines)
  groups = list(map(lambda g: list(map(set, g)), groups))

  union_groups = map(lambda g: set().union(*g), groups)

  print("Sum of counts:", sum(map(len, union_groups)))

  intersection_groups = map(lambda g: g[0].intersection(*g), groups)

  print("Sum of intersections:", sum(map(len, intersection_groups)))

if __name__ == "__main__":
  run()