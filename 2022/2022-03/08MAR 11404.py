import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[float('inf')] * (n + 1) for _ in range(n + 1)]
for rdx, row in enumerate(graph):
    for cdx, c in enumerate(row):
        if rdx == cdx:
            graph[rdx][cdx] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == float('inf'): # 이 부분 없으면 틀린다.
            graph[i][j] = 0
        print(graph[i][j], end=' ')
    print('')

"""
4 2
2 1 2
4 3 2
1 4 3
1 2
3 2
"""
