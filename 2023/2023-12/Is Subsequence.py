class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for s_ in s:
            idx = t.find(s_)
            if idx == -1:
                return False
            t = t[idx + 1:]
        return True
    

s = Solution()
print(s.isSubsequence("abc", "ahabc"))
print(s.isSubsequence("abdx", "ahabcd"))
