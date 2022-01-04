# from sys import stdin
# from collections import deque
# import heapq
#
# read = stdin.readline
#
# N = int(read())
# queue = deque()
# heap = []
# result = []
# for _ in range(N):
#     a, b = map(int, read().split())
#     result.append((a, b))
# result.sort()  # time 정렬상태
# heapq.heappush(heap, result[0][1])  # 첫번째 수업 끝나는 시간부터 들어가 있다.
#
# for i in range(1, N):
#     if heap[0] > result[i][0]:
#         heapq.heappush(heap, result[i][1])
#         # 못들어가.
#     else:  # 들어갈 수 있어
#         heapq.heappop(heap)
#         heapq.heappush(heap, result[i][1])
#
# print(len(heap))
#
# # time 을 힙으로 바꾸면, 최소 힙으로 가장 빠른게 먼저 나온다.
# # 하나를 팝해서 끝시간을 어디에 박아두면, 힙의 0번째 인덱스와 비교할 수 있다.


from sys import stdin
import heapq

read = stdin.readline

N = int(read())
heap = []
result = []

for _ in range(N):
    a, b = map(int, read().split())
    heapq.heappush(heap, (a, b))
start, end = heapq.heappop(heap)
result.append([end])


for i in range(1, N):
    if result[i][-1] <= heap[0][0]:
        result[i].append(heap[0][1])
        heapq.heappop(heap)
        break
    else:
        result.append([heap[0][1]])
        heapq.heappop(heap)

print(len(result))