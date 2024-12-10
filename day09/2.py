from collections import Counter
import itertools
import sys

def index_disk(disk: list[int]) -> tuple[dict[int, int], dict[int, int]]:
    free_blocks = {}
    free_len = 0
    file_ids = {}
    for i in range(len(disk)):
        if disk[i] < 0:
            free_len += 1
            continue
        if free_len > 0:
            free_blocks[i - free_len] = free_len
        free_len = 0
        if disk[i] not in file_ids:
            file_ids[disk[i]] = i
    return free_blocks, file_ids

def find_free_blocks(free_blocks: dict[int, int], file_idx: int, file_len: int) -> tuple[int, int]:
    for free_idx, free_len in sorted(free_blocks.items()):
        if free_idx < file_idx and free_len >= file_len:
            return free_idx, free_len
    return -1, 0

flatten = itertools.chain.from_iterable
disk = list(flatten([i // 2] * int(char) if not i % 2 else [-1] * int(char)
                    for i, char in enumerate(sys.stdin.read().strip())))
free_blocks, file_ids = index_disk(disk)
file_lens = Counter(block for block in disk if block > 0)
for file_id, file_idx in sorted(file_ids.items(), reverse=True):
    file_len = file_lens[file_id]
    free_idx, free_len = find_free_blocks(free_blocks, file_idx, file_len)
    if free_idx < 0:
        continue
    for i in range(file_len):
        disk[free_idx + i] = file_id
        disk[file_idx + i] = -1
    del free_blocks[free_idx]
    if free_len > file_len:
        free_blocks[free_idx + file_len] = free_len - file_len

print(sum(i * int(char) for i, char in enumerate(disk) if char >= 0))
