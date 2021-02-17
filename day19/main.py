import re
from typing import Union

import lib

### This still fails

def run(file: str = 'input.txt'):
    lines = open(file, 'r').readlines()
    lines = [line.strip() for line in lines]
    rules, messages = lib.split_on_empty(lines)

    rule_set = RuleSet(rules)
    regex = rule_set.compute_rule_zero_regex()

    print(regex)

    compiled_regex = re.compile(regex)

    matches = [m for m in messages if compiled_regex.match(m)]
    # Answer is too high
    print(f'Part 1: {len(matches)}')


class RuleSet:
    def __init__(self, rules):
        self.rules = rules
        self.computed_rules = {}
        self.reference_rules = {}

    def compute_rule_zero_regex(self):
        self._parse_rules()
        self._resolve_rules()
        computed_rule = self.computed_rules[0]
        return f'^{self._rule_to_regex(computed_rule)}$'

    def _parse_rules(self):
        for rule in self.rules:
            key, rule = rule.split(': ')
            key = int(key)
            if rule[0] == '"':
                self.computed_rules[key] = rule[1]
            else:
                self.reference_rules[key] = [[int(o) for o in option.split(' ')] for option in rule.split(' | ')]

    def _resolve_rules(self):
        while self.reference_rules:
            for key, rule in list(self.reference_rules.items()):
                try:
                    computed_rule = [tuple(self.computed_rules[o] for o in option) for option in rule]

                    del self.reference_rules[key]
                    self.computed_rules[key] = computed_rule
                except KeyError:
                    pass  # All rules needed to compute this rule have not been computed

    def _rule_to_regex(self, rule: Union[list, str]):
        if type(rule) == str:
            return rule  # Reached bottom of the recursion

        # Turn options into regexes
        options = [''.join(map(self._rule_to_regex, option)) for option in rule]

        # Combine options into one regex
        return '((' + ')|('.join(options) + '))'


if __name__ == "__main__":
    run()
