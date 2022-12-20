import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
dp = [[0] * n for _ in range(n)]
dp[0][0] = 1
for r in range(n):
    for c in range(n):
        if r == n - 1 and c == n - 1:
            print(dp[n - 1][n - 1])

            break
        down = r + board[r][c]
        right = c + board[r][c]

        if down < n:
            dp[down][c] += dp[r][c]
        if right < n:
            dp[r][right] += dp[r][c]
