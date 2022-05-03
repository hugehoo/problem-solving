import sys

input = sys.stdin.readline

first = list(input().strip())
second = list(input().strip())

first = [0] + first
second = [0] + second
board = [[0] * (len(first)) for _ in range(len(second))]

for sec in range(1, len(second)):
    for fir in range(1, len(first)):
        if first[fir] == second[sec]:
            board[sec][fir] += (board[sec - 1][fir - 1] + 1)
        else:
            board[sec][fir] = max(board[sec - 1][fir], board[sec][fir - 1])
answer = 0
for b in board:
    answer = max(max(b), answer)
print(answer)