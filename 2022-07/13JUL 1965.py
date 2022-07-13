import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))

dp = [0] * 1001
for i in arr:
    dp[i] = 1
    dp[i] += max(dp[:i])
print(max(dp))
