import sys
from collections import defaultdict

read = sys.stdin.readline
N = int(read())
graph_dict = defaultdict(set)
visited = []

for _ in range(int(read())):
    a, b = map(int, read().split())
    graph_dict[a].add(b)
    graph_dict[b].add(a)


def dfs(start, graph):
    for i in graph[start]:
        if i not in visited:
            visited.append(i)
            dfs(i, graph)


dfs(1, graph_dict)
print(len(visited) - 1)
