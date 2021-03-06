from collections import deque
from itertools import chain
from sys import stdin

M, N, H = map(int, stdin.readline().split())
board = []
queue = deque()

for h in range(H):
    temp = []
    for n in range(N):
        temp.append(list(map(int, stdin.readline().split())))
        for m in range(M):
            if temp[n][m] == 1:
                queue.append((h, n, m))
    board.append(temp)

visited = []
dh = [0, 0, 0, 0, 1, -1]
dc = [0, 0, 1, -1, 0, 0]
dr = [1, -1, 0, 0, 0, 0]
while queue:
    h, r, c = queue.popleft()
    for i in range(6):
        nh = h + dh[i]
        nr = r + dr[i]
        nc = c + dc[i]
        if nh < 0 or nh >= H or nc < 0 or nc >= M or nr < 0 or nr >= N:
            continue
        if board[nh][nr][nc] == 0:
            queue.append((nh, nr, nc))
            board[nh][nr][nc] = board[h][r][c] + 1
answer = 1
for b in board:
    for c in chain(b):
        if 0 in c:
            print(-1)
            exit()
        else:
            answer = max(max(c), answer)

print(answer - 1)

