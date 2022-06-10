import sys

input = sys.stdin.readline

N = int(input())
board = []
start = 301
count, max_date, flag = 0, 0, 0

for _ in range(N):
    a, b, c, d = map(int, input().split())
    board.append([a * 100 + b, c * 100 + d])
board.sort()

for i in range(N):
    if start > 1130:
        break
    if board[i][0] <= start < board[i][1]:
        if flag != start:
            flag = start
            count += 1
        if max_date < board[i][1]:
            max_date = board[i][1]
    else:
        if flag == start:
            if board[i][0] <= max_date < board[i][1]:
                start = max_date
                flag = start
                max_date = board[i][1]
                count += 1
        else:
            if start < board[i][0]:
                count = 0
                break
if max_date <= 1130:
    count = 0
print(count)

"""
10 만개를 어케 소팅하노

10
2 15 3 23
4 12 6 5
5 2 5 31
9 14 12 24
6 15 9 3
6 3 6 15
2 28 4 25
6 15 9 27
10 5 12 31
7 14 9 1
"""
