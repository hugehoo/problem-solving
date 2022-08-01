import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
board = [list(input().rstrip()) for _ in range(M)]

visited = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result_v = 0
result_o = 0

for m in range(M):
    for n in range(N):
        queue = deque()
        temp = []
        if board[m][n] in ["v", "o", "."] and [m, n] not in visited:
            queue.append([m, n])
            temp.append(board[m][n])
            visited.append([m, n])
            while queue:
                m_, n_ = queue.popleft()
                for i in range(4):
                    nx = dx[i] + n_
                    ny = dy[i] + m_
                    if nx < 0 or N <= nx or ny < 0 or M <= ny:
                        continue
                    if board[ny][nx] == '#':
                        continue
                    if [ny, nx] not in visited:
                        queue.append([ny, nx])
                        temp.append(board[ny][nx])
                        visited.append([ny, nx])
        if temp:
            if temp.count('v') < temp.count('o'):
                result_o += temp.count('o')
            else:
                result_v += temp.count('v')
print(result_o, result_v)