import sys

input = sys.stdin.readline

M = int(input())
board = []
max_board = []
min_board = []
for m in range(M):
    _list = list(map(int, input().split()))
    board.append(_list)
    if m == 0:
        max_board.append(_list)
        min_board.append(_list)
        continue
    max_board.append([0, 0, 0])
    min_board.append([0, 0, 0])

for r in range(1, M):
    for c in range(3):
        if c == 0:
            max_board[r][c] = max(max_board[r - 1][c], max_board[r - 1][c + 1]) + board[r][c]
            min_board[r][c] = min(min_board[r - 1][c], min_board[r - 1][c + 1]) + board[r][c]

        elif c == 1:
            max_board[r][c] = max(max_board[r - 1][c - 1], max_board[r - 1][c], max_board[r - 1][c + 1]) + board[r][c]
            min_board[r][c] = min(min_board[r - 1][c - 1], min_board[r - 1][c], min_board[r - 1][c + 1]) + board[r][c]
        else:
            max_board[r][c] = max(max_board[r - 1][c], max_board[r - 1][c - 1]) + board[r][c]
            min_board[r][c] = min(min_board[r - 1][c], min_board[r - 1][c - 1]) + board[r][c]
# for m in max_board:
#     print(m)
# print(' ')
# for m in min_board:
#     print(m)

print(max(max_board[M - 1]), min(min_board[M - 1]))

