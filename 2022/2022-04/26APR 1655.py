import sys
from heapq import heappop, heappush

input = sys.stdin.readline

n = int(input())
left_heap = []
right_heap = []
for _ in range(n):
    now = int(input())
    if len(left_heap) == len(right_heap):
        heappush(left_heap, [-now, now])
    else:
        heappush(right_heap, [now, now])
    if right_heap and left_heap[0][1] >= right_heap[0][1]:
        right_pops = heappop(right_heap)
        left_pops = heappop(left_heap)
        heappush(left_heap, [-right_pops[1], right_pops[1]])
        heappush(right_heap, [left_pops[1], left_pops[1]])
    print(left_heap[0][1])

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
