from itertools import permutations, combinations_with_replacement
import sys

input = sys.stdin.readline


def solve():
    n, m, = map(int, input().split())
    arr = sorted(list(map(int, input().split())))
    temp = sorted(list(set(combinations_with_replacement(arr, m))))
    for i in temp:
        print(*i)

solve()

"""
3 1
4 5 2

4 2
9 8 7 1
"""
