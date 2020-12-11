
import more_itertools
import re

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

def check(p: dict) -> bool:
  return bool(
    {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}.issubset(p.keys()) and
    1920 <= int(p['byr']) <= 2002 and
    2010 <= int(p['iyr']) <= 2020 and
    2020 <= int(p['eyr']) <= 2030 and
    height_check(p['hgt']) and
    hair_color_check(p['hcl']) and
    p['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'} and
    re.fullmatch('[0-9]{9}', p['pid'])
  )


def height_check(h):
  height = int(h[:-2])
  unit = h[-2:]

  if unit == 'cm':
    return 150 <= height <= 193
  elif unit == 'in':
    return 59 <= height <=76
  else:
    return False

def hair_color_check(c):
  return re.fullmatch('#[0-9a-f]{6}', c)

if __name__ == "__main__":
  print(run())