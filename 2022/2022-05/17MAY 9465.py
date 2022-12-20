import sys

input = sys.stdin.readline

N = int(input().strip())
for _ in range(N):
    m = int(input())
    board = []
    for _ in range(2):
        board.append(list(map(int, input().split())))
    dp = [[0] * m for _ in range(2)]
    dp[0][0] = board[0][0]
    dp[1][0] = board[1][0]
    if m > 1:
        dp[0][1] = board[0][1] + dp[1][0]
        dp[1][1] = board[1][1] + dp[0][0]

        for i in range(2, m):
            dp[0][i] = board[0][i] + max(max(dp[1][i - 1], dp[0][i - 2]), dp[1][i - 2])
            dp[1][i] = board[1][i] + max(max(dp[0][i - 1], dp[1][i - 2]), dp[0][i - 2])
    max_val = max(max(dp[0]), max(dp[1]))
    print(max_val)

"""
2
5
50 10 100 20 40
30 50 70 10 60
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
"""
