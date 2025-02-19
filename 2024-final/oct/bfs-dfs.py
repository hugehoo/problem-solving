from collections import deque


def dfs(graph, start_node):
    visited = []
    stack = [start_node]
    
    while stack:
        element = stack.pop()
        if element not in visited:
            visited.append(element)
            stack.extend(reversed(graph[element]))
    return visited


def bfs(graph, start_node):
    queue = deque()
    visited = []
    queue.append(start_node)
    
    while queue:
        element = queue.popleft()
        if element not in visited:
            visited.append(element)
            queue.extend(graph[element])
    return visited



# def bfs(graph, start_node) -> list:
#     visited = list()
#     q = list()
#     q.append(start_node)
#     while q:
#         element = q.pop(0)
#         if element not in visited:
#             visited.append(element)
#             q.extend(graph[element])
#     return visited
#
#
# def dfs(graph, start_node) -> list:
#     visited = []
#     stack = [start_node]
#     while stack:
#         element = stack.pop()
#         if element not in visited:
#             visited.append(element)
#             stack.extend(reversed(graph[element]))
#     return visited


myGraph = {
    'A': ['B', 'C', 'D'],
    'B': ['A', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['A', 'H'],
    'E': ['B', 'I'],
    'F': ['C', 'J'],
    'G': ['C'],
    'H': ['D'],
    'I': ['E'],
    'J': ['F']
}

print("dfs:", dfs(myGraph, "A"))
print("bfs:", bfs(myGraph, "A"))

""""
    A
B   C   D
E  F G  H
I  J
"""
