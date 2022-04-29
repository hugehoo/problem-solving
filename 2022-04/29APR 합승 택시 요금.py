from collections import defaultdict


def solution(n, s, a, b, fares):
    taxi = defaultdict(list)
    for i in range(n):
        taxi[i] = [float('inf')] * n

    for st, e, f in fares:
        taxi[st - 1][e - 1] = f
        taxi[e - 1][st - 1] = f
    for i in range(n):
        taxi[i][i] = 0
    for k in range(n):
        for a_ in range(n):
            for b_ in range(n):
                taxi[a_][b_] = min(taxi[a_][b_], taxi[a_][k] + taxi[k][b_])
    min_ = float('inf')
    for k in range(n):
        min_ = min(min_, taxi[s - 1][k] + taxi[k][a - 1] + taxi[k][b - 1])
    return min_


print(solution(6, 4, 6, 2,
               [[4, 1, 10],
                [3, 5, 24],
                [5, 6, 2],
                [3, 1, 41],
                [5, 1, 24],
                [4, 6, 50],
                [2, 4, 66],
                [2, 3, 22],
                [1, 6, 25]]))
print(solution(7, 3, 4, 1,
               [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))

"""
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])    
각각의 최소 경로를 구해보자. 그 경로중 겹치는게 있느지 체크
4 -> 6
4 -> 2
"""
