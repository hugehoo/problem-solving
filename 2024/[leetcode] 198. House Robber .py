class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) < 2:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], nums[0])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
        return dp[-1]
        
        # 퐁당퐁당을 해야 하는게 아니었다.
        # 그냥 인접하지 않으면 됨.


s = Solution()
print(s.rob([2, 7, 9, 3, 1]))
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 1, 1, 2]))
