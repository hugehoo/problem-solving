import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
q = []
for _ in range(N):
    temp = sorted(list(map(int, input().split())))
    heappush(q, temp)
# visited = [False] * 2_000_000_001

a, b = heappop(q)
min_v, max_v = a, b
answer = 0
while q:
    a, b = heappop(q)
    if max_v < a:
        answer += (max_v - min_v)
        min_v = a
        max_v = b
    if a <= max_v < b:
        max_v = b

answer += (max_v - min_v)
print(answer)

"""
5
1 3
2 5
3 5
6 7
8 9

5
1 9 
3 6
 4 10
5 20
2 21
"""