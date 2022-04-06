class Solution:
    def maxSubArray(self, nums) -> int:
        N = len(nums)

        dp = [0] * N
        dp[0] = nums[0]
        max_ = dp[0]
        for i in range(1, N):
            dp[i] = nums[i] + (dp[i - 1] if dp[i - 1] > 0 else 0)
            max_ = max(dp[i], max_)
        return max_

    # [true_value] if [condition] else [false_value] // 파이썬 지원


s = Solution()
print(s.maxSubArray([1, 2, 3])
)
