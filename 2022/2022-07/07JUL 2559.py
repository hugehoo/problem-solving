import sys
from collections import deque

input = sys.stdin.readline
n, k = map(int, input().split())

arr = list(map(int, input().split()))  # arr 의 길이 100_000
init_arr = deque()
for i in range(k):
    init_arr.append(arr[i])
init_sum = sum(init_arr)
result = init_sum
for i in range(k, len(arr)):
    pop = init_arr.popleft()
    init_sum -= pop
    new = arr[i]
    init_sum += new
    init_arr.append(new)

    result = max(result, init_sum)

print(result)
