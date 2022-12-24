
from itertools import permutations

N, M = map(int, input().split())
arr = list(map(int, input().split()))

# 1
# res = []
# for j in permutations(arr, M):
#     if sorted(j) == list(j):
#         res.append(list(j))
#
# for s in (sorted(res)):
#     print(*s)

# 2
arr.sort()
result = []


def dfs(start):
    if len(result) == M:
        print(' '.join(map(str, result)))
        return
    for i in range(start, N):
        result.append(arr[i])
        dfs(i + 1)
        result.pop()


start_idx = 0
dfs(start_idx)
"""
4 2
9 8 7 1
"""