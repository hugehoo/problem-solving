from collections import deque
import sys

R, C = map(int, sys.stdin.readline().split())
j_queue, f_queue = deque(), deque()
board = [list(sys.stdin.readline()) for _ in range(R)]
visited, j_visited = [[0] * C for _ in range(R)], [[0] * C for _ in range(R)]  # declare fire, jihoon visited

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for r in range(R):
    for c in range(C):
        if board[r][c] == "F":
            f_queue.append((r, c))
        elif board[r][c] == "J":
            j_queue.append((r, c))


def bfs():
    while f_queue:
        _r, _c, = f_queue.popleft()
        for i in range(4):
            ny = _r + dy[i]
            nx = _c + dx[i]

            if 0 <= nx < C and 0 <= ny < R:
                if not visited[ny][nx] and board[ny][nx] != "#":
                    visited[ny][nx] = visited[_r][_c] + 1
                    f_queue.append((ny, nx))

    while j_queue:
        _r, _c = j_queue.popleft()

        for i in range(4):
            ny = _r + dy[i]
            nx = _c + dx[i]

            if 0 <= nx < C and 0 <= ny < R:
                if not j_visited[ny][nx] and board[ny][nx] != "#":
                    if not visited[ny][nx] or visited[ny][nx] > j_visited[_r][_c] + 1:
                        j_visited[ny][nx] = j_visited[_r][_c] + 1
                        j_queue.append((ny, nx))
            else:
                return j_visited[_r][_c] + 1
    print(j_visited, visited)
    return "IMPOSSIBLE"


print(bfs())

"""
4 4
####
#JF#
#..#
#..#

4 4
####
JF.#
#..#
#..#

3 3
###
#J#
F.#

3 4
###F
.J#.
###.


3 3
F.F
.J.
F.F
"""
