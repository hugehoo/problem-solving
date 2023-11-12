class Solution:
    def arithmeticTriplets(self, nums: list[int], diff: int) -> int:
        set_num = set(nums)
        return sum(1 for n in nums if n + diff in set_num and n + (diff * 2) in set_num)
        

s = Solution()
print(s.arithmeticTriplets([0, 1, 4, 6, 7, 10], 3))
print(s.arithmeticTriplets([4, 5, 6, 7, 8, 9], 2))
