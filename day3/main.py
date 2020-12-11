lines = open('input.txt', 'r').readlines()

trees=0

for i, line in enumerate(lines):
  line = line.strip()

  # Final version modification
  if i % 2 == 1:
    continue

  index = (i // 2) % 31

  if line[index] == '#':
    trees += 1

  print(i, index, line[index], trees)


print(trees)

# Slope 1 67
# Slope 3 299
# Slope 5 67
# Slope 7 71
# Slope 0.5 38
# Ans 3621285278
