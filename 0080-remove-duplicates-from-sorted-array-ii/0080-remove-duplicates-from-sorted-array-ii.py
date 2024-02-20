class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dict_ = {}
        removed = 0
        for idx, n in enumerate(nums):
            if dict_.get(n) == 2:
                removed += 1
                nums[idx] = float('inf')
                continue
            dict_[n] = dict_.setdefault(n, 0) + 1
        nums.sort()
        count = 0
        for n in nums:
            if n != float('inf'):
                count += 1
        return count