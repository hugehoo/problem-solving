class Solution:
    def search(self, nums: list[int], target: int) -> int:
        len_nums = len(nums)
        start = 0
        last = len_nums
        mid = len_nums // 2
        
        while True:
            if nums[mid] == target:
                return mid
            if start >= last or start == mid or mid == last:
                return -1
            elif nums[mid] < target:
                start = mid
                mid = (start + last) // 2
            else:
                last = mid
                mid = (start + last) // 2


s = Solution()
print(s.search([-1, 0, 3, 5, 9, 12], 9))
print(s.search([-1, 0, 3, 5, 9, 12], 2))
