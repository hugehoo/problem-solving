from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N = int(input().rstrip())
    numbers = list(map(int, input().split()))
    dp = [[0] * N for _ in range(N)]
    for num in range(N):
        for start in range(N - num):
            end = num + start
            if start == end:
                dp[start][end] = 1
            elif numbers[start] == numbers[end]:
                if start + 1 == end or dp[start + 1][end - 1]:
                    dp[start][end] = 1
    
    for _ in range(int(input().rstrip())):
        start, end = map(int, input().split())
        print(dp[start - 1][end - 1])

"""
7
1 2 1 3 1 2 1
4
1 3
2 5
3 3
5 7
"""
