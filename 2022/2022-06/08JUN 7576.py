import sys
from collections import deque
from itertools import chain

input = sys.stdin.readline

C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
init_q = deque()
visited = [[0] * C for _ in range(R)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for r in range(R):
    for c in range(C):
        if board[r][c] == 1: init_q.append([r, c])

while init_q:
    y_, x_ = init_q.popleft()
    for i in range(4):
        ny = y_ + dy[i]
        nx = x_ + dx[i]
        if 0 <= ny < R and 0 <= nx < C and board[ny][nx] == 0:
            board[ny][nx] = board[y_][x_] + 1
            init_q.append([ny, nx])
for b in chain(*board):
    if b == 0:
        print(-1)
        exit()
else:
    print(max(chain(*board)) - 1)
