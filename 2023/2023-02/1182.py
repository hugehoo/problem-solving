N, S = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0


def backtracking(idx, partial_sum):
    global cnt
    
    if idx >= N:
        return

    partial_sum += nums[idx]

    if partial_sum == S:
        cnt += 1

    backtracking(idx + 1, partial_sum)
    backtracking(idx + 1, partial_sum - nums[idx])


backtracking(0, 0)
print(cnt)


"""
5 0
-7 -3 -2 5 8
"""
