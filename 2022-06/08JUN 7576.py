import sys
from collections import defaultdict, deque
from copy import deepcopy


input = sys.stdin.readline

C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
init_q = deque()
visited = [[0] * C for _ in range(R)]
count = 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for r in range(R):
    for c in range(C):
        if board[r][c] == 1: init_q.append([r, c])

while True:
    another_q = deque()
    while init_q:
        y_, x_ = init_q.popleft()
        visited[y_][x_] = 1
        board[y_][x_] = "X"
        for i in range(4):
            ny = y_ + dy[i]
            nx = x_ + dx[i]
            if 0 > ny or R <= ny or nx < 0 or nx >= C:
                continue
            if board[ny][nx] == -1:
                continue
            if 0 <= ny < R and 0 <= nx < C and visited[ny][nx] == 0:
                visited[ny][nx] = 1
                board[ny][nx] = "X"
                another_q.append([ny, nx])
    count += 1
    if not init_q and not another_q:
        break
    else:
        init_q = deepcopy(another_q)

for b in board:
    if 0 in b:
        print(-1)
        exit()
print(count - 1)



