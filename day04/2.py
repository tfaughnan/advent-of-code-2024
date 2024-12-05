import sys

DIRECTIONS = (
    (-1 + 1j, 0, 1 - 1j),   # diagonal upper left to lower right
    (-1 - 1j, 0, 1 + 1j),   # diagonal lower left to upper right
)

grid = {}
for a, line in enumerate(sys.stdin):
    for b, char in enumerate(line.strip()):
        grid[complex(a, b)] = char

total = 0
for coord in grid:
    diag1 = ''.join(grid.get(coord + d, '') for d in DIRECTIONS[0])
    diag2 = ''.join(grid.get(coord + d, '') for d in DIRECTIONS[1])
    if diag1 in ('MAS', 'SAM') and diag2 in ('MAS', 'SAM'):
        total += 1

print(total)
