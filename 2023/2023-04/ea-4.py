# def solution(board):
#     # 1방향 O -> 이동.
#     # 2방향 O -> 이동.
#     # 각 점마다 생성할 수 있는 다이아몬드 케이스를 만들어.
#
#     return
#
# def diamonds(r, c):
#     n = 1
#
#     while True:
#
#
#
#
# print(solution([[0, 0, 1, 0, 0],
#                 [0, 0, 1, 0, 0],
#                 [0, 0, 1, 0, 0],
#                 [0, 0, 1, 0, 0],
#                 [0, 0, 1, 0, 0]]))
#
# print(solution([
#     [0, 0, 0, 1, 0, 0, 0],
#     [0, 0, 1, 0, 1, 1, 0],
#     [0, 1, 0, 1, 0, 0, 1],
#     [1, 0, 0, 0, 1, 1, 0],
#     [0, 1, 0, 1, 0, 1, 0],
#     [1, 0, 1, 0, 0, 0, 1],
#     [0, 1, 0, 1, 0, 1, 0]
# ]))
arr = [[0, 0, 1, 0, 0],
       [0, 1, 0, 1, 0],
       [1, 0, 1, 0, 1],
       [0, 1, 0, 1, 0],
       [0, 0, 1, 0, 0]]

from typing import List

def count_diamonds(arr: List[List[int]]) -> int:
    n = len(arr)
    cnt = 0
    for i in range(1, n-1):
        for j in range(1, n-1):
            if arr[i][j] == 1:
                for k in range(1, n-j):
                    if arr[i-k][j] and arr[i][j-k] and arr[i+k][j] and arr[i][j+k]:
                        cnt += 1
                    else:
                        break
    return cnt


print(count_diamonds(arr))

# print(find_diamond([[0, 0, 1, 0, 0],
#                     [0, 1, 0, 1, 0],
#                     [1, 0, 1, 0, 1],
#                     [0, 1, 0, 1, 0],
#                     [0, 0, 1, 0, 0]]))
