import sys
from math import inf


input = sys.stdin.readline

N, M = map(int, input().split())
min1 = inf
min6 = inf

for _ in range(M):
    six, one = map(int, input().split())
    min1 = min(min1, one)
    min6 = min(min6, six)

b, r = divmod(N, 6)
if min6 > min1 * 6:  # 1
    print(N * min1)
elif min6 < min1:  # 2
    print(b * min6 + (min6 if r else 0))
else: # 3
    print(b * min6 + (min(r * min1, min6) if r else 0))

