import sys
from itertools import chain

input = sys.stdin.readline
n, m, = map(int, input().split())
board = [[0] * 100 for _ in range(100)]
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1 - 1, y2):
        for x in range(x1 - 1, x2):
            board[y][x] += 1
answer = 0
for line in chain(board):
    for l in line:
        if m < l:
            answer += 1
print(answer)
