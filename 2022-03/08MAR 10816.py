import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
n_arr = list(input().split())
n_dict = {}
for n in n_arr:
    n_dict[n] = n_dict.get(n, 0) + 1

m = int(input())
m_arr = list(input().split())
for m in m_arr:
    print(n_dict.get(m, 0), end=' ')
