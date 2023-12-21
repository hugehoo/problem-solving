class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        
        for i in range(k, len(nums)):
            curr_sum = curr_sum + nums[i] - nums[i - k]
            max_sum = max(max_sum, curr_sum)
        return max_sum / k


s = Solution()
print(s.findMaxAverage([1, 12, -5, -6, 50, 3], 4))
print(s.findMaxAverage([5], 1))
