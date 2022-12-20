
N, M = map(int, input().split())
arr = list(map(int, input().split()))
s, e = 0, 0
count = 0

while s < N:
    partial_sum = sum(arr[s: e])
    if partial_sum == M:
        count += 1
        s += 1
        continue

    if partial_sum > M or e == N:
        s += 1
    else:
        e += 1


print(count)





"""
부분합이 m이 되도록

1) e == N 이면 s++
2) s == e 이면 e ++
3) sum = M 이면 e ++
4) sum < M 이면 e ++ 
5) M < sum 이면 s ++  
"""

