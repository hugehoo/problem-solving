import heapq
from sys import stdin

N = int(stdin.readline())
heap = []
for _ in range(N):
    a = int(stdin.readline())
    if a == 0 and not heap:
        print(0)
        continue
    if a == 0:
        pop = heapq.heappop(heap)
        print(pop[1])
    else:
        heapq.heappush(heap, (-a, a))



"""
13
0
1
2
0
0
3
2
1
0
0
0
0
0
"""