class Solution:
    def search(self, nums, target: int) -> int:
        N = len(nums)
        start = 0
        end = N - 1
        medium = (end - start) // 2 + 1
        while start <= end:
            # medium = N // 2
            if nums[medium] > target:
                end = medium - 1
                medium = (end + start) // 2
                # print('l', medium)

            elif nums[medium] < target:
                start = medium + 1
                medium = (end + start) // 2
                # print('r', medium, end, start)

            else:
                return medium

        return -1


solution = Solution()
print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
print(solution.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
