import sys

input = sys.stdin.readline

N, M = map(int, input().split())
board = [[float('inf')] * N for _ in range(N)]
for i in range(N):
    board[i][i] = 0

for _ in range(M):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1
    board[b - 1][a - 1] = 1

for k in range(N):
    for r in range(N):
        for c in range(N):
            board[r][c] = min(board[r][c], board[r][k] + board[k][c])
answer_array = []
for idx, bo in enumerate(board):
    answer_array.append(sum(bo))
print(answer_array.index(min(answer_array)) + 1)
