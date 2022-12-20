import sys
from heapq import heappop, heappush


input = sys.stdin.readline

N, M = map(int, input().split())
cards = list(map(int, input().split()))
hq = []
for c in cards:
    heappush(hq, c)
for _ in range(M):
    pop1 = heappop(hq)
    pop2 = heappop(hq)
    for _ in range(2):

        heappush(hq, pop1+pop2)
print(sum(hq))


"""
3 1
3 2 6
"""