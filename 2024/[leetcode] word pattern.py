class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(list(pattern)) != len(s_list) or len(set(list(pattern))) != len(set(s_list)):
            return False
        res = {}
        for x, y in zip(pattern, s_list):
            if res.get(x):
                if res[x] != y:
                    return False
            else:
                res[x] = y
        return True

s = Solution()
print(s.wordPattern("abba", "dog dog dog dog"))



