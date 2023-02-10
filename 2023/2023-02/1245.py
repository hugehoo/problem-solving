N, M = map(int, input().split())

count = 0
visited = [[0] * M for _ in range(N)]
farm = [list(map(int, input().split())) for _ in range(N)]
direction = [[0, 0, 1, -1, 1, -1, 1, -1], [1, -1, 0, 0, 1, -1, -1, 1]]


def dfs(r, c):
    global flag

    for i in range(8):
        nr = r + direction[0][i]
        nc = c + direction[1][i]
        
        visited[r][c] = 1
        # 탐색 범위이면서
        if 0 <= nr < N and 0 <= nc < M:
            if farm[r][c] < farm[nr][nc]:
                flag = False
            # 아직 방문 안하고,
            if not visited[nr][nc] and farm[r][c] == farm[nr][nc]:
                dfs(nr, nc)


for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            flag = True
            dfs(n, m)
            if flag:
                count += 1
print(count)


"""
주변보다 높은지 어떻게 확인하지?
같은 수끼리 묶어야 함.
8 방향으로 탐색해야 한다.

(0, 0) 부터 시작
주변 탐색 -> 자신보다 낮으면 flag = False -> count += 1
자신보다 낮으면 카운팅하지 않는다. 다만 방문했다는 기록만 남김.
방문하지 않은 곳 기준으로 다시 산봉우리 플래그를 연산

8 7
4 3 2 2 1 0 1
3 3 3 2 1 0 1
2 2 2 2 1 0 0
2 1 1 1 1 0 0
1 1 0 0 0 1 0
0 0 0 1 1 1 0
0 1 2 2 1 1 0
0 1 1 1 2 1 0
"""
