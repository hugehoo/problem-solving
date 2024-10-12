from sys import stdin
from collections import defaultdict

input = stdin.readline

if __name__ == '__main__':
    N = int(input())
    profit, time = [0], [0]
    dp = [0] * (N + 1)
    for _ in range(N):
        t, p = map(int, input().split())
        time.append(t)
        profit.append(p)

    for i in range(1, N + 1):
        dp[i] = max(dp[i], dp[i - 1])
        man_date = i + time[i] - 1
        if man_date <= N:
            dp[man_date] = max(dp[i - 1] + profit[i], dp[man_date])

    print(max(dp))
