from collections import deque

N, M = map(int, input().split())
queue = deque()
board, visit = [list(input()) for _ in range(M)], [[0] * N for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
result = [0, 0]

for m in range(M):
    for n in range(N):
        count = 0
        if not visit[m][n]:
            visit[m][n] = 1
            count += 1
            queue.append([m, n])

        while queue:
            y, x = queue.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < N and 0 <= ny < M and board[y][x] == board[ny][nx] and not visit[ny][nx]:
                    visit[ny][nx] = 1
                    queue.append([ny, nx])
                    count += 1

        if board[m][n] == "W":
            result[0] += count ** 2
        else:
            result[1] += count ** 2

print(*result)

"""
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
"""
