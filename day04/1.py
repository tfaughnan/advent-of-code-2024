import sys

DIRECTIONS = (
    ((0, -3), (0, -2), (0, -1), (0, 0)),      # left
    ((-3, -3), (-2, -2), (-1, -1), (0, 0)),   # diag upper left
    ((-3, 0), (-2, 0), (-1, 0), (0, 0)),      # above
    ((-3, 3), (-2, 2), (-1, 1), (0, 0)),      # diag upper right
    ((0, 3), (0, 2), (0, 1), (0, 0)),         # right
    ((3, 3), (2, 2), (1, 1), (0, 0)),         # diag lower right
    ((3, 0), (2, 0), (1, 0), (0, 0)),         # below
    ((3, -3), (2, -2), (1, -1), (0, 0)),      # diag lower left
)

grid = {}
for r, line in enumerate(sys.stdin):
    for c, char in enumerate(line.strip()):
        grid[(r, c)] = char

total = 0
for r, c in grid:
    for d in DIRECTIONS:
        word = ''.join(grid.get((d[i][0] + r, d[i][1] + c), '')
                       for i in range(len(d)))
        if word == 'XMAS':
            total += 1

print(total)
