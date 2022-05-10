import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(input().strip()))

for b in board:
    print(b)
start_ = [0, 0]
start_right = [0, 7]
end_ = [7, 0]
end_right = [7, 7]
for r in range(n - 7):
    for c in range(m - 7):
        print(board[r][c])
        print(board[r][c+7])
        print(board[r+7][c])
        print(board[r+7][c+7])

"""
어떻게 wbwb 를 체크할지
"""