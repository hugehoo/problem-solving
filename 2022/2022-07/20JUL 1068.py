from collections import deque

N = int(input())
arr = list(map(int, input().split()))
D = int(input())
arr[D] = -2


def dfs(idx):
    arr[idx] = -2
    for jdx, a in enumerate(arr):
        if a == idx:
            dfs(jdx)


for i in range(N):
    if arr[i] != -2 and arr[i] != -1:
        dfs(i)
print(arr)

# board = [[0] * N for _ in range(N)]
#
# for idx, v in enumerate(arr):
#     if v == -1:
#         continue
#     board[v][idx] = 1
# for b in board:
#     print(b)
# del_list = []
# for idx, v in enumerate(board[D]):
#     if v == 1:
#         del_list.append(idx)
# print(del_list)
# while del_list:
#     node = del_list.pop()
#     for v in board[node]:
#         if v == 1:
#             del_list.append(node)


"""
1
2
0 0
-450 -250
-600 500
-600 1000

1
2
0 0
-1000 0
1000 0
2000 0

1
0
0 0
2000 0

1
0
0 0
1000 0
"""
