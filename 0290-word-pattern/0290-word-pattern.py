class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        res = {}
        if len(list(pattern)) != len(s):
            return False
        pattern_set = set(list(pattern))
        s_set = set(s)
        if len(pattern_set) != len(s_set):
            return False
        for x, y in zip(pattern, s):
            if res.get(x):
                if res[x] != y:
                    return False
            else:
                res[x] = y
        return True