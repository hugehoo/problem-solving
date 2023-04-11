N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

dp[0][N - 1] = board[0][N - 1]

# data set up
for c in range(N - 1, 0, -1):
    dp[0][c - 1] = board[0][c - 1] + dp[0][c]
for r in range(N - 1):
    dp[r + 1][N - 1] = board[r + 1][N - 1] + dp[r][N - 1]

# tabulation
for r in range(1, N):
    for c in range(N - 2, -1, -1):
        dp[r][c] = min(dp[r][c + 1], dp[r - 1][c]) + board[r][c]

print(dp[N - 1][0])
