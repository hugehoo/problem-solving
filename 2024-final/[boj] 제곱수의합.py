from sys import stdin


def min_square_sum(N):
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    
    for i in range(1, N + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    return dp[N]


print(min_square_sum(int(stdin.readline())))
"""
1인 경우를 체커로 잡자.

"""

"""
13 = 9 + 4
규칙으로 조지면 될 듯.
1: 1
2: 2
3: 3
4: 1
5: 2
6: 3
7: 4
8: 2
9: 1
10: 2
11: 3
12: 3 / 2**2, 2**2, 2**2
13: 2
14: 3
15: 4
16: 1
17: 2
"""
