import sys

input = sys.stdin.readline
N = int(input())
dp = [0] * (N + 1)
for n in range(2, N + 1):
    if n % 2 == 0:
        dp[n] = min(dp[n // 2], dp[n-1]) + 1
    elif n % 3 == 0:
        dp[n] = min(dp[n // 3], dp[n-1]) + 1
    else:
        dp[n] = dp[n-1] + 1
print(dp)
print(dp[N])

"""
ar [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 16, 17, 18, 19, 20, 21, 22, 23...]
dp [0, 0, 1, 1, 2, 3, 2, 3, 3, 2,  3,  4,  3,  4,  4,  4, 4,  5,  3,  4,  4,  5,  5, 6...]

15 -> 5 -> 4 -> 2 -> 1
30 -> 10 : 3 + 1
"""
