from sys import stdin
from collections import deque

input = stdin.readline


def rgb(colors: list):
    visited = [[0] * N for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    number = 0
    for color in colors:
        for r in range(N):
            for c in range(N):
                if board[r][c] == color and not visited[r][c]:
                    q.append((r, c))
                    while q:
                        r_, c_ = q.popleft()
                        visited[r_][c_] = 1
                        for i in range(4):
                            ny = dy[i] + r_
                            nx = dx[i] + c_
                            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx] and board[ny][nx] == color:
                                q.append((ny, nx))
                                visited[ny][nx] = 1
                    number += 1
    return number

def rg_b(colors: list):
    visited = [[0] * N for _ in range(N)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    q = deque()
    number = 0
    for color in colors:
        for r in range(N):
            for c in range(N):
                if (board[r][c] == color or (board[r][c] == "G" and color == "R")) and not visited[r][c]:
                    q.append((r, c))
                    while q:
                        r_, c_ = q.popleft()
                        visited[r_][c_] = 1
                        for i in range(4):
                            ny = dy[i] + r_
                            nx = dx[i] + c_
                            if 0 <= ny < N and 0 <= nx < N \
                                    and not visited[ny][nx] \
                                    and (board[ny][nx] == color or (board[ny][nx] == "G" and color == "R")):
                                q.append((ny, nx))
                                visited[ny][nx] = 1
                    number += 1
    return number

if __name__ == '__main__':
    N = int(input().rstrip())
    board = [list(input().rstrip()) for _ in range(N)]
    print(rgb(["R", "G", "B"]))
    print(rg_b(["R", "B"]))
    
    
"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR

5
RBRBB
RRBGG
BBRBR
RRRBB
RRRBR

2
GR
GR
"""