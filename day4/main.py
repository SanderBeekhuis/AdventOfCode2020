
import more_itertools

def run(file: str='input.txt') -> int:
  lines = open(file, 'r').readlines()
  lines = map(lambda l: l.strip(), lines)

  return process_passports(list(lines))

def process_passports(lines) -> int:
  """Returns the number of valid passports"""
  try:
    i = lines.index('')
    passport = parse(lines[:i])
    return int(check(passport)) + process_passports(lines[i+1:])

  except ValueError:
    passport = parse(lines)
    return int(check(passport))

def parse(lines):
  passport = map(lambda l: l.split(), lines)
  passport = more_itertools.flatten(passport)
  return {k: v for k, v in map(lambda s: s.split(':'), passport) }

def check(passport: dict) -> bool:
  return {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(passport.keys())


if __name__ == "__main__":
  print(run())