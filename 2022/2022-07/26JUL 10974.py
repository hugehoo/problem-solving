from itertools import permutations

T = int(input())
for p in permutations([i for i in range(1, T+1)]):
    print(*p)
