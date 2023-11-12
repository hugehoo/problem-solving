from itertools import combinations


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        return len([1 for c in combinations(nums, 2) if c[0] == c[1]])


s = Solution()
print(s.numIdenticalPairs([1, 2, 3, 1, 1, 3]))
print(s.numIdenticalPairs([1, 1, 1, 1]))
print(s.numIdenticalPairs([1, 2, 3]))
