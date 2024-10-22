from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    numbers = list(map(int, input().rstrip()))
    N = len(numbers)
    dp = [0] * (N + 1)
    if numbers[0] == 0:
        print(0)
    else:
        numbers = [0] + numbers
        dp[0] = dp[1] = 1
        for i in range(2, N + 1):
            if numbers[i] != 0:
                dp[i] += dp[i - 1]
            concat_number = numbers[i - 1] * 10 + numbers[i]
            if 10 <= concat_number <= 26:
                dp[i] += dp[i - 2]
        print(dp)

"""
25114
1 ~ 26
25 : 2 가지
11 : 2 가지
14 : 2 가지

25 11 4
25 1 1 4
25 1 14
2 5 1 1 4
2 5 11 4
2 5 1 14


"""
