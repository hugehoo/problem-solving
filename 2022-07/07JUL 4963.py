import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

dx = [0, 0, 1, -1, 1, -1, 1, -1]
dy = [1, -1, 0, 0, 1, -1, -1, 1]

while True:
    w, h, = map(int, input().split())
    if w == h and h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = deepcopy(arr)
    queue = deque()
    count = 0
    for r in range(h):
        for c in range(w):
            if arr[r][c] == 1 and visited[r][c] == 1:
                count += 1
                queue.append((r, c))
                visited[r][c] = 0
            while queue:
                y, x = queue.popleft()
                for i in range(8):
                    ny = dy[i] + y
                    nx = dx[i] + x
                    if 0 <= ny < h and 0 <= nx < w and arr[ny][nx] == 1 and visited[ny][nx] == 1:
                        queue.append((ny, nx))
                        visited[ny][nx] = 0
    print(count)
"""
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
"""
