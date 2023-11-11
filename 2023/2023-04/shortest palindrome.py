class Solution:
    def shortestPalindrome(self, s: str) -> str:
        r = s[::-1]
        for i in range(len(s)):
            if s.startswith(r[i:]):
                return r[:i] + s
        return r + s


s = Solution()
print(s.shortestPalindrome("aacecaaa"))
"""
_ _ _ _ _ _ _ _ a a c e c a a a
한글자가 추가된다고 하면. -> 추가됐을 때 총 길이를 구해서 -> 중앙값 구함 -> palindrome 되는지 검증
안되면 또 한글자 더 추가 -> 변경된 중앙값 기준으로 검증 ->
"""
