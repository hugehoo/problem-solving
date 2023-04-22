class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = list(filter(lambda x: len(x) > 0, s.split(" ")))
        return len(words[-1])