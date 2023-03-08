N = int(input())
balls = []

b = 0
i = 1
while b < N:
    b += (i * (i + 1)) // 2
    balls.append(b)
    i += 1
# print(balls)
MAX = float('inf')
dp = [MAX] * (N + 1)
# b 는 사면체 갯수 모음, 각 인덱스가 몇 층 짜리 사면체 인지 의미.
for i in range(1, N + 1):
    for b in balls:
        if b >= i:
            if b == i:
                dp[i] = 1
            break
        # 여기는 b 가 i 보다 작음을 의미 => i 개로 b 를 만들 수 있따.
        # i 가 b 보다 크므로, i - b 는 양수. b 는 이미 만들어진 정사면체 하나. 그러기에 +1 을 해주는 것.
        # i - b 는 이미 잘 만들어진 b 를 이루는 공의 개수에서, 현재 가진 공의 수 i 를 뺀 것.
        dp[i] = min(dp[i], 1 + dp[i - b]) # dp[i - b] ?
# print(dp)
# print(len(dp))
print(dp[N])

"""
"""

"""
최소 개수

1 2 3  4  5  6  7  8
1 4 10 20 35 56 84 120

15 -> 3

10 4 1

9
4 4 1
91


"""
