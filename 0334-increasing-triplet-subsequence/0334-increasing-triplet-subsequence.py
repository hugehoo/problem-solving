class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first, second = float('inf'), float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        else:
            return False
                