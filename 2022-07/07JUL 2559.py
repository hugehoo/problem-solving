import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline
n, m = map(int, input().split())

arr = list(map(int, input().split()))  # arr 의 길이 100_000
max_v = sum(arr[0: 0 + m])
if m == 1:
    print(max(arr))
    exit()
elif n == m:
    print(sum(arr))
    exit()

for i in range(len(arr) - m + 1):
    temp = arr[i: i + m]
    result = sum(temp + temp[::-1]) // 2
    max_v = max(max_v, result)  # slicing 은 결국 O(n)
print(max_v)
