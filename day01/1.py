import sys

ids = [*map(int, sys.stdin.read().split())]
lefts = ids[::2]
rights = ids[1::2]
dist = sum(abs(left - right) for left, right in zip(sorted(lefts), sorted(rights)))
print(dist)
