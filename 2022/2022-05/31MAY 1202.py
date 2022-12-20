# import sys
# from heapq import heappop, heappush
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# jewelry = [list(map(int, input().split())) for _ in range(N)]
# jewelry = sorted(jewelry, key=lambda x: (x[1] / x[0], x[0]))
#
# answer = []
# hq = []
#
# for _ in range(M):
#     c = int(input())
#     heappush(hq, (-c, c))
#
# while hq:
#     pops = heappop(hq)
#     if jewelry and jewelry[-1][0] <= pops[1]:
#         res = jewelry.pop()
#         result = pops[1] - res[0]
#         answer.append(res)
# print(sum(list(map(lambda x: x[1], answer))))
#
# """
# 가방에 최대 한개의 보석
# """

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

answer = 0
N, K = map(int, sys.stdin.readline().rstrip().split())
gem = [list(map(int, input().split())) for _ in range(N)]
bag = [int(input()) for _ in range(K)]
gem.sort()
bag.sort()

Q = []
for i in bag:
    while gem and gem[0][0] <= i:
        heappush(Q, -heappop(gem)[1])
    if Q:
        answer -= heappop(Q)
print(answer)
