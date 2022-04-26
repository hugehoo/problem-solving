import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
heap = []
# print(heap[0])
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
    # print(heappop(heap), temp, heap)
    pops = heappop(heap)
    print(pops[1])
    heappush(heap, pops)
    # print(heappop(heap))
    # heappop(heap) 프린트 한 것도 다시 넣어줘야지.

    for t in temp:
        heappush(heap, t)

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
