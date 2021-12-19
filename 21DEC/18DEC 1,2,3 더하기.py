from itertools import permutations, combinations


# 순열, permutation
# 1, 2, 3 합으로 나타내
N = int(input())
# for _ in range(N):
#     M = int(input())
# arr = [1, 2, 3]
one = [1] * 11
two = [2] * 5
three = [3] * 3
arr = one + two + three
for _ in range(N):
    M = int(input())
    check = []
    for i in reversed(range(1, 12)):
        for j in combinations(arr, i):
            if sum(j) == M:
                for k in permutations(j, len(j)):
                    if k not in check:
                        check.append(k)
                break
    print(check)
    print(len(check))

# for i in permutations(arr, 3):
#     print(sum(i))

# 3이 있으면 3으로 만들 수 있는 경우의 수,

"""
3
4
7
10

1, 2, 3
"""
