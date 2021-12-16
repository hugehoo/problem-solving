# import heapq
# heap = []
# for _ in range(int(sys.stdin.readline())):
#     m = int(sys.stdin.readline())
#     heapq.heappush(heap, (-m, m))
# while heap:
#     a, b = heapq.heappop(heap)
#     print(b)

import sys

N = int(sys.stdin.readline())
number_dict = {}
for _ in range(N):
    n = int(sys.stdin.readline())
    number_dict[n] = number_dict.get(n, 0) + 1

for i in range(1, 10001):
    m = number_dict.get(i, 0)

    for _ in range(m):
        print(i)



