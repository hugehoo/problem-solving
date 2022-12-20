from sys import stdin
from itertools import chain

read = stdin.readline

n, m, = map(int, read().split())
board = [list(map(int, read().strip())) for _ in range(n)]
# _max = 0  # -1 이면 결국 1이 되어 오답 (모두 0인 케이스)


def square(arr, a, b):
    if a + 1 < n and b + 1 < m:
        if arr[a][b] > 0 and arr[a][b + 1] > 0 and arr[a + 1][b] > 0 and arr[a + 1][b + 1] > 0:
            return True


for i in range(n):
    for j in range(m):
        if square(board, i, j):
            board[i + 1][j + 1] = min(board[i][j], board[i + 1][j], board[i][j + 1]) + 1
            # _max = max(_max, board[i + 1][j + 1]) # max 를 구하는 방식이 잘못된 것 같음

print(max(list(chain(*board))) ** 2)

"""
4 4
0100
0111
1110
0010

5 5
11111
11111
11011
11111
11111

4 4
1100
1110
1110
1110


6 6
111110
111110
111111
111111
111111
001111
"""
