from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N = int(input())
    if N == 1 or N == 3:
        print("SK")
        exit(0)
    if N == 2:
        print("CY")
        exit(0)
    
    dp = [0] * (N + 1)
    dp[1], dp[3] = "SK", "SK"
    dp[2] = "CY"
    for i in range(4, N + 1):
        if dp[i - 1] == "SK" or dp[i - 3] == "SK":
            dp[i] = "CY"
        else:
            dp[i] = "SK"
    print(dp[N])
