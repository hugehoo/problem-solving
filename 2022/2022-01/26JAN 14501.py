N = int(input())
arr_t = [0]
arr_p = [0]
dp = [0] * (N + 2)

for _ in range(N):
    t, p = map(int, input().split())
    arr_t.append(t)
    arr_p.append(p)

for i in range(1, N + 2):
    for j in range(1, i):
        dp[i] = max(dp[j], dp[i])
        if j + arr_t[j] == i:
            dp[i] = max(dp[i], arr_p[j] + dp[j])
print(max(dp))
