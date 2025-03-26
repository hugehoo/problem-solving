from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    num = int(input().rstrip())
    dp = [float('inf')] * (num + 1)
    dp[num] = 0
    current_num = num
    for n in range(num - 1, 0, -1):
        if current_num // 3 == n or current_num // 2 == n or current_num - 1 == n:
            print('c', n)
            dp[n] = min(dp[current_num] + 1, dp[n])
            current_num = n
    print(dp)
    # while num != 1:
    #     prev_dp = dp[num]
    #     if num % 3 == 0:
    #         num = num // 3
    #         dp[num] = min(dp[num], prev_dp + 1)
    #     elif num % 2 == 0:
    #         num = num // 2
    #         dp[num] = min(dp[num], prev_dp + 1)
    #     else:
    #         num -= 1
    #         print(num)
    #         dp[num] = min(dp[num], prev_dp + 1)
    # print(dp)

"""
3으로 나누거나
2로 나누거나
1을 뺀다.

1을 만들어라.
"""
