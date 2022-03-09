import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    x, y, value = map(int, input().split())
    graph[x].append([y, value])
    graph[y].append([x, value])


def bfs(start, end):
    visited, dist = [0] * (n + 1), [0] * (n + 1)
    queue = deque([start])
    while queue:
        current = queue.popleft()
        if current == end:
            return dist[end]

        if not visited[current]:
            visited[current] = 1
            for next_node in graph[current]:
                queue.append(next_node[0])
                dist[next_node[0]] = next_node[1] + dist[current]


for _ in range(m):
    start, end = map(int, input().split())
    print(bfs(start, end))



"""
4 2
2 1 2
4 3 2
1 4 3
1 2
3 2
"""
