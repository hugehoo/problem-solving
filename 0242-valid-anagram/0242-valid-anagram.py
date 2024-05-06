class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_ = sorted(list(s))
        t_ = sorted(list(t))
        
        return s_ == t_
