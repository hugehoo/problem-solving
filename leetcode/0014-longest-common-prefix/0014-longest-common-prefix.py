class Solution:
    def longestCommonPrefix(self, strs) -> str:
        strs = list(map(lambda x: list(x), strs))
        result = ""
        for a in zip(*strs):
            if len(set(a)) == 1:
                result += a[0]
            else:
                break
        return result