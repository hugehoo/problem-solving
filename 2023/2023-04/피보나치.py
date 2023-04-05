N = int(input())

dp = [0, 1, 1] + [0] * 43
if N <= 2:
    print(1)
else:
    for n in range(3, N + 1):
        dp[n] = dp[n - 1] + dp[n - 2]
    print(dp[N])
