import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

case = []
dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, N + 1):
        dp[i][j] = board[i - 1][j - 1] + (dp[i][j - 1] + dp[i - 1][j] - dp[i - 1][j - 1])
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(dp[x2][y2] - (dp[x2][y1 - 1] + dp[x1 - 1][y2] - dp[x1 - 1][y1 - 1]))

"""
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
"""
