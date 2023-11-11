from collections import Counter


class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1
        return [k for k, v in dic.items() if v == 1][0]
        

s = Solution()
print(s.singleNumber([2, 2, 2, 1]))
