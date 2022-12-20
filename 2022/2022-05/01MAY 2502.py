import sys

input = sys.stdin.readline

n, m = map(int, input().split())
dp = [(0, 0)] * 31
dp[1] = (1, 0)
dp[2] = (0, 1)
for i in range(3, 31):
    dp[i] = (dp[i - 2][0] + dp[i - 1][0], dp[i - 2][1] + dp[i - 1][1])

a, b = dp[n]

x = 1
while True:
    if (m - a * x) / b == (m - a * x) // b:
        print(x)
        print((m - a * x) // b)
        break
    x += 1
