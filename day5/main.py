import functools

def run(file: str='input.txt'):
  lines = open(file, 'r').readlines()
  lines = map(lambda l: l.strip(), lines)

  seat_ids = list(map(seat_id, lines))
  max_seat = max(seat_ids)
  print("Max seat:" , max_seat)

  missing_seats = list(filter(lambda s: (s-1 in seat_ids) and (s+1 in seat_ids) and (s not in seat_ids) , range(0, max_seat)))
  assert len(missing_seats) == 1
  print("Missing seat", missing_seats.pop())
  return ""

def seat_id(s):
    return 8* row(s[:7]) + collumn(s[7:])

def row(s):
    return functools.reduce(lambda acc, c: (1 if c=='B' else 0) + acc*2, s, 0)

def collumn(s):
    return functools.reduce(lambda acc, c: (1 if c=='R' else 0) + acc*2, s, 0)


if __name__ == "__main__":
  print(run())