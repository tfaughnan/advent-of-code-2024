import itertools
import sys

flatten = itertools.chain.from_iterable
disk = list(flatten([i // 2] * int(char) if not i % 2 else [-1] * int(char)
                    for i, char in enumerate(sys.stdin.read().strip())))
left = 0
right = len(disk) - 1
while left < right:
    if disk[left] < 0 and disk[right] >= 0:
        disk[left] = disk[right]
        disk[right] = -1
    left += disk[left] >= 0
    right -= disk[right] < 0

print(sum(i * int(char) for i, char in enumerate(disk) if char >= 0))
