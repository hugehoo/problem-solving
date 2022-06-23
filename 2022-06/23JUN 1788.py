n = int(input())
if n == 0:
    print(0, 0, sep='\n')
    exit()

dp = [0 for _ in range(1 + abs(n))]
dp[0], dp[1] = 0, 1

for i in range(2, len(dp)):
    dp[i] = (dp[i-1] + dp[i-2]) % 1000000000

idx = abs(n)
answer = -dp[idx] if n < 0 and n % 2 == 0 else dp[idx]

print(1 if answer > 0 else -1)
print(abs(answer))