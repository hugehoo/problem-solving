def dfs(r, c, total):
    global maximum
    maximum = max(maximum, total)
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m and graph[nr][nc] not in s:
            s.add(graph[nr][nc])
            dfs(nr, nc, total + 1)
            s.remove(graph[nr][nc])


n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]

maximum = 0
s = set()
s.add(graph[0][0])

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]
dfs(0, 0, 1)

print(maximum)

# start = board[0][0]
# visited = [start]
#
# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]
# last = []
# queue = deque()
# queue.append([0, 0])
# for r in range(R):
#     for c in range(C):
#         while queue:
#             r_, c_ = queue.popleft()
#
#             before = len(visited)
#             for i in range(4):
#                 nx = dx[i] + c_
#                 ny = dy[i] + r_
#                 if 0 <= nx < C and 0 <= ny < R and board[ny][nx] not in visited:
#                     queue.append((ny, nx))
#                     visited.append(board[ny][nx])
#                     last = [ny, nx]
#
#             after = len(visited)
#             if before == after and not queue:
#                 print(visited)
#                 print(after)
#                 exit()

""" 어느 순서로 먼저 받느냐에 따라 결과가 달라진다. 
"""
