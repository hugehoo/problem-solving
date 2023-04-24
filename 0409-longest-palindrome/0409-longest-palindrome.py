from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_counts = Counter(s)
        result = sum(v // 2 * 2 for v in char_counts.values())
        if result < len(s):
            result += 1
        return result