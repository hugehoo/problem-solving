N = int(input())
# dp = [0] * (N + 1)
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3
# dp[4] = 1
dp = [x for x in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, i):
        if i - j * j >= 0:
            if i == 12:
                print('dp[12] = ', dp[i], '  j = ', j)
            dp[i] = min(dp[i], dp[i - j * j] + 1)
        #     # if dp[i] > dp[i - j * j] + 1:
        #     dp[i] = dp[i - j * j] + 1
        # if sqr > i:
        #     break
        # if dp[i] > dp[i - sqr] + 1:
        #     dp[i] = dp[i - sqr] + 1

print(dp)
"""
12

[0, 1, 2, 3, 1, 2, 3, 4, 2, 1, 2, 3, 4]

"""
