from collections import deque, defaultdict


def solution(tickets):
    graph = defaultdict(list)
    START = "ICN"
    route = []
    for start, end in sorted(tickets, reverse=True):
        graph[start].append(end)

    def dfs(to):
        while graph[to]:
            dfs(graph[to].pop())
        route.append(to)
    dfs(START)
    return route[::-1]


solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]])
solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]])
