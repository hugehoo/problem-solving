import sys

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# for _ in range(M):
#     a, b = map(int, sys.stdin.readline().split())
#     print(sum(arr[a - 1: b]))

accumulate = [0]
for i in range(N):
    accumulate.append(accumulate[i] + arr[i])

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    print(accumulate[b] - accumulate[a - 1])

"""
5 3
5 4 3 2 1
1 3
2 4
5 5
"""


