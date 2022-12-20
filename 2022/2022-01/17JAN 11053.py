import sys
import heapq

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
dp = [1] * N
for i in range(N):
    for j in range(i + 1):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))
# 증가하는걸 어케 표현하지.
"""
arr를 절반으로 나눈 후 dp 배열을 업데이트하면?


가장 긴 증가하는 수열
6
10 20 10 30 20 50
"""
