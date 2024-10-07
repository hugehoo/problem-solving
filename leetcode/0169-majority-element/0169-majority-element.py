class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s_n = set(nums)
        for s in list(s_n):
            if nums.count(s) > len(nums) // 2:
                return s
        