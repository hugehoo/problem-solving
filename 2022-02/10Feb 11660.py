import heapq
from math import inf
import sys

input = sys.stdin.readline
arr = [int(input()) for _ in range(9)]
value = max(arr)
print(value)
print(arr.index(value) + 1)

# N, M = map(int, input().split())
# board = []
# for _ in range(N):
#     temp = []
#     for i in list(map(int, input().split())):
#         if len(temp) > 0:
#             temp.append(i + temp[-1])
#         else:
#             temp.append(i)
#     board.append(temp)
# print(board)

# board.append(list(map(int, input().split())))

# for _ in range(M):
#     x1, y1, x2, y2 = map(int, input().split())
#     total = 0
#     for y in range(x1 - 1, x2):
#         for x in range(y1 - 1, y2):
#             total += board[y][x]
#
#     print(total)

"""
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
"""
