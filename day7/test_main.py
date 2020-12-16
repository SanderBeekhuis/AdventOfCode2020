import pytest

import day7.main

@pytest.mark.parametrize('line,expected',
  [
    ('light red bags contain 1 bright white bag, 2 muted yellow bags.', ('light red bag', {'bright white bag', 'muted yellow bag'})),
    ('bright white bags contain 1 shiny gold bag.', ('bright white bag', {'shiny gold bag'})),
    ('dotted black bags contain no other bags.', ('dotted black bag', set())),
  ]
)
def test_parse_line(line, expected):
  assert expected == day7.main.parse_line(line)


def test_run():
  assert 4 == day7.main.run('day7/test_input.txt')