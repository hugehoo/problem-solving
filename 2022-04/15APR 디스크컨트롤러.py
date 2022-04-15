from heapq import heappop, heappush


def solution(jobs):
    answer, now, idx = 0, 0, 0
    start = -1
    heap = []

    while idx < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heappush(heap, [j[1], j[0]])
        if len(heap) > 0:
            current = heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            idx += 1
        else:
            now += 1
    return int(answer / len(jobs))


print(solution([[0, 10], [2, 10], [9, 10], [15, 2]]))  # 9
# print(solution([[0, 3], [1, 9], [2, 6]]))
