import sys
from itertools import permutations
import heapq


input = sys.stdin.readline

n = int(input())
if n == 1:
    print(0)
    exit()

heap = []
dasom = 0
count = 0

for j in range(n):
    if j == 0:
        i = int(input())
        dasom = i
        # heapq.heappush(heap, (-i, i))  # 얘를 heap 에 넣으면 안됐네
        continue
    i = int(input())
    heapq.heappush(heap, (-i, i))
while heap:
    idx, val = heapq.heappop(heap)
    if val >= dasom:
        val -= 1
        dasom += 1
        count += 1
        heapq.heappush(heap, (-val, val))
    else:
        print(count)
        exit()

