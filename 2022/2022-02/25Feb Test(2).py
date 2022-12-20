import heapq


# 2. 프로그래머스 2주차 2번문제
def solution(people, tshirts):
    people_heap = []
    tshirts_heap = []

    for p in people:
        heapq.heappush(people_heap, p)
    for t in tshirts:
        heapq.heappush(tshirts_heap, t)

    count = 0

    while tshirts_heap:
        if not people_heap:
            break
        p_size = heapq.heappop(people_heap)
        t_size = heapq.heappop(tshirts_heap)
        if p_size <= t_size:
            count += 1
            continue
        if p_size > t_size:
            heapq.heappush(people_heap, p_size)
    print(count)
    return count


solution([2, 3], [1, 2, 3])
solution([1, 2, 3], [1, 1, 1, 1])

"""
people = 2 ~ 5000
tshirts = 2 ~ 5000

각 원소 크기는 1 ~ 1000
"""
