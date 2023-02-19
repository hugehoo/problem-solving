from itertools import combinations

N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0

for n in range(1, N+1):
    for c in list(combinations(nums, n)):
        if sum(c) == S:
            cnt += 1

print(cnt)
"""
5 0
-7 -3 -2 5 8
"""
