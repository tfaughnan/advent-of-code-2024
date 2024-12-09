from collections import defaultdict
import itertools
import sys

def antinodes_in_bounds(w: int, h: int, z1: complex, z2: complex) -> list[complex]:
    a1 = 2 * z1 - z2
    a2 = 2 * z2 - z1
    return [a for a in (a1, a2) if 0 <= a.real < w and 0 >= a.imag > -h]

w, h = 0, 0
freqs = defaultdict[str, list[complex]](list)
for b, line in enumerate(sys.stdin):
    w = len(line.strip())
    h += 1
    for a, char in enumerate(line.strip()):
        if char != '.':
            freqs[char].append(complex(a, -b))

antinodes = set()
for antennae in freqs.values():
    for z1, z2 in itertools.combinations(antennae, 2):
        antinodes.update(antinodes_in_bounds(w, h, z1, z2))

print(len(antinodes))
