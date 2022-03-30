import heapq


def solution(jobs):
    result = []
    heap = []
    answer = []
    for j in jobs:
        heapq.heappush(heap, j)

    # 가장 먼저 시작하는 녀석을 찾자.
    first = heapq.heappop(heap)
    result.append(first[1])
    answer.append(first[1])
    # heapq 에서 2개를 꺼내본다.
    # 비교를 한다. 어떻게? result[-1] + pops[-1] + (result[-1] - pops[0])
    while len(heap) >= 2:
        pops1 = heapq.heappop(heap)
        pops2 = heapq.heappop(heap)
        a = sum(result) + pops1[-1] - pops1[0]
        b = sum(result) + pops2[-1] - pops2[0]
        if a < b:
            heapq.heappush(heap, pops2)
            result.append(pops1[-1])
            answer.append(a)
        else:
            heapq.heappush(heap, pops1)
            result.append(pops2[-1])
            answer.append(b)
    if heap:
        pops1 = heapq.heappop(heap)
        a = sum(result) + pops1[-1] - pops1[0]
        answer.append(a)
        result.append(pops1[-1])

    return sum(answer) // len(answer)


print(solution([[0, 3], [1, 9], [2, 6]]))
