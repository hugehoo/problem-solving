from collections import deque


N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]

queue = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for _ in range(K):
    a, b = map(int, input().split())
    board[a - 1][b - 1] = 1

max_count = -1
count = 0
for r in range(N):
    for c in range(M):
        if board[r][c] == 1:
            queue.append((r, c))
            visited[r][c] = 1
            count += 1

            while queue:
                a, b = queue.popleft()
                for i in range(4):
                    ny = a + dy[i]
                    nx = b + dx[i]

                    # if ny <= -1 or ny >= N or nx <= -1 or nx >= M:
                    #     continue

                    if 0 <= ny < N and 0 <= nx < M and board[ny][nx] == 1 and visited[ny][nx] == 0:
                        queue.append((ny, nx))
                        visited[ny][nx] = 1
                        count += 1
            max_count = max(max_count, count)
            count = 0
print(max_count)
