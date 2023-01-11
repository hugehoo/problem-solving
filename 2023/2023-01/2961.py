from itertools import combinations
from math import prod
from functools import reduce

N = int(input())
ingredients = [list(map(int, input().split())) for _ in range(N)]

min_value = float('inf')
for n in range(1, N + 1):
    for li in (combinations(ingredients, n)):
        prod_ = prod(list(map(lambda x: x[0], li)))
        sum_ = sum(list(map(lambda x: x[1], li)))
        min_value = min(abs(prod_ - sum_), min_value)
print(min_value)
