class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(str.lower(s_) for s_ in s if s_.isalpha() or s_.isnumeric())
        return ss == ss[::-1]
    