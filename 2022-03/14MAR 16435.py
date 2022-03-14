import sys
import heapq


input = sys.stdin.readline

n, m, = map(int, input().split())

arr = list(map(int, input().split()))
heap = []
for a in arr:
    heapq.heappush(heap, a)
while heap:
    a = heapq.heappop(heap)
    if m >= a:
        m += 1
    else:
        print(m)
        exit()
print(m)




"""
3 10
10 11 13
"""