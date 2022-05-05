import sys

input = sys.stdin.readline

first = list(input().strip())
second = list(input().strip())
third = list(input().strip())

x = len(first)
y = len(second)
z = len(third)

board = [[[0] * (x + 1) for _ in range(y + 1)] for _ in range(z + 1)]

for i in range(1, z + 1):
    for j in range(1, y + 1):
        for k in range(1, x + 1):
            if first[k - 1] == second[j - 1] and second[j - 1] == third[i - 1]:
                board[i][j][k] = board[i - 1][j - 1][k - 1] + 1
            else:
                board[i][j][k] = max(board[i - 1][j][k], board[i][j - 1][k], board[i][j][k - 1])
answer = -1
for i in range(z + 1):
    for j in range(y + 1):
        answer = max(max(board[i][j]), answer)
print(answer)

# for b in board:
#     for a in b:
#         print(a)
#     print(' ')
#