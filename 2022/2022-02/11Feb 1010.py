import sys
from math import factorial

input = sys.stdin.readline
N = int(input())

def solve(x, y):
    return int(factorial(y) / (factorial(x) * factorial(y - x)))

for _ in range(N):
    x, y = map(int, input().split())
    (solve(x, y))
