from itertools import combinations


class Solution:
    def countKDifference(self, nums: list[int], k: int) -> int:
        count = 0
        for a, b in combinations(nums, 2):
            if abs(a - b) == k:
                count += 1
        return count
