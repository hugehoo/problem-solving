class Solution:
    def minimumSum(self, num: int) -> int:
        nums = sorted((str(num)))
        return int(nums[0] + nums[2]) + int(nums[1] + nums[3])


s = Solution()

print(s.minimumSum(2932))
print(s.minimumSum(4009))
