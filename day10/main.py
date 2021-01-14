import functools
import itertools
import collections

def run(file: str='day10/input.txt'):
  lines = open(file, 'r').readlines()
  lines = map(lambda l: l.strip(), lines)
  lines = list(map(int, lines))

  adapter_stack = sorted(lines + [0, max(lines)+3] )

  differences = collections.Counter()

  for i, j in pairwise(adapter_stack): 
    differences[j-i] += 1

  print("Part 1:", differences[1]*differences[3])
  print("Part 2:", part_2(adapter_stack))

def part_2(adapter_stack):
  segmented_stack = []
  segment=[]
  for i, j in pairwise(adapter_stack): 
    segment.append(i)

    if j-i == 1:
      pass
    elif j-i == 3:
      segmented_stack.append(segment)
      segment = []
    else:
      assert False, f"Unexpected difference {i}, {j}"

  segmented_stack.append(segment)
  segment_sizes = collections.Counter(map(len, segmented_stack))
  ## Assumes the largest segment size is 5
  return 2 ** segment_sizes[3] * 4 ** segment_sizes[4] * 7 ** segment_sizes[5]

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

if __name__ == "__main__":
  run()