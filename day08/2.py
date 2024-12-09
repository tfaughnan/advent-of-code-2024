from collections import defaultdict
import itertools
import sys

def antinodes_in_bounds(w: int, h: int, z1: complex, z2: complex) -> list[complex]:
    # place bounds on t for the parametrized line f(t) = (z2 - z1) * t + z1
    top = -z1.imag / (z2 - z1).imag
    bottom = (-(h - 1) - z1.imag) / (z2 - z1).imag
    left = -z1.real / (z2 - z1).real
    right = ((w - 1) - z1.real) / (z2 - z1).real
    t1, t2 = map(int, sorted((top, bottom, left, right))[1:3])

    # compute f(t) at integer values of t in [t1, t2]
    return [(z2 - z1) * t + z1 for t in range(t1, t2 + 1)]

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
