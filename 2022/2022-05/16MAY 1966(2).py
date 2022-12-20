import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    queue = deque(list(map(int, input().split())))
    count = 0

    while queue:

        best = max(queue)
        front = queue.popleft()
        b -= 1
        if best == front:
            count += 1
            if b < 0:
                print(count)
                break

        else:
            queue.append(front)
            if b < 0:
                b = len(queue) - 1







"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""
