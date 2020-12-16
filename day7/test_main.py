import pytest

import day7.main

@pytest.mark.parametrize('line,expected',
  [
    ('light red bags contain 1 bright white bag, 2 muted yellow bags.', ('light red bag', {'bright white bag': 1, 'muted yellow bag': 2})),
    ('bright white bags contain 1 shiny gold bag.', ('bright white bag', {'shiny gold bag': 1})),
    ('dotted black bags contain no other bags.', ('dotted black bag', {})),
  ]
)
def test_parse_line(line, expected):
  assert expected == day7.main.parse_line(line)

def test_run():
  bag_contents = day7.main.run('day7/test_input.txt')
  assert 4 == day7.main.bags_possibly_containing_gold_bag(bag_contents)
  assert 32 == day7.main.bags_inside_gold_bag(bag_contents)