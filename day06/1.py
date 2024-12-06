import sys

def move_guard(lab: dict[complex, str], pos: complex, heading: complex) -> tuple[complex, complex]:
    if lab[pos + heading] == '#':
        heading *= -1j
    else:
        pos += heading
        lab[pos] = 'X'
    return pos, heading

lab = {}
for b, line in enumerate(sys.stdin):
    for a, char in enumerate(line.strip()):
        if char == '^':
            startpos = complex(a, -b)
            char = 'X'
        lab[complex(a, -b)] = char

pos = startpos
heading = 1j
while pos + heading in lab:
    pos, heading = move_guard(lab, pos, heading)

print(sum(char == 'X' for char in lab.values()))
