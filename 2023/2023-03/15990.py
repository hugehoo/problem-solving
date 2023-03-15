N = list(int(input()) for _ in range(int(input())))
MOD = 1_000_000_009

dp = list([0, 0, 0] for _ in range(max(N) + 1))
dp[1] = [1, 0, 0]  # 1
dp[2] = [0, 1, 0]  # 2
dp[3] = [1, 1, 1]  # 1 2, 2 1, 3
for i in range(4, max(N) + 1):
    dp[i][0] = dp[i - 1][1] % MOD + dp[i - 1][2] % MOD
    dp[i][1] = dp[i - 2][0] % MOD + dp[i - 2][2] % MOD
    dp[i][2] = dp[i - 3][1] % MOD + dp[i - 3][0] % MOD
for n in N:
    print(sum(dp[n]) % MOD)
