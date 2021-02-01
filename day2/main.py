from collections import Counter

def is_valid(line):
  line = line.strip()
  policy, password = line.split(': ')
  count, letter = policy.split(' ')
  min_count, max_count = map(int, count.split('-'))

  # Count password characters
  c = Counter(password)

  return c[letter] in range(min_count, max_count+1)


lines = open('day2/input.txt', 'r').readlines()
valid_password_count = 0

for line in lines:
  if is_valid(line):
    valid_password_count += 1

print(valid_password_count)
