import sys
from collections import deque, defaultdict


input = sys.stdin.readline

n, m = map(int, input().split())
count = 0
queue = deque()
visited = [0] * (n + 1)
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    if visited[i] == 1:
        continue
    queue.append(i)
    while queue:
        pop = queue.popleft()
        if visited[pop] == 0:
            visited[pop] = 1
            for p in graph[pop]:
                queue.append(p)
    count += 1
print(count)

"""
6 5
1 2
2 5
5 1
3 4
4 6
"""