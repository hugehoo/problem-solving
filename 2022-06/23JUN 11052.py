import sys
from copy import deepcopy

n = int(sys.stdin.readline())
cards = list(map(int, input().split()))
dp = [0] + deepcopy(cards)
for i in range(1, len(cards) + 1):
    if i % 2 == 0:
        dp[i] = max(dp[i], dp[1] * i, dp[1] + dp[i - 1], dp[i // 2] * 2)
        continue
    dp[i] = max(dp[i], dp[1] * i, dp[1] + dp[i - 1])
print(dp[-1])

"""
dp = [] 각 장을 살때 지불할 수 있는 최대 금액을 저장.
2장을 만드려면 1 + 1, 2
3장을 만드려면, 1 + 1 + 1, 1 + 2, 3
4장을 만드려면, 1 + 1 + 1 + 1, 1 + 3, 2 + 2, 4 
"""
