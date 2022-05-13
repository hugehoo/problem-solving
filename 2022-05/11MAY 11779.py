import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
board = [[float('inf')] * n for _ in range(n)]
for i in range(m):
    a, b, c = map(int, input().split())
    board[a - 1][b - 1] = c
    board[b - 1][a - 1] = c
    if i < n:
        board[i][i] = 0
    # board.append([a, b, c])
start, end = map(int, input().split())
for k in range(n):
    for r in range(n):
        for c in range(n):
            board[r][c] = min(board[r][k] + board[k][c], board[r][c])
for b in board:
    print(b)
"""
5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
"""
