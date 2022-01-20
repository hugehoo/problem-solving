N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N
dp[0] = arr[0]
for i in range(1, N):
    dp[i] = max(dp[i - 1] + arr[i], arr[i])
print(max(dp))

"""
5
-1 -2 -3 -4 -5

10
2 1 -4 3 4 -4 6 5 -5 1
"""
