from sys import stdin

read = stdin.readline
N, M = map(int, read().split())


def solution(n, m):
    m += 1
    result = [True] * m
    for i in range(2, int(m ** 0.5) + 1):
        for j in range(2 * i, m, i):
            result[j] = False

    for i in range(n, m + 1):
        if result[i]:
            print(i)


solution(N, M)
# 에라토스테네스의 체: 포스팅

"""
5
12 7 9 15 5
13 8 11 19 6
21 10 26 31 16
48 14 28 35 25
52 20 32 41 49
"""
