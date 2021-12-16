import heapq
import sys
heap = []
for _ in range(int(sys.stdin.readline())):
    m = int(sys.stdin.readline())
    heapq.heappush(heap, (-m, m))
while heap:
    a, b = heapq.heappop(heap)
    print(b)
