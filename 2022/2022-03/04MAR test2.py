from collections import defaultdict


def solution(N, number):
    def calculate2(param: set, param2: set, temp:set):
        # temp = set() # 이게 여기 있으면 안돼.
        for p in param:
            for p2 in param2:
                temp.add(p + p2)
                temp.add(p - p2)
                temp.add(p * p2)
                if p2 != 0:
                    temp.add(p // p2)
        return temp

    graph = defaultdict(set)
    graph[1].add(N)

    for i in range(1, 9):
        i_set = set()
        for j in range(i):
            graph[i] = calculate2(graph[j], graph[i - j], i_set)
            graph[i].add(int(str(N) * i))
        if number in graph[i]:
            return i
    return -1


print(solution(5, 12))
print(solution(2, 11))
