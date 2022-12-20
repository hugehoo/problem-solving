from collections import deque

graph = {
    1: [2, 3, 4],
    2: [5],
    3: [5],
    4: [],
    5: [6, 7],
    6: [],
    7: [3],
}


# def recursive_dfs(v, visited=[]):
#     visited.append(v)  # 시작 정점 방문
#     for w in graph[v]:
#         if not w in visited:  # 방문 하지 않았으면
#             visited = recursive_dfs(w, visited)
#     return visited
#
#
# print(recursive_dfs(1, []))


def bfs(start_v):
    visited = [start_v]
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
    return visited


print(bfs(1))
