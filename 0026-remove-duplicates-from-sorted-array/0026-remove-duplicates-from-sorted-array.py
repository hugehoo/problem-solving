class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp = sorted(list(set(nums)))
        for i, v in enumerate(temp):
            nums[i] = v
        return len(temp)
