class Solution:
    def canJump(self, nums: list[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            
            if n > gas:
                gas = n
            gas -= 1
        return True
            
