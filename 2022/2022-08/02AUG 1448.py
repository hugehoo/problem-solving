n = int(input())
nums = sorted([int(input()) for _ in range(n)], reverse=True)

for i in range(len(nums) - 2):
    if nums[i] < nums[i + 1] + nums[i + 2]:
        print(sum(nums[i: i + 3]))
        exit()
else:
    print(-1)
