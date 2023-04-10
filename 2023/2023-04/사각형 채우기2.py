N = int(input())

dp = [0, 1, 3] + [0] * 1000

for n in range(3, N + 1):
    dp[n] = (dp[n - 1] + dp[n - 2] * 2) % 10007
print(dp[N])