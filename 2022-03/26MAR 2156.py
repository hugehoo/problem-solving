import sys

input = sys.stdin.readline

n = int(input())
wine = [0] * 10000
for i in range(n):
    wine[i] = int(input())
dp = [0] * 10000
dp[0] = wine[0]
dp[1] = wine[0] + wine[1]
dp[2] = max(wine[0] + wine[2], wine[1] + wine[2], dp[1])
for i in range(3, n):
    dp[i] = max(dp[i - 2] + wine[i], dp[i - 3] + wine[i - 1] + wine[i], dp[i - 1])

# 경우에 따라 분류하는 것이 포인트네.

print(max(dp))

"""
dp 에서 인덱스 에러가 뜨면, n 이 1~3 에서 발생 하는 문제
"""