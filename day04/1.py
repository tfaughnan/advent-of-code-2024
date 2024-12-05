import sys

DIRECTIONS = (
    (0, 1, 2, 3),                       # up
    (0, -1j, -2j, -3j),                 # down
    (0, -1, -2, -3),                    # left
    (0, 1j, 2j, 3j),                    # right
    (0, -1 - 1j, -2 - 2j, -3 - 3j),     # diagonal down and left
    (0, -1 + 1j, -2 + 2j, -3 + 3j),     # diagonal up and left
    (0, 1 + 1j, 2 + 2j, 3 + 3j),        # diagonal up and right
    (0, 1 - 1j, 2 - 2j, 3 - 3j),        # diagonal down and right
)

grid = {}
for a, line in enumerate(sys.stdin):
    for b, char in enumerate(line.strip()):
        grid[complex(a, b)] = char

total = 0
for coord in grid:
    for direction in DIRECTIONS:
        if ''.join(grid.get(coord + d, '') for d in direction) == 'XMAS':
            total += 1

print(total)
