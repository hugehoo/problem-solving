class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = "".join(str.lower(s_) for s_ in s if s_.isalpha() or s_.isnumeric())
        return ss == ss[::-1]
    


s = Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama"))
print(s.isPalindrome("race a car"))
print(s.isPalindrome("0P"))
