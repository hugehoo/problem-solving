import sys

# from sys import stdin
# from collections import defaultdict
#
# read = stdin.readline
# N = int(read())
# dict_list = defaultdict(list)
#
# while True:
#     a, b = map(int, read().split())
#     if a == -1:
#         break
#     dict_list[a].append(b)
#     dict_list[b].append(a)
#
# new_dict = dict()
# _max = -1
# for k, v in dict_list.items():
#     m = len(dict_list[k])
#     new_dict[k] = m
#     if m > _max:
#         _max = m
# result = []
# for k, v in new_dict.items():
#     if v == _max:
#         result.append(k)
# score = N - 1
# final_score = score - _max + 1
#
# print(final_score, len(result))
# print(*result)

# if __name__ == "__main__":
#     n = int(sys.stdin.readline())
#     graph = [[float('inf') for _ in range(n + 1)] for _ in range(n + 1)]
#
#     for i in range(1, n + 1):
#         graph[i][i] = 0
#
#     while True:
#         a, b = map(int, sys.stdin.readline().split())
#         if a == -1 and b == -1:
#             break
#         else:
#             graph[a][b] = 1
#             graph[b][a] = 1
#
#     for k in range(1, n + 1):
#         for i in range(1, n + 1):
#             for j in range(1, n + 1):
#                 graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
#
#     # 회장 후보 점수 찾기
#     min_score = float('inf')
#     for i in range(1, n + 1):
#         min_score = min(min_score, max(graph[i][1:]))
#
# print('min', min_score)
# for g in graph:
#     print(g)

"""
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1
"""

import copy


inf = float('inf')
arr = [
    [0, 5, inf, 8],
    [7, 0, 9, inf],
    [2, inf, 0, 4],
    [inf, inf, 3, 0]
]
N = 4


def floydWarshall():
    # temp = [[0] * (N) for _ in range(N)]

    # for i in range(N):
    #     for j in range(N):
    #         temp[i][j] = arr[i][j]
    temp = copy.deepcopy(arr)
    print('1')
    for i in temp:
        print(i)

    print(' ')

    for l in range(N):
        for m in range(N):
            for n in range(N):
                if temp[m][n] > temp[m][l] + temp[l][n]:
                    temp[m][n] = temp[m][l] + temp[l][n]
    for i in (temp):
        print(i)


floydWarshall()



