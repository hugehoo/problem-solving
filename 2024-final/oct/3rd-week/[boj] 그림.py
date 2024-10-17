from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())  # row, column
    board = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    
    number = 0
    max_area = 0
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    area = 0
    for r in range(n):
        for c in range(m):
            stack = []
            if board[r][c] == 1 and not visited[r][c]:
                stack.append([r, c])
                visited[r][c] = 1
                number += 1
                area = 1
                while stack:
                    row, col = stack.pop()
                    for i in range(4):
                        nx = dx[i] + col
                        ny = dy[i] + row
                        if 0 <= ny < n and 0 <= nx < m and board[ny][nx] and not visited[ny][nx]:
                            stack.append([ny, nx])
                            visited[ny][nx] = 1
                            area += 1
                max_area = max(area, max_area)

    print(number)
    print(max_area)
    
