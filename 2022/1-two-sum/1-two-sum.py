class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            try:
                sub = target - nums[i]
                find = nums.index(sub, i + 1)
            except ValueError:
                continue
            return [i, find]
