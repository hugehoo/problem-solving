class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        for n in nums:
            if n != 0:
                continue
            nums.remove(n)
            nums.append(n)
            