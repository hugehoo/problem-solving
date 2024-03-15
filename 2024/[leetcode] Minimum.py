class Solution:
    def numberGame(self, nums: list[int]) -> list[int]:
        nums.sort(reverse=True)
        result = []
        for i in range(len(nums) - 1, -1, -2):
            result.append(nums[i - 1])
            result.append(nums[i])
        return result


s = Solution()
print(s.numberGame([1, 2, 3, 4]))
git commit --amend --no-edit --date "Fri 15 Mar 2024 20:19:19 KST"

