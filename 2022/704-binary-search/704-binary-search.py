class Solution:
    def search(self, nums, target: int) -> int:
        N = len(nums)
        start = 0
        end = N - 1
        medium = (end - start) // 2
        while start <= end:
            if nums[medium] > target:
                end = medium - 1
                medium = (end + start) // 2

            elif nums[medium] < target:
                start = medium + 1
                medium = (end + start) // 2

            else:
                return medium

        return -1