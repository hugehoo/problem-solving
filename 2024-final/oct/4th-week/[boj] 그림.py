from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    visited = [[0] * m for _ in range(n)]
    count = 0
    max_area = float('-inf')
    for r in range(n):
        for c in range(m):
            if board[r][c] == 1 and not visited[r][c]:
                stack = [(r, c)]
                area = 1
                visited[r][c] = 1
                while stack:
                    r_, c_ = stack.pop()
                    visited[r_][c_] = 1
                    for i in range(4):
                        ny = dy[i] + r_
                        nx = dx[i] + c_
                        if 0 <= ny < n and 0 <= nx < m and not visited[ny][nx] and board[ny][nx] == 1:
                            visited[ny][nx] = 1
                            stack.append((ny, nx))
                            area += 1
                count += 1
                max_area = max(max_area, area)
    print(count)
    print(max_area if max_area != float('-inf') else 0)
    
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
