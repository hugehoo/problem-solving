import sys
from itertools import combinations

N, target = map(int, input().split())
coins = []
dp = [float('inf')] * (target + 1)

dp[0] = 0
for _ in range(N):
    coins.append(int(input()))

for n in range(N):
    for c in range(coins[n], target + 1):
        dp[c] = min(dp[c], dp[c - coins[n]] + 1)
if dp[target] == float('inf'):
    print(-1)
else:
    print(dp[target])

"""
3 15
1
5
12
"""
