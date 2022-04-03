class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            sub = target - nums[i]
            try:
                find = nums.index(sub, i + 1)
            except ValueError:
                continue
            return [i, find]
