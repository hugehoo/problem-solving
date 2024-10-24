from sys import stdin
from collections import deque

input = stdin.readline


def bfs(number: int):
    distance = [[-1] * N for _ in range(N)]
    q = deque()
    for r in range(N):
        for c in range(N):
            if board[r][c] == number:
                q.append((r, c))
                distance[r][c] = 0
    while q:
        r_, c_, = q.popleft()
        for i in range(4):
            ny = dy[i] + r_
            nx = dx[i] + c_
            if 0 <= ny < N and 0 <= nx < N:
                # 다른 섬을 만날때
                if board[ny][nx] != number and board[ny][nx] != 0:
                    return distance[r_][c_]
                # 그냥 바다일 때
                if board[ny][nx] == 0 and distance[ny][nx] == -1:
                    distance[ny][nx] = distance[r_][c_] + 1
                    q.append((ny, nx))


if __name__ == '__main__':
    N = int(input().rstrip())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    island_number = 1
    
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for r in range(N):
        for c in range(N):
            if board[r][c] == 1 and not visited[r][c]:
                q = deque()
                board[r][c] = island_number
                q.append((r, c))
                while q:
                    nr, nc = q.popleft()
                    visited[nr][nc] = 1
                    for i in range(4):
                        ny = dy[i] + nr
                        nx = dx[i] + nc
                        if 0 <= ny < N and 0 <= nx < N and board[ny][nx] and not visited[ny][nx]:
                            visited[ny][nx] = 1
                            board[ny][nx] = island_number
                            q.append((ny, nx))
                island_number += 1
    # for b in board:
    #     print(b)
    # print('island ', island_number)
    # for v in visited:
    #     print(v)
    
    min_distance = float('inf')
    for number in range(1, island_number):
        min_distance = min(bfs(number), min_distance)
    print(min_distance)
