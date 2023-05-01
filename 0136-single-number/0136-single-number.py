

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums = Counter(nums)
        return [n_ for n_ in nums if nums.get(n_) == 1][0]