import sys

input = sys.stdin.readline
n = int(input())
arr = [int(input()) for _ in range(n)]

if n == 1:
    print(arr[0])
    exit()

dp = [0] * n
dp[0] = arr[0]
dp[1] = arr[1] + arr[0]
for i in range(2, n):
    dp[i] = max(arr[i - 1] + dp[i - 3] + arr[i], dp[i - 2] + arr[i], dp[i - 1])
print(max(dp))
# 1. 바로 이전 것과 더하기 <- 그러려면 얘는, 그 직전의 것과 더해선 안된다. arr[i] + arr[i - 1]
# 2. 두번째 이전 것과 더하기 : arr[i] + dp[i - 2]
# 3. dp 가 두번연속 더해진 것인지 어떻게 알지 -> dp[i - 2] + arr[i]
# 4. 현재 것은 스킵하고 이전걸 더하기 (중요) <- 내가 놓친 것.