from collections import deque
import sys

input = sys.stdin.readline
N, K = map(int, input().split())
queue = deque()
queue.append([N, 0, N])
result = []
visited = set()
while queue:
    # 브레이크 조건
    # K 보다 커지면
    n, c, before = queue.popleft()
    if n == K:
        result.append(c)
        continue
    # if n in visited:
    #     continue

    if abs(n - K) > abs(before - K):
        continue

    # visited.add(n)
    # c += 1
    queue.append([n + 1, c + 1, n])
    queue.append([n - 1, c + 1, n])
    queue.append([n * 2, c + 1, n])
print(result)
print(min(result))
if min(result) == 0:
    print(0)
else:
    print(result.count(min(result)))

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
