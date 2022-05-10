import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
for _ in range(n):
    m = int(input())
    dp = [(1, 0), (0, 1), (1, 1), (1, 2)]

    if m <= 3:
        x, y = dp[m]
        print(x, y)
        continue
    for i in range(4, m + 1):
        dp.append([dp[i - 1][0] + dp[i - 2][0], dp[i - 1][1] + dp[i - 2][1]])

    print(dp[m][0], dp[m][1])