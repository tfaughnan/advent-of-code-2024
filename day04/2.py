import sys

grid = {}
for r, line in enumerate(sys.stdin):
    for c, char in enumerate(line.strip()):
        grid[(r, c)] = char

total = 0
for r, c in grid:
    diag1 = ''.join((grid.get((r - 1, c - 1), ''),
                     grid.get((r, c), ''),
                     grid.get((r + 1, c + 1), '')))
    diag2 = ''.join((grid.get((r + 1, c - 1), ''),
                     grid.get((r, c), ''),
                     grid.get((r - 1, c + 1), '')))
    if diag1 in ('MAS', 'SAM') and diag2 in ('MAS', 'SAM'):
        total += 1

print(total)
