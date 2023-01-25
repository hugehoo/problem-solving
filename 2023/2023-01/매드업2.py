from itertools import combinations
from copy import deepcopy

max_long = 1


def find_max_long(temp):
    global max_long
    temp_long = 1
    for t in range(len(temp) - 1):
        if temp[t] == temp[t + 1]:
            temp_long += 1
        else:
            max_long = max(temp_long, max_long)
            temp_long = 1
    max_long = max(temp_long, max_long)


def solution(N, K, blocks):
    global max_long
    frequent_value = max(blocks, key=blocks.count)
    idxs = [idx for idx, v in enumerate(blocks) if v != frequent_value]
    if len(idxs) <= K:
        print(len(blocks))
        exit()
    for c in list(combinations(idxs, K)):
        temp = deepcopy(blocks)
        for c_ in c:
            temp[c_] = frequent_value
        find_max_long(temp)
    return max_long


result = solution(6, 2, [1, 2, 3, 2, 4, 2])
print(result)

# result = solution(4, 2, [1, 2, 1, 1])
# print(result)

# result = solution(3, 2, [1, 1, 1])
# print(result)
