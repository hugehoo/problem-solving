class Solution:
    def countPairs(self, nums: list[int], target: int) -> int:
        count = 0
        for a in range(0, len(nums) - 1):
            for b in range(a + 1, len(nums)):
                if nums[a] + nums[b] < target:
                    count += 1
                    
        return count