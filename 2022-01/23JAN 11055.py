# from sys import stdin
#
# read = stdin.readline
#
# N = int(read())
# arr = list(map(int, read().split()))
#
# dp = [0] * N
# dp[0] = arr[0]
# for i in range(1, N):
#     dp[i] = arr[i]
#     for j in range(i):
#         if arr[j] < arr[i]:
#             print(dp)
#             dp[i] = max(dp[i], dp[j] + arr[i])
#
#     # if arr[i - 1] < arr[i]:
#     #     dp[i] = dp[i - 1] + arr[i]
#     # else:
#     #     for jdx, j in enumerate(arr[:i][::-1]):
#     #         if arr[i] > j:
#     #             idx = len(arr[:i]) - jdx - 1
#                 # dp[i] = arr[i] + dp[idx]
#                 # break
# print(max(dp))
#
"""
10
1 100 2 50 60 3 5 6 7 8

4
1 10 18 9
"""

import sys

input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

max_num = 0
data = list(map(int, input().split()))

for i in data:
    dp[i] = i
    dp[i] += max(dp[:i])
print(max(dp))