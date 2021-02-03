from day18.main import compute, matching_bracket_index, compute_advanced

import pytest


@pytest.mark.parametrize('line,expected', [
    ('5 * 5', 25),  # Multiplication
    ('5 + 5', 10),  # Addition
    ('5 + 5 * 5', 50),  # Operation order
    ('5 * 5 + 5', 30),  # Operation order II
    ('5 + (5 * 5)', 30),  # Parenthesis
    ('5 + (5 * 5) + 5', 35),  # Parenthesis in middle
    ('5 * ((5 * 5) + 5)', 150)  # Nested parenthesis

])
def test_compute(line, expected):
    assert compute(line) == expected


@pytest.mark.parametrize('line,expected', [
    ('5 * 5', 25),  # Multiplication
    ('5 + 5', 10),  # Addition
    ('5 + 5 * 5', 50),  # Operation order
    ('5 * 5 + 5', 50),  # Operation order II
    ('5 + (5 * 5)', 30),  # Parenthesis
    ('5 + (5 * 5) + 5', 35),  # Parenthesis in middle
    ('5 * ((5 * 5) + 5)', 150),  # Nested parenthesis
    ('5 * 5 + (5 * 5)', 150),  # Mult in  parenthesis
    ('5 * 5 * 5 * 5', 625),  # Repeated multiplication

    ## Advent Of Code test cases
    ('1 + (2 * 3) + (4 * (5 + 6))', 51),
    ('2 * 3 + (4 * 5)', 46),
    ('5 + (8 * 3 + 9 + 3 * 4 * 3)', 1445),
    ('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', 669_060),
    ('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', 23_340),
    ('(2 + 4 * 9) * (6 + 9 * 8 + 6) + 6', 11_664),
    ('6 + 9 * 8 + 6', 210),
    ('2 + 4 * 9', 54),
    ('54 * 210 + 6', 11_664),
    ('54 * (200 + 10) + 6', 11_664),

])
def test_compute_advanced(line, expected):
    assert compute_advanced(line) == expected

def test_matching_bracket_index():
    assert matching_bracket_index('(())') == 3
    assert matching_bracket_index('a()') == 2
