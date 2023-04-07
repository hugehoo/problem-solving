N = int(input())

dp = [0, 1, 2, 3] + [0] * 1000

if N <= 3:
    print(N)
else:
    for n in range(4, N + 1):
        dp[n] = (dp[n - 1] + dp[n - 2]) % 10007
    print(dp[N])