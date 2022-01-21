from collections import defaultdict


def solution(N, number):
    def calculate(param: set):
        temp = set()

        for p in param:
            temp.add(p + N)
            temp.add(p - N)
            temp.add(p * N)
            temp.add(p // N)
        return temp

    graph = defaultdict(set)
    graph[1].add(N)

    for i in range(2, 9):
        graph[i] = calculate(graph[i - 1])
        graph[i].add(int(str(N) * i))
        if number in graph[i]:
            return i
    return -1


print(solution(5, 12))
print(solution(2, 11))
