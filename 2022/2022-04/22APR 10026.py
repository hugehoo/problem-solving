import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
board_ = [list(input().strip()) for _ in range(N)]


def find(board):
    count = 0
    visited = [[0] * N for _ in range(N)]
    queue = deque()
    queue.append((0, 0))
    mx = [1, -1, 0, 0]
    my = [0, 0, 1, -1]

    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                queue.append((r, c))
                while queue:
                    r_, c_ = queue.popleft()
                    for i in range(4):
                        ny = r_ + my[i]
                        nx = c_ + mx[i]
                        if ny < 0 or ny >= N or nx < 0 or nx >= N:
                            continue
                        if board[ny][nx] == board[r_][c_] and visited[ny][nx] == 0:
                            queue.append((ny, nx))
                            visited[ny][nx] = -1
                count += 1
    return count


first = find(board_)
for r in range(N):
    for c in range(N):
        if board_[r][c] == "R":
            board_[r][c] = "G"
second = find(board_)
print(first, second)

"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""
