import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input())

"""
0 -> 1
1 -> 10
배열 2개
  0 1 2 3 4 5 6 7 
A 1 0 1 1 2 3 5 8 13 21 34
B 0 1 1 2 3 5 8 13
"""
string_N = str(N)
l = sorted(string_N, reverse=True)
temp = sorted(set(p for p in permutations(string_N, len(string_N))))
answer = temp.index(tuple(string_N))
if answer < len(temp) -1:
    print(''.join(temp[answer + 1]))
else:
    print(0)

