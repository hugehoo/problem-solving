import sys
from bisect import bisect_left

input = sys.stdin.readline
TC = int(input().strip())

while TC > 0:
    result = 0
    _, _ = map(int, input().split())
    a_list = list(map(int, input().split()))
    b_list = sorted(list(map(int, input().split())))
    
    for a in a_list:
        result += bisect_left(b_list, a)
    print(result)
    TC -= 1
