class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        set_s = set(s)
        set_t = set(t)
        difference = set_t.__contains__(set_s)
        if not difference:
            return False
        sequence = 0
        for s_ in s:
            if t.__contains__(s_):
                if sequence <= t.index(s_):
                    sequence = t.index(s_)
                else:
                    return False
            else:
                return False
        return True
    

s = Solution()
print(s.isSubsequence("aaaaa", "bbbbb"))
print(s.isSubsequence("abc", "ahbgdc"))
print(s.isSubsequence("axc", "ahbgdac"))


