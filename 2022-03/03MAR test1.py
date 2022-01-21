import heapq


def solution(scoville, K):
    count = 0
    heap = []

    for s in scoville:
        heapq.heappush(heap, s)

    while True:
        if len(heap) == 1 and heap[0] < K:
            return -1

        mini = heapq.heappop(heap)
        if mini >= K:
            break
        mini2 = heapq.heappop(heap)
        heapq.heappush(heap, mini + (mini2 * 2))
        count += 1
    return count


solution([1, 2, 3, 9, 10, 12], 7)
