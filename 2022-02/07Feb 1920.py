import bisect
import sys


input = sys.stdin.readline
N = int(input())
arr1 = list(map(int, input().split()))
arr1.sort()

M = int(input())
result = [0] * M
arr2 = list(map(int, input().split()))

for a in arr2:
    i = bisect.bisect_left(arr1, a)
    if i != len(arr1) and arr1[i] == a:
        print(1)
    else:
        print(0)



# N, M 의 범위가 크다.
# 이중 포문 에바
