import sys
from itertools import permutations, product

input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for i in range(1, n + 1):
    arr.append(i)
result = [arr] * m
for i in product(*result):
    print(*i)
