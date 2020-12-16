def run(file: str='day7/input.txt'):
  lines = open(file, 'r').readlines()
  lines = map(lambda l: l.strip(), lines)

  bag_contents = {bag: content for bag, content in map(parse_line, lines)}

  bags_possibly_containing_gold_bag = {'shiny gold bag'}
  size = 0

  # Loop while we still find more bags possibly containing the shiny gold bag
  while size < len(bags_possibly_containing_gold_bag):
    size = len(bags_possibly_containing_gold_bag)

    # Add bags that contain (bags that) can contain the shiny gold bag
    for bag, contents in bag_contents.items():
      if contents.intersection(bags_possibly_containing_gold_bag):
        bags_possibly_containing_gold_bag.add(bag)

  # Subtract one for the shiny gold bag itself
  return len(bags_possibly_containing_gold_bag) - 1

def parse_line(line):
  bag, raw_contents = line.split('s contain ')
  if raw_contents == 'no other bags.':
    return bag, set()
  raw_contents = raw_contents.split(', ')
  contents = {c[2:].rstrip('s.') for c in raw_contents}
  return (bag, contents)

if __name__ == "__main__":
  print("Number of possible outermost bags: ", run())