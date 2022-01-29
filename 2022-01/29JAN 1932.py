n = int(input())

board = [list(map(int, input().split())) for i in range(n)]
for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            board[i][0] += board[i - 1][0]
        elif i == j:
            board[i][j] += board[i - 1][j - 1]
        else:
            board[i][j] += max(board[i - 1][j], board[i - 1][j - 1])

print(max(board[-1]))
