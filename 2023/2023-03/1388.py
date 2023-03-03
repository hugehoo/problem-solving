R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
count = 0


def search_horizon(r, c):
    global count
    if c - 1 >= 0:
        if not visited[r][c - 1] and board[r][c - 1] == '-':
            # count += 1
            visited[r][c - 1] = 1
            search_horizon(r, c - 1)
    if c + 1 < C:
        if not visited[r][c + 1] and board[r][c + 1] == '-':
            # count += 1
            visited[r][c + 1] = 1
            search_horizon(r, c + 1)
    # count += 1
    return


def search_vertical(r, c):
    global count
    if r - 1 >= 0:
        if not visited[r - 1][c] and board[r - 1][c] == '|':
            visited[r - 1][c] = 1
            search_vertical(r - 1, c)
    if r + 1 < R:
        if not visited[r + 1][c] and board[r + 1][c] == '|':
            visited[r + 1][c] = 1
            search_vertical(r + 1, c)
    return


for r in range(R):
    for c in range(C):
        if board[r][c] == '-' and not visited[r][c]:
            visited[r][c] = 1
            search_horizon(r, c)
            count += 1
        elif board[r][c] == '|' and not visited[r][c]:
            visited[r][c] = 1
            search_vertical(r, c)
            count += 1

print(count)
