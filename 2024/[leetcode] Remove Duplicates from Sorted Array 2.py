class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        dict_ = {}
        dict_.get()
        removed = 0
        for idx, n in enumerate(nums):
            if dict_.get(n) == 2:
                removed += 1
                nums[idx] = float('inf')
                continue
            dict_[n] = dict_.setdefault(n, 0) + 1
        nums.sort()
        count = 0
        for n in nums:
            if n != float('inf'):
                count += 1
        return count


s = Solution()
print(s.removeDuplicates([1, 1, 1, 2, 2, 3]))
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s.lower()
        
        sl = sorted(list(s))
        tl = sorted(list(t))
        for i in range(len(sl)):
            if sl[i] != tl[i]:
                return tl[i]
        return tl[-1]