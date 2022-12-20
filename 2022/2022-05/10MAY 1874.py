import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
queue = deque(o for o in range(1, n + 1))
answer = []
while queue:
    for i in range(m - 1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
print("<", end='')
for i in range(len(answer) - 1):
    print("%d, " % answer[i], end='')
print(answer[-1], end='')
print(">")
"""
역시 단순하게 생각해야한다. 
"""
