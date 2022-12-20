from sys import stdin

read = stdin.readline


T = int(read())
for _ in range(T):
    case = int(read())
    arr = map(int, read().split())
    K = int(read())
    dp = [0] * (K + 1)
    dp[0] = 1
    for i in arr:
        for j in range(i, K + 1):
            dp[j] = dp[j] + dp[j - i]
    print(dp[K])