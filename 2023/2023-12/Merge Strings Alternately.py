class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = list(word1)
        b = list(word2)
        result = []
        if len(a) < len(b):
            for i in range(len(a)):
                result.append(a[i])
                result.append(b[i])
            return "".join(result + b[len(a):])
        else:
            for i in range(len(b)):
                result.append(a[i])
                result.append(b[i])
            return "".join(result + a[len(b):])


s = Solution()
print(s.mergeAlternately("abc", "pqr"))
