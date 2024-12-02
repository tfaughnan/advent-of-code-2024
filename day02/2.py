import sys


def is_safe(report: list[int], tolerate: int = 1) -> bool:
    diffs = [a - b for a, b in zip(report, report[1:])]
    if is_strictly_monotone(diffs) and is_gradual(diffs):
        return True
    if tolerate > 0:
        for i in range(len(report)):
            subreport = report[:i] + report[i + 1:]
            if is_safe(subreport, tolerate=tolerate - 1):
                return True
    return False


def is_strictly_monotone(diffs: list[int]) -> bool:
    return abs(sum(abs(d) // d if d else 0 for d in diffs)) == len(diffs)


def is_gradual(diffs: list[int]) -> bool:
    return all(1 <= abs(d) <= 3 for d in diffs)


safe = sum(is_safe([*map(int, line.split())]) for line in sys.stdin)
print(safe)
