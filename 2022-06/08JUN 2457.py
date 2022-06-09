import sys
from collections import deque
from itertools import chain

input = sys.stdin.readline

N = int(input())
board  =[]
for _ in range(N):
    a, b, c, d = map(int, input().split())
    board.append(([a, b], [c, d]))
board.sort()
print(board)


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
