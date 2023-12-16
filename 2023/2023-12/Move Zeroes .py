class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1


s = Solution()
print(s.moveZeroes([0, 0, 1, 3, 12]))
# Output: [1,3,12,0,0]
