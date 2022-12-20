import sys
from copy import deepcopy

n = int(sys.stdin.readline())
cards = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
for i in range(1, n + 1):
    for k in range(1, i + 1):
        dp[i] = max(dp[i], dp[i - k] + cards[k])
print(dp[-1])

"""
dp = [] 각 장을 살때 지불할 수 있는 최대 금액을 저장.
2장을 만드려면 1 + 1, 2
3장을 만드려면, 1 + 1 + 1, 1 + 2, 3
4장을 만드려면, 1 + 1 + 1 + 1, 1 + 3, 2 + 2, 4 <- 내가 이런식으로 여러 경우를 구현하려 했던걸, 이중 for문으로 만들 수 있따. 

dp[i] i 번째에서 만들수 있는 최대 값. 
dp[5 - 3] + cards[3] => dp[2] 2를 만들 때의 최대값 + 기존 3번째의 값.   
"""
