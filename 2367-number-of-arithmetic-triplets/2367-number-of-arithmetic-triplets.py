class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        set_num = set(nums)
        return sum(1 for n in nums if n + diff in set_num and n + (diff * 2) in set_num)
        
