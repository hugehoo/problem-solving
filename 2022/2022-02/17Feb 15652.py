import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline


def solve():
    n, m, = map(int, input().split())
    arr = [i for i in range(1, n + 1)]
    for i in combinations_with_replacement(arr, m):
        print(*i)


solve()

"""
4 2

1 1
1 2
1 3
1 4
2 2
2 3
2 4
3 3
3 4
4 4
"""
