N = int(input())
balls = []
dp = [float('inf')] * (N + 1)
dp[1] = 1

b = 0
i = 1

while i < N:
    b += (i * (i + 1)) // 2
    balls.append(b)
    i += 1

for n in range(1, N + 1):
    for b in balls:
        if b >= n:
            if b == n:
                dp[b] = 1
            break
        dp[n] = min(dp[n], 1 + dp[n - b])
print(dp[N])
