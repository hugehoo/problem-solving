from itertools import permutations


N, M, = map(int, input().split())
result = [str(i) for i in range(1, N + 1)]
arr = list(permutations(result, M))
for ar in arr:
    print(' '.join(list(ar)))

"""
4 2
"""