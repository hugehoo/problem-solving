import sys
import heapq

heap = []
N = int(sys.stdin.readline())
for _ in range(N):
    a = int(sys.stdin.readline())
    if a == 0:
        if not heap:
            print(0)
        else:
            pop = heapq.heappop(heap)
            print(pop)
    else:
        heapq.heappush(heap, a)


