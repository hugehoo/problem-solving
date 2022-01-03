import sys
from collections import defaultdict, deque

read = sys.stdin.readline
N = int(read())  # 노드 수
M = int(read())

queue = deque()
graph_dict = defaultdict(set)
count = 1
for _ in range(M):
    a, b = map(int, read().split())
    graph_dict[a].add(b)
    graph_dict[b].add(a)

for i in graph_dict[1]:
    queue.append(i)

visited = [1]

while queue:
    pops = queue.popleft()
    if pops not in visited:
        for i in graph_dict[pops]:
            queue.append(i)
            visited.append(pops)
print(len(set(visited)) - 1)

"""
7
6
1 2
2 3
1 5
5 2
5 6
4 7
"""
