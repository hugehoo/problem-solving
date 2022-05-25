import sys
from copy import deepcopy

input = sys.stdin.readline

M = int(input())
board = []
max_board = [[], []]
min_board = [[], []]
for m in range(M):
    _list = list(map(int, input().split()))
    board.append(_list)

max_board[0] = deepcopy(board[0])
min_board[0] = deepcopy(board[0])
max_board[1] = [0, 0, 0]
min_board[1] = [0, 0, 0]

for r in range(1, M):
    for c in range(3):
        if c == 0:
            max_board[1][c] = max(max_board[0][c], max_board[0][c + 1]) + board[r][c]
            min_board[1][c] = min(min_board[0][c], min_board[0][c + 1]) + board[r][c]
        elif c == 1:
            max_board[1][c] = max(max_board[0][c - 1], max_board[0][c], max_board[0][c + 1]) + board[r][c]
            min_board[1][c] = min(min_board[0][c - 1], min_board[0][c], min_board[0][c + 1]) + board[r][c]
        else:
            max_board[1][c] = max(max_board[0][c], max_board[0][c - 1]) + board[r][c]
            min_board[1][c] = min(min_board[0][c], min_board[0][c - 1]) + board[r][c]
    if r == M - 1:
        print(max(max_board[1]), min(min_board[1]))
        break
    max_board[0], max_board[1] = max_board[1], max_board[0]
    min_board[0], min_board[1] = min_board[1], min_board[0]


"""
위 아래 컬럼 두개를 만들어야 한다.
2 x 3 배열을 만들고, 때가 되면 위아래를 스왑? 
"""
