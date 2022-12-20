import sys
from collections import defaultdict, deque


read = sys.stdin.readline
N = int(read())  # 노드 수
queue = deque()
graph_dict = defaultdict(set)
board = [list(map(int, read().split())) for _ in range(N)]

for idx, b in enumerate(board):
    for jdx, each_b in enumerate(b):
        if each_b == 1:
            graph_dict[idx + 1].add(jdx + 1)

for i in range(1, N + 1):
    visited = []
    queue = deque(graph_dict[i])
    while queue:
        pops = queue.popleft()
        for j in graph_dict[pops]:
            if j not in visited:
                queue.append(j)
                visited.append(j)
    for v in visited:
        board[i - 1][v - 1] = 1

for b in board:
    print(*b)
"""
1 : 4
2:  7
4 : 5 6 
5 : 1
6 : 7
7 : 3

7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0
"""
