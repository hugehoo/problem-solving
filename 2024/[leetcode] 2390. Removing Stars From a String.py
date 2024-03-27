class Solution:
    def removeStars(self, s: str) -> str:
        result = []
        list_s = list(s)
        

        for s in list_s:
            if s == "*":
                result.pop()
            else:
                result.append(s)
                
        
        return "".join(result)


s = Solution()
print(s.removeStars("leet**cod*e"))
print(s.removeStars("erase*****"))
