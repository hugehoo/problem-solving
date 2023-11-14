from itertools import combinations


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        for a, b in combinations(nums, 2):
            if abs(a - b) == k:
                count += 1
        return count


s = Solution()
print(s.countKDifference([1, 2, 2, 1], 1))
print(s.countKDifference([1, 3], 3))
print(s.countKDifference([3, 2, 1, 5, 4], 2))
