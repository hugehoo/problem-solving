class Solution:
    def canJump(self, nums: list[int]) -> bool:
        reachable = 0
        for i in range(len(nums)):
            if reachable >= len(nums) - 1:
                return True
                
            if i > reachable:
                return False
            reachable = max(reachable, i + nums[i])
        return True