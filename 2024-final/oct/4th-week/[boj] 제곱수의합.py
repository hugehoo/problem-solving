from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N = int(input().rstrip())
    dp = [float('inf')] * (N + 1)
    dp[0] = 0
    for i in range(1, N + 1):
        j = 1
        while j ** 2 <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j += 1
    print(dp[N])

"""
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18
1 2 3 1 2 3 4 2 1  2  3  4  2  3  4  1  2  2

1 4 9 16
"""
