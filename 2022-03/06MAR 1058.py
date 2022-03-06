import sys
from collections import defaultdict, deque

n = int(sys.stdin.readline())
board = []
graph = defaultdict(list)
answer = 0

for i in range(1, n + 1):
    arr = list(sys.stdin.readline().rstrip())
    graph[i] = [idx + 1 for idx, a in enumerate(arr) if a == "Y"]

for i in range(1, n + 1):
    queue, two_i = deque(), set()
    for g in graph[i]:
        queue.append(g)
        two_i.add(g)
    while queue:
        pops = queue.popleft()
        for g in graph[pops]:
            two_i.add(g)
    answer = max(answer, len(two_i))
print(0 if answer == 0 else answer - 1)
