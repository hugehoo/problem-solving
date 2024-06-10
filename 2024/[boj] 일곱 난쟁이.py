import sys
from itertools import combinations

input = sys.stdin.readline
result = sorted([int(input().rstrip()) for _ in range(9)])

for combi in combinations(result, 7):
    if sum(combi) == 100:
        for n in combi:
            print(n)
        break


