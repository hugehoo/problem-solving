import sys

sys.setrecursionlimit(10 ** 9)
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n + 1)]


def dfs(x, weight):
    for node, cost in graph[x]:
        if distance[node] == -1:
            distance[node] = weight + cost
            dfs(node, distance[node])
    return


for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append([b, c])
    graph[b].append([a, c])

distance = [-1] * (n + 1)
distance[1] = 0
dfs(1, 0)
farthest_index = distance.index(max(distance))

distance = [-1] * (n + 1)
distance[farthest_index] = 0
dfs(farthest_index, 0)
print(max(distance))

"""

leaf 의 두 노드를 당긴다. 
중간 노드는 당겨봤자, 더 긴 경우가 필연적으로 존재한다.

한 노드에서 다른 노드로 가는 경로의 값을 모두 안다고 할 때,
리프 노드끼리 값 중 가장 큰 것을 고르면 되는 거 아닌가??
그러려면 우선 리프노드가 무엇인지 따로 뽑아야한다.

=> 그냥 리프노드에서 출발하여 각 노드별로 가장 긴 거리를 찾으면 된다.
"""
