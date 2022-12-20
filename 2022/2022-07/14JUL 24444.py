import sys
from collections import deque, defaultdict


input = sys.stdin.readline
n, m, r = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n + 1):
    graph[i].sort()
queue = deque()
queue.append(r)
visited = set()
visited.add(r)
answer = [0] * (n + 1)
answer[r] = 1
count = 2
while queue:
    pops = queue.popleft()
    for v in graph[pops]:
        if v not in visited:  # 이건 O(n) 시간복잡도 걸린다. 배열을 사용할꺼면 차라리 인덱스 접근을 하라.
            answer[v] = count
            count += 1
            queue.append(v)
            visited.add(v)

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

