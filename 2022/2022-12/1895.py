"""
6 5
49 36 73 62 21
27 88 14 11 12
99 18 36 91 21
45 96 72 12 10
12 48 49 75 56
12 15 48 86 78
40
"""

R, C = map(int, input().split())
board = [list(map(int, input().split())) for r in range(R)]
T = int(input())


def get_median(arr: list):
    arr.sort()
    return arr[4]


moveC = C - 2
moveR = R - 2
result = []
for mr in range(moveR):
    for mc in range(moveC):
        result.append(get_median(board[mr][mc: mc + 3] + board[mr + 1][mc: mc + 3] + board[mr + 2][mc: mc + 3]))
print(len(list(filter(lambda x: x >= T, result))))
