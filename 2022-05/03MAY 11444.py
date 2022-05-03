import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

for _ in range(m + 1):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2 and y1 == y2:
        print(board[x1 - 1][y1 - 1])
        continue
    answer = 0
    for y in range(y1 - 1, y2 - 1 + 1):
        row = 0
        for x in range(x1 - 1, x2 - 1 + 1):
            row += board[x][y]
        answer += row
    print(answer)
