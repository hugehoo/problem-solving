N = int(input())
arr = list(map(int, input().split()))

dp = [0] * N
dp[0] = 1

for i in range(1, N):
    for j in range(i):
        if not dp[j]:
            continue
        if j + arr[j] >= i:
            dp[i] = dp[j] + 1
print(max(dp) - 1)

"""
5
2 3 0 1 4

7
2 0 0 0 1 2 3
"""
