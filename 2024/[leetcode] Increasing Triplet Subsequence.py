class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        nums.sort(reverse=True)
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        else:
            return False
        
        # 다른 방법 없을까.


s = Solution()

print(s.increasingTriplet([2, 1, 5, 0, 4, 6]))
