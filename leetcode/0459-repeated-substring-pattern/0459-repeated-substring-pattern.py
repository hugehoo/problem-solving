class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        N = len(s)
        # s = list(s)
        for i in range(1, N):
            after = s[i:]
            before = s[:i]
            if after.startswith(before):
                M = N // len(before)
                if before * M == s:
                    return True
        else:
            return False

        