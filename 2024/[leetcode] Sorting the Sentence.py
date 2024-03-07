class Solution:
    def sortSentence(self, s: str) -> str:
        split = s.split(" ")
        result = [0] * len(split)
        for s_ in split:
            idx = s_[-1]
            result[int(idx) - 1] = s_[:-1]
        return ' '.join(result)
    
    
s = Solution()
print(s.sortSentence("Myself2 Me1 I4 and3"))

