"""
동일한 등차 구간은 제끼고 연산 가능
"""


def solution(arr):
    dp = [1] * len(arr)
    for idx, val, in enumerate(arr):
        fix_idx = idx
        while idx <= len(arr) - 3:
            if arr[idx + 1] - arr[idx] == arr[idx + 2] - arr[idx + 1]:
                dp[fix_idx] += 1
                idx += 1
            else:
                break
    
    return max(dp) + 1


print(solution([2, 3, 4, -1, -6, -11, 1]))
print(solution([0, 0, 0, 0, 0]))
