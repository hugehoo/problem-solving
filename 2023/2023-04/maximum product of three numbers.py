class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums.sort()
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])


s = Solution()
print(s.maximumProduct([1, 2, 3]))
print(s.maximumProduct([1, 2, 3, 4]))
print(s.maximumProduct([1, 2, 3, -4]))
