import sys

input = sys.stdin.readline

N = int(input())

board = []
for _ in range(N):
    s, e = map(int, input().split())
    board.append([s, e])
board.sort()
temp = [board[0]]
for i in range(1, len(board)):
    if not temp:
        temp.append(board[i])
    s, e = board[i]
    curr_s, curr_e = temp[-1]
    if e < curr_e:
        temp.pop()
        temp.append([s, e])
    elif curr_e <= s:
        temp.append([s, e])
    elif e > curr_e:
        continue
# print(temp)
print(len(temp))

"""
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14


7
3 10
2 2
1 3
2 2
9 10
4 9
2 2

5
6 7
6 6
5 6
5 5
7 7

"""
