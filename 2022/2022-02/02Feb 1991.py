from collections import deque, defaultdict


import sys

input = sys.stdin.readline


N = int(input())
tree = defaultdict(list)
for _ in range(N):
    root, l, r = map(str, input().split())
    tree[root] = [l, r]
print(tree)
start = "A"
queue = deque([start])
visited = []
while queue:
    pops = queue.popleft()
    visited.append(pops)
    _l, _r = tree[pops]


"""
7
A B C
B D .
C E F
E . .
F . G
D . .
G . .
"""