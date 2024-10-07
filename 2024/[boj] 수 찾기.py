import sys

input = sys.stdin.readline
N = int(input().strip())
number_dict = {}
for n in list(map(int, input().split())):
    number_dict[n] = 1
    
M = int(input().strip())
for t in list(map(int, input().split())):
    if number_dict.get(t) != 1:
        print(0)
    else:
        print(1)

"""
5
4 1 5 2 3
5
1 3 7 9 5
"""
