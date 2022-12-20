import heapq
import sys


input = sys.stdin.readline
v, k = map(int, input().split())
s = int(input())
dp = [float('inf')] * (v + 1)
heap = []
graph = [[] for _ in range(v + 1)]

for i in range(k):
    v1, v2, w = map(int, input().split())
    graph[v1].append([w, v2])


def dijkstra(start):
    dp[start] = 0
    heapq.heappush(heap, [0, start])
    while heap:
        wei, now = heapq.heappop(heap)

        if dp[now] < wei:
            continue

        for w, next_node in graph[now]:
            next_wei = wei + w
            if next_wei < dp[next_node]:
                dp[next_node] = next_wei
                heapq.heappush(heap, [next_wei, next_node])


# dijkstra(s)
for i in range(1, v + 1):
    print("INF" if dp[i] == float('inf') else dp[i])
