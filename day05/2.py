from collections import defaultdict
import functools
import itertools
import sys

def is_correctly_ordered(rules: defaultdict[int, list[int]], update: list[int]) -> bool:
    for x, y in itertools.pairwise(update):
        if x in rules[y]:
            return False
    return True

# XXX: relies on rules being global (cmp_to_key functions take exactly 2 args)
def cmp(x: int, y: int) -> int:
    if x in rules[y]:
        return 1
    elif y in rules[x]:
        return -1
    return 0

rules_input, updates_input = sys.stdin.read().split('\n\n')
rules = defaultdict[int, list[int]](list)
for line in rules_input.split('\n'):
    x, y = map(int, line.split('|'))
    rules[x].append(y)

total = 0
for line in updates_input.strip().split('\n'):
    update = [*map(int, line.split(','))]
    if not is_correctly_ordered(rules, update):
        fixed = sorted(update, key=functools.cmp_to_key(cmp))
        total += fixed[len(fixed) // 2]

print(total)
