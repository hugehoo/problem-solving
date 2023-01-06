# N = int(input())
# arr = list(map(int, input().split()))
# arr.sort()
# ans = 1
#
# board = {}
# for a in arr:
#     board.setdefault(a, 0)
#     board[a] += 1
# while True:
#     get = board.get(1)
#     if not get:
#
#     ans += 1
#
# """
# 1 1 2 3 6 7 30
#
# 주어진 배열의 작은 수부터 더해서, 1부터 1000까지의 수 배열을 만들어본다.
# 1000이 아니라 100만이라  배열은 안될듯
# 딕셔너리?
# for a in arr:
#     answer[a] += 1
# ex, 1 2 x x 5 x 7
# 개수 1 2 0 0 1 0 1
# 3은 비어있지만 1 + 2 로 만들 수 있다
# 4도 비었지만, 2 가 2개이므로 만들 수 있다.
# 6도 비었지만, 1 + 5로 만들 수 있다.
#
# x 가 있는 곳은, x 보다 작은 숫자범위 내에서 조합하여 만들면 된다.
# combination 돌릴까.
#
# """
#
# # def sample(answer, arr):
# #     count = 0
# #     if answer in arr:
# #         return True
# #
# #     for a in arr:
# #         answer -= a
# #         if answer in arr:
# #             return True
# # while True:
# #     if sample(ans, arr):
# #         ans += 1
# #     else:
# #         break

import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

target = 1

for num in arr:
    if target < num:
        break

    target += num

print(target)