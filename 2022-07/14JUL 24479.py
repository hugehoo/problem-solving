import sys
from collections import defaultdict

input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = defaultdict(list)
sys.setrecursionlimit(1000000)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n + 1):
    graph[i].sort()

stack = [r]
answer = [0] * (n + 1)
count = 1


def dfs(answer, stack, count):
    if not stack:
        return
    pops = stack.pop()
    answer[pops] = count
    for v in graph[pops]:
        if not answer[v]:
            stack.append(v)
            dfs(answer, stack, count + 1)


dfs(answer, stack, count)
for a in answer[1::]:
    print(a)

"""
5 5 1
1 4
1 2
2 3
2 4
3 4
"""
