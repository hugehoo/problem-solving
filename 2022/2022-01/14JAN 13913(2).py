from collections import deque

N, K, = map(int, input().split())


def path(x):
    arr = []
    temp = x
    for _ in range(dist[x] + 1):
        arr.append(temp)
        temp = move[temp]
    print(' '.join(map(str, arr[::-1])))


def bfs():
    q = deque()
    q.append(N)
    while q:
        x = q.popleft()
        if x == K:
            print(dist[x])
            path(x)
            return x
        for i in (x + 1, x - 1, 2 * x):
            if 0 <= i <= 100000 and dist[i] == 0:
                q.append(i)
                dist[i] = dist[x] + 1
                move[i] = x


dist = [0] * 100001  # 각 노드 별 걸리는 시간
move = [0] * 100001  # 각 노드의 이전 노드 (부모 노드)
bfs()
