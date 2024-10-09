from sys import stdin
from collections import defaultdict

input = stdin.readline


def recursive(n: int):
    if dp[n] != 0:
        return dp[n]
    dp[n] = recursive(n // P) + recursive(n // Q)
    return dp[n]


if __name__ == '__main__':
    N, P, Q = map(int, input().split())
    if N == 0:
        print(1)
        exit(0)
    dp = defaultdict(int)
    dp[0] = 1
    print(recursive(N))
