class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            try:
                find = nums.index(target - nums[i], i + 1)
            except ValueError:
                continue
            return [i, find]
