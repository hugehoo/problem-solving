N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]

dp[0][0] = board[0][0]
# data set up
for r in range(N):
    for c in range(N):
        if c == 0 and r < N - 1:
            dp[r + 1][c] = board[r + 1][c] + dp[r][c]
        if r == 0 and c < N - 1:
            dp[r][c + 1] = board[r][c + 1] + dp[r][c]

start = [0, 0]

for r in range(1, N):
    for c in range(1, N):
        dp[r][c] = max(dp[r][c - 1], dp[r - 1][c - 1], dp[r - 1][c]) + board[r][c]

print(dp[N - 1][N - 1])
