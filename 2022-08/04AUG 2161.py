from collections import deque


N = int(input())

nums = [n for n in range(1, N + 1)]
nums = deque(nums)


answer = []
while nums:
    answer.append(nums.popleft())
    if nums:
        pops = nums.popleft()
        nums.append(pops)
print(*answer)
