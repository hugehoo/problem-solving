class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.index(needle)
        else:
            return -1


s = Solution()
print(s.strStr("sadbutsad", "sad"))
print(s.strStr("leetcode", "leeto"))
