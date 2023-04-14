def catalan(m):
    dp_size = m + 1
    dp = [0] * dp_size
    dp[0] = 1
    for size in range(1, dp_size):
        for s in range(size):
            dp[size] += dp[s] * dp[size - s - 1]
    return dp[m]


n = int(input())
print(catalan(n))
