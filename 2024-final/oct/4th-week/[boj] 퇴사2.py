from sys import stdin

input = stdin.readline

if __name__ == '__main__':
    N = int(input().rstrip())
    t = [0]
    p = [0]
    dp = [0] * (N + 1)
    for _ in range(N):
        t_, p_ = map(int, input().split())
        t.append(t_)
        p.append(p_)
    
    for n in range(1, N + 1):
        dp[n] = max(dp[n], dp[n - 1])
        end_date = t[n] + n - 1
        if end_date <= N:
            dp[end_date] = max(dp[end_date], dp[end_date - 1] + p[n])
    print(dp)
