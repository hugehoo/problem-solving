class Solution(object):
    def isIsomorphic(self, s, t):
        s_dict = {}
        for s_, t_ in zip(list(s), list(t)):
            if not s_dict.get(s_):
                s_dict[s_] = t_
            else:
                if s_dict[s_] != t_:
                    return False
        return True
    

s = Solution()
print(s.isIsomorphic("egg", "add"))
print(s.isIsomorphic("foo", "var"))
print(s.isIsomorphic("paper", "title"))

