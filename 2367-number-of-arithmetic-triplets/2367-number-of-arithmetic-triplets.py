class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        count = 0
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                if nums[j] - nums[i] != diff:
                    continue
                for k in range(j + 1, len(nums)):
                    if nums[k] - nums[j] != diff:
                        continue
                    count += 1
        return count
