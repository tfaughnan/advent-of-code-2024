from collections import defaultdict
import itertools
import sys

def is_correctly_ordered(rules: defaultdict[int, list[int]], update: list[int]) -> bool:
    for x, y in itertools.pairwise(update):
        if x in rules[y]:
            return False
    return True

rules_input, updates_input = sys.stdin.read().split('\n\n')
rules = defaultdict[int, list[int]](list)
for line in rules_input.split('\n'):
    x, y = map(int, line.split('|'))
    rules[x].append(y)

total = 0
for line in updates_input.strip().split('\n'):
    update = [*map(int, line.split(','))]
    if is_correctly_ordered(rules, update):
        total += update[len(update) // 2]

print(total)
