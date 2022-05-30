import sys
from copy import deepcopy

input = sys.stdin.readline

M = int(input())
list1 = list(map(int, input().strip()))
list2 = list(map(int, input().strip()))
array1 = deepcopy(list1)
array2 = deepcopy(list1)


def two_flip(a, b):
    list1[a] = 1 - list1[a]
    list1[b] = 1 - list1[b]


def three_flip(a, b, c):
    list1[a] = 1 - list1[a]
    list1[b] = 1 - list1[b]
    list1[c] = 1 - list1[c]


for i in range(2):
    list1 = array1 if i == 0 else array2
    cnt = 0
    for j in range(M):
        if j == 0:
            if i == 0 and list1 != list2:
                cnt += 1
                two_flip(j, j + 1)
        elif 0 < j <= M - 2:
            if list1[j - 1] != list2[j - 1]:
                cnt += 1
                three_flip(j - 1, j, j + 1)
        elif j == M - 1:
            if list1[j - 1] != list2[j - 1]:
                cnt += 1
                two_flip(j - 1, j)
    if list1 == list2:
        print(cnt)
        break
if list1 != list2:
    print(-1)



