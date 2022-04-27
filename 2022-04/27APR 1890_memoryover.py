import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))
queue = deque()
queue.append([0, 0])
count = 0
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
# while queue:
#     r, c = queue.popleft()
#     if r == c == n - 1:
#         count += 1
#         continue
#     i = board[r][c]
#     if i == 0:
#         continue
#     if (r + i) < n:
#         queue.append([r + i, c])
#         dp[r + i][c] += 1
#     if (c + i) < n:
#         queue.append([r, c + i])
#         dp[r][c + i] += 1

# print(dp)
# print(dp[n - 1][n - 1])

for r in range(n):
    for c in range(n):
        # if r == 0 and c == 0:
        #     dp[r][c] = 1
        if r == n - 1 and c == n - 1:
            print('a ', dp[r][c])
        if dp[r][c] != 0:
            i = board[r][c]
            # if i == 0:
            #     continue
            if (r + i) < n:
                dp[r + i][c] += 1
            if (c + i) < n:
                dp[r][c + i] += 1

print(dp)
print(dp[n - 1][n - 1])
