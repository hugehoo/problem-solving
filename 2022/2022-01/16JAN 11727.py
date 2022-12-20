N = int(input())

# 배열을 쓸 필요가 없구나
# dp = [0, 0, 0, 0] * N
# dp[1] = 1
# dp[2] = 3
# dp[3] = 5
# for i in range(4, N + 1):
#     dp[i] = (dp[i - 1] + 2 * dp[i - 2]) % 10007
# print(dp[N])

a = 1
b = 3
for _ in range(N - 1):
    a = b
    b = 2 * a + b
print(b)
print(a % 10007)

