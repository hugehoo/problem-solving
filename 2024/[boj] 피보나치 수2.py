import sys

input = sys.stdin.readline

N = int(input())
dp = [0] * (N + 2)
dp[1] = 1
dp[2] = 1
# if N <= 2:
#     print(dp[N])
# else:
# dp3 =
dp1 = 1
dp2 = 1
dp3 = 0
for i in range(2, N):
    dp3 = dp2 + dp1
    # dp[i] = dp[i - 1] + dp[i - 2]
    dp2 = dp3
    dp1 = dp2
# print(dp[N])
print(dp3)
