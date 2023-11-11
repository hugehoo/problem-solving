class Solution(object):
    def singleNumber(self, nums: list):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in nums:
            dict[i] = dict.setdefault(i, 0) + 1
        for k, v in dict.items():
            if v == 1:
                return k


solution = Solution()
print(solution.singleNumber([3, 3, 3, 2]))
