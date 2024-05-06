class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sl = sorted(list(s))
        tl = sorted(list(t))
        for i in range(len(sl)):
            if sl[i] != tl[i]:
                return tl[i]
        return tl[-1]