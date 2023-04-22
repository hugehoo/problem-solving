class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for s_ in s[::-1]:
            if s_ != " ":
                count += 1
                continue
            if count:
                return count
        return count