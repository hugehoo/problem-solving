# from itertools import combinations
#
N = int(input())
arr = sorted(list(map(int, input().split())))
#
# # num_set = set()
# # for n in range(1, N+1):
# #     for c in combinations(arr, n):
# #         num_set.add(sum(c))
# #
# # i = 1
# # while True:
# #     if i not in num_set:
# #         print(i)
# #         exit()
# #     i += 1
#
#
# # 나름 투 포인터라는 생각이 드네.
# a = 0
# for i in arr:
#     if a + 1 < i:
#         break
#     a += 1
# print(a + 1)

a = 0
for i in arr:
    if a + 1 < i:
        break
    a += i
print(a + 1)
