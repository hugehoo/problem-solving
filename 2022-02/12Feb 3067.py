import sys

input = sys.stdin.readline
for _ in range(int(input())):
    n = int(input())
    coins = map(int, input().split())
    target = int(input())
    dp = [1] + target * [0]
    for coin in coins:
        for j in range(coin, target + 1):
            dp[j] += dp[j - coin]
    print(dp[target])

"""
3
2
1 2
1000
3
1 5 10
100
2
5 7
22

T 테스트케이스
N  동전의 가지수
a, b 동전의 각 금액이 오름차순 정렬
M 타겟 금액
"""
