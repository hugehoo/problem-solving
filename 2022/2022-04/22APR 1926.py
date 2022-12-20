import sys
from collections import deque

input = sys.stdin.readline

board = []
r, c = map(int, input().split())

for _ in range(r):
    board.append(list(map(int, input().split())))

mx = [1, -1, 0, 0]
my = [0, 0, 1, -1]

visited = []
queue = deque()
sum_ = 0
max_sum = 0
cnt = 0
num_list = []
for r_ in range(r):
    for c_ in range(c):
        if board[r_][c_] == 1: # and (r_, c_) not in visited:
            board[r_][c_] = 0
            # visited.append((r_, c_))
            sum_ = 0
            queue.append((r_, c_))
            area = 1
            while queue:
                pops = queue.popleft()
                for i in range(4):
                    ny = pops[0] + my[i]
                    nx = pops[1] + mx[i]

                    if ny < 0 or ny >= r or nx < 0 or nx >= c:
                        continue
                    if board[ny][nx] == 1: # and (ny, nx) not in visited:
                        queue.append((ny, nx))
                        # visited.append((ny, nx))
                        board[ny][nx] = 0
                        sum_ += 1
                        area += 1
            num_list.append(area)
            # max_sum = max(sum_, max_sum)
            # cnt += 1
# print(cnt)
# print(max_sum)
if len(num_list):
    # print(num_list)
    print(len(num_list))
    print(max(num_list))
else:
    print(len(num_list))
    print(0)