import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

# 1
a = list(combinations(range(n), m))
print((len(a)))


# 2
def combi(n, m):
    if m == 0 or n == m:
        return 1
    return combi(n - 1, m) + combi(n - 1, m - 1)


print(combi(n, m))
