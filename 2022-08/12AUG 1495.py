import sys

input = sys.stdin.readline
N, S, M = map(int, input().split())
V = list(map(int, input().split()))
dp = [[0] * (M + 1) for _ in range(N + 1)]
dp[0][S] = 1

for n in range(N):
    for m in range(M + 1):
        if dp[n][m]:
            if m + V[n] <= M:
                dp[n + 1][m + V[n]] = 1
            if m - V[n] >= 0:
                dp[n + 1][m - V[n]] = 1
for i in range(len(dp[N]) - 1, -1, -1):
    if dp[N][i]:
        print(i)
        exit()
print(-1)

"""
3 5 10
5 3 7
"""
