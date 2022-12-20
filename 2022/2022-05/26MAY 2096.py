import sys
from copy import deepcopy

input = sys.stdin.readline

M = int(input())
_list = list(map(int, input().split()))

max_board = [deepcopy(_list), [0, 0, 0]]
min_board = [deepcopy(_list), [0, 0, 0]]

for m in range(M - 1):
    _list = list(map(int, input().split()))
    max_board[1][0] = max(max_board[0][0], max_board[0][1]) + _list[0]
    max_board[1][1] = max(max_board[0][0], max_board[0][1], max_board[0][2]) + _list[1]
    max_board[1][2] = max(max_board[0][1], max_board[0][2]) + _list[2]
    max_board[1], max_board[0] = max_board[0], max_board[1]

    min_board[1][0] = min(min_board[0][0], min_board[0][1]) + _list[0]
    min_board[1][1] = min(min_board[0][0], min_board[0][1], min_board[0][2]) + _list[1]
    min_board[1][2] = min(min_board[0][1], min_board[0][2]) + _list[2]
    min_board[1], min_board[0] = min_board[0], min_board[1]

print(max(max_board[0]), min(min_board[0]))

"""
위 아래 컬럼 두개를 만들어야 한다.
2 x 3 배열을 만들고, 때가 되면 위아래를 스왑? 
"""
