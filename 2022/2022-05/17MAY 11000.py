import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
arr = sorted(arr, key=lambda x: (x[0], x[1],))
print(arr)
queue = deque(arr)
answer = []
while queue:
    pops = queue.popleft()
    if len(answer) == 0:
        answer.append(pops)
        continue
    for i in range(len(answer)):
        if answer[i][1] <= pops[0]:


"""
3
1 3
2 4
3 5
"""
