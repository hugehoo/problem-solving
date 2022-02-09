import heapq
from math import inf
import sys

input = sys.stdin.readline
N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])


def dijkstra(start):
    distance = [inf] * (N + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # heap 이기 때문에 거리가 짧은 노드부터 출력된다.
        dist, now = heapq.heappop(q)  # dist 는 start 로 부터 각각의 now 까지의 거리
        if distance[now] < dist:
            print('di', dist, 'now ', now, ' distance ', distance[now])
            # continue
        for i in graph[now]:   # 시작점과 연결된 (노드, 소요시간)
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    print('distance = ', distance)
    return distance


v1, v2 = map(int, input().split())
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[N]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[N]

result = min(v1_path, v2_path)
print(result if result < inf else -1)





# graph = [[0] * N for _ in range(N)]
# for _ in range(E):
#     a, b, c = map(int, input().split())
#     if c == 0:
#         graph[a - 1][b - 1] = float('inf')
#         graph[b - 1][a - 1] = float('inf')
#     graph[a - 1][b - 1] = c
#     graph[b - 1][a - 1] = c
#
# v1, v2 = map(int, input().split())
# for r in graph:
#     print(r)
# first = float('inf')
# second = float('inf')
# third = float('inf')
#
# first_ = float('inf')
# second_ = float('inf')
# third_ = float('inf')
#
# for idx, row in enumerate(graph):
#
#
#     first = min(graph[0][idx] + graph[idx][v1 - 1], first)
#     second = min(graph[v1 - 1][idx] + graph[idx][v2 - 1], second)
#     third = min(graph[v2 - 1][idx] + graph[idx][N - 1], third)
#
#     first_ = min(graph[0][idx] + graph[idx][v2 - 1], first_)
#     second_ = min(graph[v2 - 1][idx] + graph[idx][v1 - 1], second_)
#     third_ = min(graph[v1 - 1][idx] + graph[idx][N - 1], third_)
#
# print(min(first + second + third, first_ + second_ + third_))



"""
6 6 
5 4 3
5 3 6 
1 3 9 
1 4 1 
5 1 6 
3 4 4 
5 2



8 8 
1 2 4 
1 7 6 
2 8 1 
2 4 2 
3 8 3 
4 5 4 
5 7 3 
7 8 5 
2 7

"""