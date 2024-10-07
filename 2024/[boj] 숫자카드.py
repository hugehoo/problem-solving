import sys

input = sys.stdin.readline

N = int(input())
n_dict = {}
for n in list(input().split()):
    n_dict[n] = n_dict.get(n, 0) + 1

M = int(input())
for m in list(input().split()):
    print(n_dict.get(m, 0), end=' ')
