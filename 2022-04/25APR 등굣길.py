from collections import deque


def solution(m, n, puddles):
    board = [[0 for _ in range(m)] for _ in range(n)]
    for x, y in puddles:
        board[x - 1][y - 1] = -1
    queue = deque()
    queue.append((0, 0))

    dx = [1, 0]
    dy = [0, 1]
    board[0][0] = 1
    visited = []
    for r in range(0, n):
        for c in range(0, m):
            # queue append 할 조건이 뭐지
            while queue:
                y, x = queue.popleft()
                for i in range(2):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < m and 0 <= ny < n and board[ny][nx] != -1: # and (ny, nx) not in visited:
                        queue.append((ny, nx))
                        # visited.append((ny, nx))
                        board[ny][nx] += board[y][x]
    for b in board:
        print(b)
    return


print(solution(4, 3, [[2, 2]]))
