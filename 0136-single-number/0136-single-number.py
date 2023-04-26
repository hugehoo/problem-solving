

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        n = Counter(nums)
        return [n_ for n_ in n if n.get(n_) == 1][0]