class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        for s_ in list(s):
            dic[s_] = dic.get(s_, 0) + 1
        result = 0
        odds = []
        for v in dic.values():
            if v % 2 == 0:
                result += v
            else:
                odds.append(v)
        odds.sort(reverse=True)
        if odds and odds[0] == 1:
            return result + 1
        elif odds:
            total = sum(num - 1 for num in odds[1:])
            return result + odds[0] + total
        return result