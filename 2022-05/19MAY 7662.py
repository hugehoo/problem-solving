import sys
import heapq

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    M = int(input())
    hq = []
    for _ in range(M):
        order, value = map(str, input().strip().split())
        if order == "I":
            heapq.heappush(hq, int(value))
        if order == "D":
            if value == "1":
                if hq:
                    max_value = max(hq)
                    hq.remove(max_value)
            else:
                if hq:
                    heapq.heappop(hq)
    if hq:
        print(max(hq), min(hq))
    else:
        print("EMPTY")







"""
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
"""
