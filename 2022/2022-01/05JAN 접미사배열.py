from sys import stdin

N = stdin.readline().strip()
# for r in sorted([N[i:] for i in range(len(N))]):
#     print(r)
#
# """
# baekjoon
# """

arr = list(N)
print(arr)
M = int(stdin.readline())
idx = len(arr)
for _ in range(M):
    k = input()
    if len(k) > 1:
        if idx >= 0:
            print('idx', idx)
            arr.insert(idx, k[-1])
            idx += 1
            print(arr)
    else:
        if k == 'L':
            idx -= 1
            print('k', k, 'idx', idx)


print(arr)
"""
abcd
3
P x
L
P y


abc
9
L
L
L
L
L
P x
L
B
P y
"""
