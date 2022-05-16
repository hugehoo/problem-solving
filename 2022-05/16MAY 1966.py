import sys
from collections import deque


input = sys.stdin.readline

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    c = list(map(int, input().split()))
    queue = deque()
    count = 0
    for i in range(len(c)):
        if i == b:
            queue.append([c[i], 0])
            continue
        queue.append([c[i]])

    if len(c) == 1:
        print(1)
        continue

    while True:
        pops = queue.popleft()
        if pops[0] < sum(max(queue)):
            queue.append(pops)
        elif pops[0] == sum(max(queue)):
            if len(pops) == 2:
                count += 1
                print(count)
                break
            else:
                count += 1
        else:
            if len(pops) == 2:
                count += 1
                print(count)
                break
            count += 1



"""
3
1 0
5
4 2
1 2 3 4
6 0
1 1 9 1 1 1
"""
