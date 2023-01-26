# N = int(input())
#
# times = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
# result = [times[0][2]]
#
# for i, start, end in times[1:]:
#     for idx, r in enumerate(result):
#         if r <= start:
#             result[idx] = end
#             break
#     else:
#         result.append(end)
#
# print(len(result))

"""
N 은 10만 까지. 
result -> 마지막 보다 작다면, 다른 r 의 테일도 순회해야함. 들어갈 자리가 없으면 그제야 result.append([end]) 해야함. 

3
1 1 4
2 4 5
3 4 6

8
6 15 21
7 20 25
1 3 8
3 2 14
8 6 27
2 7 13
4 12 18
5 6 20

5
1 1 10
2 11 12
3 8 12
4 6 8
5 2 12
"""

import heapq

N = int(input())
times = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: x[1])
min_heap = []
count = 0
for i, start, end in times:
    while min_heap and min_heap[0] <= start:
        heapq.heappop(min_heap)
    heapq.heappush(min_heap, end)
    count = max(count, len(min_heap))

print(count)
