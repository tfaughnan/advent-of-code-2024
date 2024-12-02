import sys

ids = [*map(int, sys.stdin.read().split())]
lefts = ids[::2]
rights = ids[1::2]
similarity = sum(left * rights.count(left) for left in lefts)
print(similarity)
