import sys
from copy import deepcopy

n = int(sys.stdin.readline())
cards = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for k in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - k] + cards[k])
print(dp[-1])

"""
dp = [] 각 장을 살때 지불할 수 있는 최대 금액을 저장.
2장을 만드려면 1 + 1, 2
3장을 만드려면, 1 + 1 + 1, 1 + 2, 3
4장을 만드려면, 1 + 1 + 1 + 1, 1 + 3, 2 + 2, 4 
"""
