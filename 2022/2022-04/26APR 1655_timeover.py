import sys
from heapq import heappop, heappush, heapify

input = sys.stdin.readline

n = int(input())
heap = []
for _ in range(n):
    number = int(input())
    heappush(heap, (-number, number))
    rounds = len(heap) // 2
    temp = []
    if rounds == 0:
        print(heap[0][1])
        continue

    for i in range(rounds):
        temp.append(heappop(heap))
    pops = heappop(heap)
    print(pops[1])
    heappush(heap, pops)

    heap += temp
    heapify(heap)

"""
7
1
5
2
10
-99
7
5
"""
