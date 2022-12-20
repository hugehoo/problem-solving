import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
queue = deque()
mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]
count = 1
queue.append((0, 0, count))
result = []
visited = []
while queue:
    n_, m_, count_ = queue.popleft()
    for i in range(4):
        ny = n_ + my[i]
        nx = m_ + mx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue

        if ny == N - 1 and nx == M - 1:
            result.append(count_ + 1)

        if board[ny][nx] == 1 and (ny, nx) not in visited:  # and (ny, nx) not in visited:
            queue.append((ny, nx, count_ + 1))
            visited.append((ny, nx))
print(min(result))




