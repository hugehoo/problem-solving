N = int(input())

dp = [0, 0, 1, 1, 1] + [0] * 997
if N <= 4:
    print(1)
else:
    for n in range(5, N + 1):
        dp[n] = (dp[n - 3] + dp[n - 2]) % 10007
    print(dp[N] % 10007)

"""
dp[6] = dp[3] dp[3] / dp[1] dp[5] X / dp[2] dp[4] / dp[4] dp[2]
dp[5] = dp[1] + dp[4] X / dp[2] + dp[3] / dp[3] + dp[2]

dp[2] = 1
dp[3] = 1
dp[4] = 1
dp[5] = dp[4] + dp[3] = 1 + 1 = 2 => dp[3] + dp[2] = 1 + 1
dp[6] = dp[5] + dp[4] = 2 + 1 = 3 => dp[3] + dp[4] = 1 + 1 / 3, 3 / 2, 4/ 2, 2, 2
dp[7] = dp[6] + dp[5] = 5

"""
