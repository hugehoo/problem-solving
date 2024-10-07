class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dict = {}
        for i in nums:
            dict[i] = dict.setdefault(i, 0) + 1
        for k, v in dict.items():
            if v == 1:
                return k