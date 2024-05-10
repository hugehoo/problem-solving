import sys

input = sys.stdin.readline

N, M = map(int, input().split())
dp = [[0] * (M + 1)] * (N + 1)
candy = [list(map(int, input().split())) for _ in range(N)]

for n in range(1, N + 1):
    for m in range(1, M + 1):
        dp[n][m] = max(dp[n - 1][m], dp[n][m - 1], dp[n - 1][m - 1]) + candy[n - 1][m - 1]
print(dp[N][M])


"""
https://www.acmicpc.net/problem/11048
3 4
1 2 3 4
0 0 0 5
9 8 7 6
"""
