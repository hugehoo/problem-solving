import collections


class Solution:
    def minimumAbsDifference(self, arr: list[int]) -> list[list[int]]:
        maxi = float('inf')
        arr.sort()
        diff_dict = collections.defaultdict(list)

        for i in range(len(arr) - 1):
            abs1 = abs(arr[i + 1] - arr[i])
            diff_dict[abs1].append([arr[i], arr[i + 1]])
            maxi = min(abs1, maxi)
            
        return diff_dict[maxi]



s = Solution()
print(s.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
print(s.minimumAbsDifference([1, 3, 6, 10, 15]))
