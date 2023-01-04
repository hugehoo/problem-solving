N = int(input())
arr = list(map(int, input().split()))
max_num = -1e9
dp = [[0] * N for _ in range(2)]
dp[0][0] = arr[0]
for i in range(1, N):
    dp[0][i] = max(dp[0][i - 1] + arr[i], arr[i])
    dp[1][i] = max(dp[0][i - 1], dp[1][i - 1] + arr[i])
    max_num = max(max_num, dp[0][i], dp[1][i])

print(max_num if N > 1 else arr[0])


# 얘는 증가 부분 수열이었네. 지금 풀려는 문제는 연속 증가 수열이고.
# dp = [0] * N
# dp[0] = arr[0]
# for i in range(1, N):
#     dp[i] = arr[i]
#     for j in range(i):
#         if arr[j] < arr[i]:
#             dp[i] = max(dp[i], dp[j] + arr[i])
#             print(dp)
# print(max(dp))
