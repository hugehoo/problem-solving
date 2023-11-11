class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        temp = sorted(list(set(nums)))
        for i, v in enumerate(temp):
            nums[i] = v
        return len(temp)

s = Solution()
print(s.removeDuplicates([1, 1, 2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
