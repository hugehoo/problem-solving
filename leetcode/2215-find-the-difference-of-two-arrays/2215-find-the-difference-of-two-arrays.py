class Solution(object):
    def findDifference(self, nums1, nums2):
        num1 = set(nums1)
        num2 = set(nums2)
        
        num1_diff = num1.difference(num2)
        num2_diff = num2.difference(num1)
        
        return [list(num1_diff), list(num2_diff)]