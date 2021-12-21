# from itertools import permutations, combinations, product, combinations_with_replacement
# 1, 2, 3 합으로 나타내
# N = int(input())
# four_set = set()
# three_set = set()
# for n in range(1, 5):
#     for c in combinations_with_replacement([1, 2, 3], n):
#         if sum(c) == 4:
#             for r in permutations(c):
#                 four_set.add(r)
# for n in range(1, 4):
#     for c in combinations_with_replacement([1, 2, 3], n):
#         if sum(c) == 3:
#             for r in permutations(c):
#                 three_set.add(r)
# print(four_set, three_set)
N = int(input())


def recursive(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return recursive(n - 1) + recursive(n - 2) + recursive(n - 3)


for _ in range(N):
    print(recursive(int(input())))

"""
3
4
7
10

1, 2, 3
"""
