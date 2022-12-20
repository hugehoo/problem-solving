from collections import deque
import sys

input = sys.stdin.readline

dp = [0, 1, 2, 4]
for r in range(4, 1000001):
    dp.append((dp[r - 1] + dp[r - 2] + dp[r - 3]) % 1000000009)

N = int(input())
for _ in range(N):
    a = int(input())
    print(dp[a])


