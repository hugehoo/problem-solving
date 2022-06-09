import sys
from collections import deque
from itertools import chain

input = sys.stdin.readline

N = int(input())
before = [int(input()) for _ in range(N)]
after = []
pop = before.pop()
after.append(pop)
count = 0
for i in range(len(before) - 1, -1, -1):
    pop = before.pop()
    for j in range(len(after) - 1, -1, -1):
        if after[j] < pop:
            count += 1
        else:
            break
    after.append(pop)

print(count)

"""

10000 * 10000
 
6
10
3
7
4
12
2

6
12
5
7
4
8
1
"""
