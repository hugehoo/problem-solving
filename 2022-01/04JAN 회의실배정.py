from sys import stdin
from collections import deque
import heapq

read = stdin.readline

N = int(read())
queue = deque()
heap = []
result = []
for _ in range(N):
    a, b = map(int, read().split())
    result.append((a, b))
result.sort() # time 정렬상태
heapq.heappush(heap, result[0][1]) # 첫번째 수업 끝나는 시간부터 들어가 있다.

for i in range(1, N):
    if heap[0] > result[i][0]:
        heapq.heappush(heap, result[i][1])
        # 못들어가.
    else: # 들어갈 수 있어
        heapq.heappop(heap)
        heapq.heappush(heap, result[i][1])

print(len(heap))

# while heap:
#     pops = heapq.heappop(heap)
#     for i in range(len(result)):
#         if result[i][-1] > pops[0]:
#             continue
#         else:
#             result[i].append(pops[1])
#             break
#     else:
#         result.append([pops[1]])

"""
"""

# time 을 힙으로 바꾸면, 최소 힙으로 가장 빠른게 먼저 나온다.
# 하나를 팝해서 끝시간을 어디에 박아두면, 힙의 0번째 인덱스와 비교할 수 있다.

"""
0 ~ 6, 6 ~ 10, 12 ~ 14
1 ~ 4, 5 ~ 7, 8 ~ 11, 12 ~ 14
2 ~ 13, 
3 ~ 5, 5 ~ 9
3 ~ 8 , 8 ~ 12
"""
