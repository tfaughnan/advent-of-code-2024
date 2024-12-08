from collections.abc import Callable, Iterable
import operator
import sys

def concat(x: int, y: int) -> int:
    return int(str(x) + str(y))

def satisfiable(expect: int, lhs: int, rhs: list[int], ops: Iterable[Callable[[int, int], int]]) -> int:
    if not rhs:
        return lhs == expect
    return any(satisfiable(expect, op(lhs, rhs[0]), rhs[1:], ops) for op in ops)

total = 0
for line in sys.stdin:
    s = line.split(': ')
    expect = int(s[0])
    args = [*map(int, s[1].split())]
    if satisfiable(expect, args[0], args[1:], [operator.add, operator.mul, concat]):
        total += expect

print(total)
