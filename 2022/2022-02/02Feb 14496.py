import heapq
import sys

input = sys.stdin.readline

to, target = map(int, input().split())
N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
heap = []
distance = [float('inf')] * (N + 1)


for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

heapq.heappush(heap, [0, to])
distance[to] = 0

while heap:
    cost, dest = heapq.heappop(heap)
    if distance[dest] < cost:
        continue
    # if dest == target: # 93% 에러
    #     print(distance[target])
    #     exit()
    for node in graph[dest]:
        if distance[node] > cost + 1:
            distance[node] = cost + 1
            heapq.heappush(heap, [distance[node], node])
if distance[target] != float('inf'):
    print(distance[target])
else:
    print(-1)




