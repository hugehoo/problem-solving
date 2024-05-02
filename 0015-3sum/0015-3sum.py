class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        print(nums)
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
                    e_ = ((nums[s]), nums[m], nums[e])
                    result.add(e_)
                    m += 1
                    e -= 1
        return [list(r) for r in result]
    