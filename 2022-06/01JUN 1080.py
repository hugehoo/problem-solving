import sys

input = sys.stdin.readline

N, M = map(int, input().split())

first = []
second = []


def flip(r, c):
    for i in range(r, r + 3):
        for j in range(c, c + 3):
            first[i][j] = 1 - first[i][j]


for _ in range(N):
    first.append(list(map(int, list(input().strip()))))
for i in first:
    print(i)
for _ in range(N):
    second.append(list(map(int, list(input().strip()))))
for i in second:
    print(i)
count = 0
for n in range(N - 2):
    for m in range(M - 2):
        if first[n][m] != second[n][m]:
            flip(n, m)
            count += 1
        else:
            pass
if first == second:
    print(count)
else:
    print("-1")


# def reverse(x, y):
#     for i in range(x, x + 3):
#         for j in range(y, y + 3):
#             A[i][j] = 1 - A[i][j]
#
#
# def check():
#     for i in range(N):
#         for j in range(M):
#             if A[i][j] != B[i][j]:
#                 return False
#
#     return True
#
#
# N, M = map(int, input().split())
#
# A = [list(map(int, list(input()))) for _ in range(N)]
# B = [list(map(int, list(input()))) for _ in range(N)]
# for a in A:
#     print(a)
# count = 0
#
# for i in range(N - 2):
#     for j in range(M - 2):
#         if A[i][j] != B[i][j]:
#             reverse(i, j)
#             count += 1
#
# if check():
#     print(count)
# else:
#     print("-1")
# #
# #
# # """
# # [0, 0, 0, 0]
# # [0, 0, 1, 0]
# # [0, 0, 0, 0]
# # """