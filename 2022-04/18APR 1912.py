# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# print(n, m)
# arr = list(map(int, input().strip().split(" ")))
#
# """
# 현재 값
# 최대 값 <- 현재 값을 차곡 차곡
# 이전의 값을 기억해두고, 현재 값과 더했을 때 더 작아지면,
#
# 수의 합을 반복적으로 구한다.
# 합이 음수이면, 그 다음 수부터 다시 시작한다.(1번부터)
# 합의 최대값을 도출한다.
# """
#
# # 1
# total = 0
# temp = 0
# for idx in range(len(arr)):
#     temp += arr[idx]
#     if temp > total:
#         total = temp
#     else:
#         temp = 0
# if total == 0:
#     print(max(arr))
# else:
#     print(total)
#
# # 2
# cache = [0] * len(arr)
# cache[0] = arr[0]
# max_cache = 0
# for idx in range(len(arr)):
#     cache[idx] = max(0, cache[idx - 1]) + arr[idx]
# print(cache)
#
# # for idx, a in enumerate(arr):
# #     if max_value < max_value + arr[idx]:
# #         curr = arr[idx]
# #         max_value = curr + arr[idx]
# #     else:
# #         max_value = curr + arr[idx]
# # print(max_value)
#     # max_value = max()
#     # cache[idx] = max(0, cache[idx - 1]) + arr[idx]
# # print(max(cache))
# # print(cache)
# """
# 5 0
# -7 -3 -2 5 8
# """

n = input()
arr = list(map(int, input().strip().split(" ")))
cache = [0] * len(arr)
cache[0] = arr[0]
max_cache = 0
for idx in range(len(arr)):
    cache[idx] = max(0, cache[idx - 1]) + arr[idx]
print(max(cache))