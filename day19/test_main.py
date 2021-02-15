import day19.main

import pytest


# WARNING: This implementation is incorrect for reasons unknown to me

@pytest.fixture
def rule_set():
    rules = [
        '92: "a"',
        '13: "b"',
        '0: 92 13 | 13 13',
    ]
    return day19.main.RuleSet(rules)


@pytest.fixture
def two_step_rule_set():
    rules = [
        '92: "a"',
        '13: "b"',
        '134: 92 13 | 13 13',
        '119: 92 13',
        '0: 119 13 | 134 92',
    ]
    return day19.main.RuleSet(rules)


def test_literal_rule_parsing():
    rules = ['92: "a"']
    rule_set = day19.main.RuleSet(rules)
    rule_set._parse_rules()
    assert rule_set.computed_rules[92] == 'a'


def test_reference_rule_parsing(rule_set):
    rule_set._parse_rules()
    assert rule_set.reference_rules[0] == [[92, 13], [13, 13]]


def test_compute_rule_0(rule_set):
    assert rule_set.compute_rule_zero_regex() == '((ab)|(bb))'


def test_two_step_compute_rule_0(two_step_rule_set):
    assert two_step_rule_set.compute_rule_zero_regex() == '((((ab))b)|(((ab)|(bb))a))'
