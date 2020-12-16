import collections

def run(file: str='day7/input.txt'):
  lines = open(file, 'r').readlines()
  lines = map(lambda l: l.strip(), lines)

  return {bag: content for bag, content in map(parse_line, lines)}

def parse_line(line):
  bag, raw_contents = line.split('s contain ')
  if raw_contents == 'no other bags.':
    return bag, {}
  raw_contents = raw_contents.split(', ')
  contents = {c[2:].rstrip('s.'): int(c[0]) for c in raw_contents}
  return (bag, contents)

def bags_possibly_containing_gold_bag(bag_contents):
  bags_possibly_containing_gold_bag = {'shiny gold bag'}
  size = 0

  # Loop while we still find more bags possibly containing the shiny gold bag
  while size < len(bags_possibly_containing_gold_bag):
    size = len(bags_possibly_containing_gold_bag)

    # Add bags that contain (bags that) can contain the shiny gold bag
    for bag, contents in bag_contents.items():
      if set(contents.keys()).intersection(bags_possibly_containing_gold_bag):
        bags_possibly_containing_gold_bag.add(bag)

  # Subtract one for the shiny gold bag itself
  return len(bags_possibly_containing_gold_bag) - 1

def bags_inside_gold_bag(bag_contents):
  count = 0
  current_bags = {'shiny gold bag': 1}

  while current_bags:
    new_bags = collections.Counter()
    for bag, occurrence in current_bags.items():
        for inner_bag, included in bag_contents[bag].items():
          new_bags[inner_bag] += occurrence * included

    count+=sum(new_bags.values())
    current_bags = new_bags
    print(count)

  return count

if __name__ == "__main__":
  bag_contents=run()
  print("Number of possible outermost bags: ", bags_possibly_containing_gold_bag(bag_contents))
  print("Number of bags inside a gold bag: ", bags_inside_gold_bag(bag_contents))