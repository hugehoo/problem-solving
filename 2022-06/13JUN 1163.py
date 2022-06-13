import sys

input = sys.stdin.readline

N = int(input())
d = 2

while d <= N:
    if N % d == 0:
        print(d)
        N = N / d
    else:
        d = d + 1
