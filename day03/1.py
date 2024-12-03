import re
import sys

operands = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', sys.stdin.read())
print(sum(int(x) * int(y) for x, y in operands))
