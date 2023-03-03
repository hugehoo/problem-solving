R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
count = 0


def search_horizon(r, c):
    up_c = c - 1
    down_c = c + 1

    if up_c >= 0:
        if not visited[r][up_c] and board[r][up_c] == '-':
            visited[r][up_c] = 1
            search_horizon(r, up_c)
    if down_c < C:
        if not visited[r][down_c] and board[r][down_c] == '-':
            visited[r][down_c] = 1
            search_horizon(r, down_c)
    return


def search_vertical(r, c):
    left_r = r - 1
    right_r = r + 1
    
    if left_r >= 0:
        if not visited[left_r][c] and board[left_r][c] == '|':
            visited[left_r][c] = 1
            search_vertical(left_r, c)
    if right_r < R:
        if not visited[right_r][c] and board[right_r][c] == '|':
            visited[right_r][c] = 1
            search_vertical(right_r, c)
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
