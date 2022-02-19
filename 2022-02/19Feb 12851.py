from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque()
queue.append(N)
# queue.append([N, 0, N])
result = []
visited = []
dist = [0] * 100001
cnt = 0
while queue:
    x = queue.popleft()
    if x == K:
        cnt += 1
        # print(dist[x])
    for y in [x - 1, x + 1, 2 * x]:
        if 0 <= y <= 100000 and (dist[y] == 0 or dist[y] >= dist[x] + 1):
            # if dist[y] == 0 or dist[y] >= dist[x] + 1:
            dist[y] = dist[x] + 1
            queue.append(y)
print(dist[K])
print(cnt)

"""
N - 1
N + 1
2 * N

"""

"""
5 17

4
2
"""
