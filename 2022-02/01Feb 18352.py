from collections import deque
import sys

input = sys.stdin.readline

N, M, K, X = map(int, input().split())

connect = [[] for _ in range(N)]
visited = [False] * N
visited[X - 1] = True
distance = [0] * N
for _ in range(M):
    v1, v2 = map(int, input().split())
    connect[v1 - 1].append(v2)
queue = deque([X])
while queue:
    c = queue.popleft()
    for city in connect[c - 1]:
        if not visited[city - 1]:
            visited[city - 1] = True
            distance[city - 1] = distance[c - 1] + 1
            queue.append(city)
for i in range(N):
    if distance[i] == K:
        print(i + 1)
if K not in distance:
    print(-1)














# for _ in range(M):
#     f, t = map(int, input().split())
#     connect[f - 1].append(t)
# queue = deque([X])
# answer = []
# while queue:
#     c = queue.popleft()
#     for city in connect[c - 1]:
#         if not visited[city - 1]:
#             queue.append(city)
#             distance[city - 1] = distance[c - 1] + 1
#             visited[city - 1] = True
# for i in range(N):
#     if distance[i] == K:
#         print(i + 1)
# if K not in distance:
#     print(-1)


