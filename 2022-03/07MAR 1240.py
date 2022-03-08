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
    global n
    global graph
    root = deque()
    root.append(start)
    way = [0] * (n + 1)
    visited = [0] * (n + 1)

    while root:
        current = root.popleft()
        if current == end:
            break
        if visited[current] == 0:
            visited[current] = 1
            for next_node in graph[current]:
                root.append(next_node[0])
                way[next_node[0]] = way[current] + next_node[1]
    return way[end]


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
