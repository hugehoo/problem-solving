import sys

input = sys.stdin.readline

N, R, C = map(int, input().split())
ans = 0
while N != 0:
    N -= 1
    K = 2 ** N
    if R < K and C < K:  # 1사분면
        ans += 0
    elif R < K <= C:
        ans += (K * K * 1)
        C -= K
    elif C < K <= R:
        ans += (K * K * 2)
        R -= K
    else:
        ans += (K * K * 3)
        R -= K
        C -= K
print(ans)

