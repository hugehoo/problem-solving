# def solution(money, costs):
#     answer = 0
#     won = [1, 5, 10, 50, 100, 500]
#     won.sort(reverse=True)
#     origin_money = money
#     for i in won:
#         print(money)
#         print(i, money // i)
#         money -= ((money // i) * i)
#     print(' ')
#     money = origin_money
#     for i in won[1:]:
#         print(money)
#         print(i, money // i)
#         money -= ((money // i) * i)
size = [1, 5, 10, 50, 100, 500]
value = [1, 4, 99, 35, 50, 1000]


def knapsack(capacity, n):
    if capacity == 0 or n == 0:
        return 0
    if size[n - 1] > capacity:
        return knapsack(capacity, n - 1)
    else:
        return max(value[n - 1] + knapsack(capacity - size[n - 1], n - 1), knapsack(capacity, n - 1))


print(knapsack(4578, 6))
