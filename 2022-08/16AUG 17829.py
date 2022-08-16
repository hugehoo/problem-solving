import sys

input = sys.stdin.readline

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

while N != 1:
    small_board = []
    for r in range(0, N, 2):  # for row
        temp_row = []
        for c in range(0, N, 2):  # for column
            temp = sorted([board[r][c], board[r][c + 1], board[r + 1][c], board[r + 1][c + 1]])
            temp_row.append(temp[2])
        small_board.append(temp_row)
    N //= 2
    board = small_board

for b in board:
    print(*b)

"""
8
-1 2 14 7 4 -5 8 9
10 6 23 2 -1 -1 7 11
9 3 5 -2 4 4 6 6
7 15 0 8 21 20 6 6
19 8 12 -8 4 5 2 9
1 2 3 4 5 6 7 8
9 10 11 12 13 14 15 16
17 18 19 20 21 22 23 24
"""
