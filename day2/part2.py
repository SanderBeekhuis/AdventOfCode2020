from collections import Counter

def is_valid(line):
  line = line.strip()
  policy, password = line.split(': ')
  count, letter = policy.split(' ')
  positions = map(int, count.split('-'))

  letters = [password[p-1] for p in positions]

  # Count password characters
  c = Counter(letters)

  return c[letter] == 1

lines = open('input.txt', 'r').readlines()
valid_password_count = 0

for line in lines:
  if is_valid(line):
    valid_password_count += 1

print(valid_password_count)
