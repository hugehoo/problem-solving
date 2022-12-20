import sys

input = sys.stdin.readline

N = int(input())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
alpha_dict = {}
board = []
for i in range(52):
    board.append([float('inf')] * 52)
    board[i][i] = 0

for i in range(len(alphabets)):
    alpha_dict[alphabets[i]] = i
    alpha_dict[i] = alphabets[i]

for _ in range(N):
    start, mid, end, = input().strip().split(' ')
    board[alpha_dict[start]][alpha_dict[end]] = 1
# for b in board:
#     print(b)
for k in range(52):
    for a in range(52):
        for b in range(52):
            board[a][b] = min(board[a][b], board[a][k] + board[k][b])
answer = []
for r in range(52):
    for c in range(52):
        if board[r][c] != float('inf') and board[r][c] != 0:
            if alpha_dict[r] != alpha_dict[c]:
                answer.append([alpha_dict[r], '=>', alpha_dict[c]])
# for b in board:
#     print(b)
sorted_answer =sorted(answer, key=lambda x: (x[0], x[2]))
print(len(sorted_answer))
for sa in sorted_answer:
    print(' '.join(sa))




"""
9,
18,
27
"""
