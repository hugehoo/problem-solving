import sys
from heapq import heappop, heappush

input = sys.stdin.readline

N = int(input())
for _ in range(N):
    M = int(input())
    nominate = []
    minq = []
    maxq = []
    number_dict = {}

    for _ in range(M):
        order, value = map(str, input().strip().split())
        if order == "I":
            number_dict[value] = number_dict.get(value, 0) + 1
            heappush(minq, int(value))
            heappush(maxq, -int(value))

        if order == "D":
            if value == "1":
                if maxq:
                    pop = -heappop(maxq)
                    if number_dict.get(pop, 0) != 0:
                        number_dict[pop] -= 1
                    else:
                        print("1 ", maxq, minq, pop)
                        minq.remove(pop)
                # else: # maxq 가 비어도 minq 는 존재할 경우엔?

            else:
                if minq:
                    pop = heappop(minq)
                    if number_dict.get(pop, 0) != 0:
                        number_dict[pop] -= 1
                    else:
                        print("2 ", maxq, minq, pop)
                        maxq.remove(-pop)
        # print("min : ", minq)
        # print("max : ", maxq)
        # print(number_dict)
    if minq and maxq:
        print(-heappop(maxq), heappop(minq))
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
