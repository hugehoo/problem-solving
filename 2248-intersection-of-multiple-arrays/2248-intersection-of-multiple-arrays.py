class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        temp = nums[0]
        for i in range(1, len(nums)):
            temp = list(set(temp) & set(nums[i]))
        return sorted(temp)