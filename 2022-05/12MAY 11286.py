import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
hq = []
for _ in range(n):
    m = int(input())
    if m != 0:
        heappush(hq, [abs(m), m])
        continue
    if hq:
        pop = heappop(hq)
        print(pop[1])
        continue
    print(0)
