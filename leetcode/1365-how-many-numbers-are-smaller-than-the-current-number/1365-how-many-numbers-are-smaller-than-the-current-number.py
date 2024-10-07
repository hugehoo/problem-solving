class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        sorted_nums = sorted(nums, reverse=True)
        num_dict = {}
        N = len(sorted_nums)
        
        for idx, n in enumerate(sorted_nums):
            if idx + 1 == N:
                num_dict[n] = 0
                break
            if sorted_nums[idx + 1] == n:
                continue
            num_dict[n] = N - (idx + 1)
        return [num_dict[n] for n in nums]
