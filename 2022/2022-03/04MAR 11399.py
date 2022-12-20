import sys
import heapq

input = sys.stdin.readline

numberStack = 0
heap = []
answer = []
n = int(input())

for h in list(map(int, input().split())):
    heapq.heappush(heap, h)

while heap:
    numberStack += heapq.heappop(heap)
    answer.append(numberStack)
print(sum(answer))

"""
N = 5 (1 <= N <= 1000)

5
3 1 4 3 2
"""