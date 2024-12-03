import re
import sys

memory = re.sub(r"don't\(\).*?(do\(\)|$)", '', sys.stdin.read(), flags=re.DOTALL)
operands = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', memory)
print(sum(int(x) * int(y) for x, y in operands))
