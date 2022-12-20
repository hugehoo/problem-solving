# N = int(input())
# arr = [int(input()) for _ in range(N)]
#
#
# def check_steps(steps, idx):
#     if len(steps) >= 2:
#         if abs(steps[-1] - idx) == abs(steps[-1] - steps[-2]):
#             return False
#         else:
#             return True
#     else:
#         return True
#
#
# dp = [[i, []] for i in arr]
# for idx, ele in enumerate(dp):
#
#     print(idx, ele[0], ele[1])
#     if check_steps(ele[1], idx):
#         ele[1].append(idx)
#
#
# # 더한다.
# print(dp)
#
# print(arr)


# n = int(input())
# s = [0 for i in range(301)]
# dp = [0 for i in range(301)]
# for i in range(n):
#     s[i] = int(input())
#
# dp[0] = s[0]
# dp[1] = s[0] + s[1]
# dp[2] = max(s[1] + s[2], s[0] + s[2])
# for i in range(3, n):
#     dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
# print(dp)
# print(dp[n - 1])


"""
6
10
20
15
25
10
20
"""

n = int(input())

s = [0 for _ in range(301)]
dp = [0 for _ in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[1] + s[0]
dp[2] = max(s[0] + s[2], s[1] + s[2])

for i in range(3, n + 1):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])