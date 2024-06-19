class Solution:
    def rob(self, nums: list[int]) -> int:
        N = len(nums)
        if N < 2:
            return nums[0]
        dp = [0] * N
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for n in range(2, N):
            dp[n] = max(nums[n] + dp[n - 2], dp[n - 1])
        return dp[-1]