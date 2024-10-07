class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = {}
        for r in ransomNote:
            dict[r] = dict.setdefault(r, 0) + 1
        for k, v in dict.items():
            if magazine.count(k) < v:
                return False
        return True