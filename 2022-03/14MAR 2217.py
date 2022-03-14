import sys
import heapq

input = sys.stdin.readline

n = int(input())
heap = []
for i in range(n):
    a = int(input())
    heapq.heappush(heap, (-a, a))


count = 0
arr = []
i = 1
while heap:
    pops = heapq.heappop(heap)
    arr.append(pops[1] * i)
    i += 1
print(arr, max(arr))
