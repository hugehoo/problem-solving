import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque(enumerate(map(int, input().split())))
ans = []

while q:
    idx, paper = q.popleft()
    ans.append((idx + 1))
    if paper > 0:
        q.rotate(-(paper - 1))
    else:
        q.rotate(-paper)
print(' '.join(map(str, ans)))
"""
5
3 2 1 -3 -1
"""