class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        if list(x_str) == list(x_str)[::-1]:
            return True
        return False


s = Solution()
print(s.isPalindrome(121))
print(s.isPalindrome(-121))
print(s.isPalindrome(10))
