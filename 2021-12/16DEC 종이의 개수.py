from itertools import chain
from math import sqrt

# N = int(input())  # 1, 3, 9, 27, 81, 243, ...
board = []
# for _ in range(N):
#     board.append(list(map(int, input().split())))


def all_same(small_board):
    count = set()
    for i in chain(small_board):
        count.add(i)
        if len(count) > 1:
            return False
    return True


def recursive(paper, n):
    if n == 1 or all_same(paper):
        return

    for i in range(int(sqrt(n))):
        pass
    return recursive(paper, len(paper))

# recursive(board, len(board))

# 종이 길이가 1이 되면 더이상 재귀탈 필요 없다.
# or 종이의 모든 원소가 같으면 된다.


import sys
N = int(sys.stdin.readline())
print(N == 10)


"""
9
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
0 0 0 1 1 1 -1 -1 -1
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
1 1 1 0 0 0 0 0 0
0 1 -1 0 1 -1 0 1 -1
0 -1 1 0 1 -1 0 1 -1
0 1 -1 1 0 -1 0 1 -1
"""