from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N = int(input().rstrip())
    dp = [0] * (N + 1)
    dp[1] = 0
    dp[2] = 3
    dp[3] = 0
    # dp[4] = 9 + 2
    for i in range(4, N):
        if i % 2 == 0:
            dp[i] = dp[i - 2] * 3 + 2
    print(dp)
    
    
    
