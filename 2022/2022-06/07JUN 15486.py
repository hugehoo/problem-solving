import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

N = int(input())
M = 0
p, t = [], []
dp = [0] * (N + 1)

for _ in range(N):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)
for i in range(N):
    M = max(M, dp[i])  # 왜 M 과 dp[i] 를 여기서 비교할까?
    add_date = i + t[i]
    if add_date > N:
        continue
    dp[add_date] = max(M + p[i], dp[add_date])
print(dp)