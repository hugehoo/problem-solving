# N, K = map(int, input().split())
# arr = [int(input()) for _ in range(N)]
# dp = [0] * (K + 1)
# dp[0] = 1
# for a in arr:
#     for j in range(a, K + 1):
#         dp[j] += dp[j - a]
# print(dp[K])

"""
arr 의 부분 합을 이용해 K 가 되도록. 
다만 연속 부분 합이 아니다.

dp = [] <- 각 자리수를 만드는데 몇가지 경우가 있는지 기록.
각각의 동전은 몇개라도 사용할 수 있다. 
"""


def selection_sort(arr):
    for i in range(len(arr) - 1):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


print(selection_sort([5, 2, 6, 1, 3]))
