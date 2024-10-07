import sys
from collections import deque, defaultdict


def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(sorted(set(graph[node]) - set(visited), reverse=True))
    return visited


def bfs(graph, start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            queue.extend(sorted(set(graph[node]) - set(visited)))
    return visited


graph = defaultdict(list)
input = sys.stdin.readline
node, edge, start = [int(i) for i in input().split()]

for i in range(edge):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
    graph[node2].append(node1)

for key in graph:
    graph[key] = list(set(graph[key]))

print(*dfs(graph, start))
print(*bfs(graph, start))
