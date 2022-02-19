from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque()
queue.append(N)
dist = [-1] * 100001  # 방문을 하지 않은 것과 (-1), 초기 위치의 값(0) 은 엄연히 달라야한다.
dist[N] = 0
cnt = 0
while queue:
    x = queue.popleft()
    if x == K:
        cnt += 1
    for y in [x - 1, x + 1, 2 * x]:
        if 0 <= y <= 100000 and (dist[y] == -1 or dist[y] >= dist[x] + 1):
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
