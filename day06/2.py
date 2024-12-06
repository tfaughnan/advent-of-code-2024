from collections.abc import Iterator
import sys

def move_guard(lab: dict[complex, str], pos: complex, heading: complex) -> tuple[complex, complex]:
    if lab[pos + heading] == '#':
        heading *= -1j
    else:
        pos += heading
        lab[pos] = 'X'
    return pos, heading

def obstruction_candidates(_lab: dict[complex, str], pos: complex, heading: complex) -> Iterator[complex]:
    lab = _lab.copy()
    while pos + heading in lab:
        oldchar = lab[pos + heading]
        pos, heading = move_guard(lab, pos, heading)
        if oldchar == '.':
            yield pos

def would_loop(_lab: dict[complex, str], pos: complex, heading: complex, obstruction: complex) -> bool:
    lab = _lab.copy()
    lab[obstruction] = '#'
    history = set()
    while pos + heading in lab:
        if (pos, heading) in history:
            return True
        history.add((pos, heading))
        pos, heading = move_guard(lab, pos, heading)
    return False

lab = {}
for b, line in enumerate(sys.stdin):
    for a, char in enumerate(line.strip()):
        if char == '^':
            startpos = complex(a, -b)
            char = 'X'
        lab[complex(a, -b)] = char

print(sum(would_loop(lab, startpos, 1j, candidate)
          for candidate in obstruction_candidates(lab, startpos, 1j)))
