import sys
from collections import deque

input = sys.stdin.readline

t = int(input())
board = list(map(int, input().split()))

answer = -1
curr_idx = 0
jump = 0
queue = deque()
queue.append((curr_idx, jump))
visited = []

while queue:
    curr_idx, jump = queue.popleft()
    if curr_idx == len(board) - 1:
        print(jump)
        exit()

    # if curr_idx not in visited:
    for i in range(1, board[curr_idx] + 1):
        queue.append((curr_idx + i, jump + 1))
print(curr_idx, jump)
print(-1)






"""
10
1 2 0 1 3 2 1 5 4 2
"""