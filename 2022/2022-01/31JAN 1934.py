from math import gcd


N = int(input())


for _ in range(N):
    a, b = map(int, input().split())
    print((a * b) // gcd(a, b))


# 시간초과
# def lcm(n, m):
#     for i in range(max(n, m), (n * m) + 1):
#         if i % n == 0 and i % m == 0:
#             return i
#
#
# for _ in range(N):
#     a, b = map(int, input().split())
#     print(lcm(a, b))

"""
3
1 45000
6 10
13 17
"""
