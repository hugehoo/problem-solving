from itertools import combinations

N, K, = map(int, input().split())
# n = [i for i in range(N)]
# c = len(list(combinations(n, K))) % 10007
# print(c)


# def bino_coef(n, k):
#     if n == k or k == 0:
#         return 1
#     return bino_coef(n - 1, k) + bino_coef(n - 1, k - 1)

def bino_coef(n, r):
    cache = [[0 for _ in range(r + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        cache[i][0] = 1
    for i in range(r + 1):
        cache[i][i] = 1

    for i in range(1, n + 1):
        for j in range(1, r + 1):
            cache[i][j] = cache[i - 1][j] + cache[i - 1][j - 1]

    return cache[n][r]


print(bino_coef(N, K) % 10007)
