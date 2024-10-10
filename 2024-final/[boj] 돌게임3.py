from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N = int(input())
    if N == 1:
        print("SK")
        exit(0)
    if N == 2:
        print("CY")
        exit(0)
    if N < 5:
        print("SK")
        exit(0)
    
    dp = [0] * (N + 1)
    dp[1], dp[3], dp[4] = "SK", "SK", "SK"
    dp[2] = "CY"
    
    for i in range(5, len(dp)):
        if dp[i - 1] == "CY" or dp[i - 3] == "CY" or dp[i - 4] == "CY":
            dp[i] = "SK"
        else:
            dp[i] = "CY"
    print(dp[N])

"""
1. SK, CY
마지막 턴에 1,3,4 가 남는 경우.
1, 3, 4

1 s
2 c
3 s
4 c
5 s
6
7
8
9
10
"""
