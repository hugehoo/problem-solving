import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
n, m = map(int, input().split())
ns = set()

for _ in range(n):
    ns.add(input().rstrip())

count = 0

for _ in range(m):
    ms = input().rstrip()
    if ms in ns:
        count += 1
print(count)