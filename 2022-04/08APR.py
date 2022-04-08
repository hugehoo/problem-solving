class Solution:
    def twoSum(self, nums, target: int):
        for i in range(len(nums)):
            sub = target - nums[i]
            print(sub)
            try:
                find = nums.index(sub, i + 1)
            except ValueError:
                continue
            return [i, find]


solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))
print(solution.twoSum([3, 3], 6))
print(solution.twoSum([3, 2, 4], 6))
print(solution.twoSum([0, 4, 3, 0], 0))
print(solution.twoSum([-1, -2, -3, -4, -5], -8))
