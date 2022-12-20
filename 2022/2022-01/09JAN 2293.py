N, K = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(int(input()))

dp = [0] * (K + 1)
dp[0] = 1

for a in arr:
    for j in range(a, K + 1):
        dp[j] += dp[j - a]
print(dp[K])
