from collections import defaultdict
from collections.abc import Callable
import functools
import itertools
import sys

def is_correctly_ordered(rules: defaultdict[int, list[int]], update: list[int]) -> bool:
    for x, y in itertools.pairwise(update):
        if x in rules[y]:
            return False
    return True

def cmp_with_rules(rules: defaultdict[int, list[int]]) -> Callable[[int, int], int]:
    return lambda x, y: 1 if x in rules[y] else (-1 if y in rules[x] else 0)

rules_input, updates_input = sys.stdin.read().split('\n\n')
rules = defaultdict[int, list[int]](list)
for line in rules_input.split('\n'):
    x, y = map(int, line.split('|'))
    rules[x].append(y)

total = 0
for line in updates_input.strip().split('\n'):
    update = [*map(int, line.split(','))]
    if not is_correctly_ordered(rules, update):
        fixed = sorted(update, key=functools.cmp_to_key(cmp_with_rules(rules)))
        total += fixed[len(fixed) // 2]

print(total)
