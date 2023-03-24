from collections import deque


class Solution:
    
    def romanToInt(self, s: str) -> int:
        dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900
        }
        q = deque(s)
        result = 0
        while q:
            pop = q.popleft()
            if q and (pop + q[0]) in dic:
                result += dic[pop + q[0]]
                q.popleft()
            else:
                result += dic[pop]
        return result


s = Solution()
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
