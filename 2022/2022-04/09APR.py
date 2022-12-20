class Solution:
    def searchInsert(self, nums, target: int) -> int:
        N = len(nums)
        start = 0
        end = N
        while start < end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
        if end == -1:
            return 0
        print('s e ', start - 1, end + 1)
        return end


solution = Solution()
print(solution.searchInsert(nums=[1, 3, 5, 6], target=5))
print(solution.searchInsert(nums=[1, 3, 5, 6], target=2))
print(solution.searchInsert(nums=[1, 3, 5, 6], target=7))
print(solution.searchInsert([1, 3, 5, 6], 0))
print(solution.searchInsert([1, 3], 2))
print(solution.searchInsert(nums=[1, 3, 5, 6, 9], target=8))
