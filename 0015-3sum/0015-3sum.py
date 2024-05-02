class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = set()
        for s in range(len(nums) - 2):
            m, e = s + 1, len(nums) - 1
            while m < e:
                temp = nums[s] + nums[m] + nums[e]
                if temp > 0:
                    e -= 1
                elif temp < 0:
                    m += 1
                else:
                    result.add((nums[s], nums[m], nums[e]))
                    m += 1
                    e -= 1
        return [list(r) for r in result]