import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

min_v, max_v = 1, 1

for b in board:
    max_v = max(max_v, max(b))
    min_v = min(min_v, min(b))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
max_count = 0
for d in range(0, max_v + 1):
    temp = deepcopy(board)
    visited, queue = [[False] * N for _ in range(N)], deque()
    for r in range(N):
        for c in range(N):
            # if board[r][c] <= d and (r, c) not in visited: not in ~ 이게 시간 복잡도를 높일 수도 있다.
            if board[r][c] <= d and not visited[r][c]:
                queue.append((r, c))
                visited[r][c] = True

                while queue:
                    r_, c_ = queue.popleft()
                    temp[r_][c_] = 0

                    for i in range(4):
                        ny = dy[i] + r_
                        nx = dx[i] + c_
                        if 0 <= ny < N and 0 <= nx < N and board[ny][nx] <= d and not visited[ny][nx]:
                            temp[ny][nx] = 0
                            queue.append((ny, nx))
                            visited[ny][nx] = True

    # temp 를 상대로 문자가 아닌 것들의 갯수를 구한다.
    queue = deque()
    visited = [[False] * N for _ in range(N)]
    count = 0
    for r in range(N):
        for c in range(N):
            if temp[r][c] > 0 and not visited[r][c]:
                queue.append((r, c))
                visited[r][c] = True
                while queue:
                    r_, c_ = queue.popleft()
                    for i in range(4):
                        ny = dy[i] + r_
                        nx = dx[i] + c_
                        if 0 <= ny < N and 0 <= nx < N and temp[ny][nx] > 0 and not visited[ny][nx]:
                            queue.append((ny, nx))
                            visited[ny][nx] = True
                count += 1
    max_count = max(max_count, count)

print(max_count)
