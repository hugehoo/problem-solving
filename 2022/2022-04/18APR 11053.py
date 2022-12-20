import sys

input = sys.stdin.readline

N = int(input())

arr = list(map(int, input().strip().split(" ")))
dp = [1] * N

for i in range(N):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))



"""
# wrong
cache = [1] * len(arr)
for idx in range(len(arr)):
    if arr[idx - 1] < arr[idx]:
        cache[idx] = cache[idx - 1] + 1
    else:
        cache[idx] = cache[idx - 1]
"""
