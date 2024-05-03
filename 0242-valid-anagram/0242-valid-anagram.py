class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_ = sorted(list(s))
        t_ = sorted(list(t))
        
        if s_ == t_:
            return True
        else: 
            return False