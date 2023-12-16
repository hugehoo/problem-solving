class Solution(object):
    def reverseVowels(self, s):
        list_s = list(s)
        vowels = {'a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I'}
        temp = [ls for ls in list_s if ls in vowels]
        for idx, ls in enumerate(list_s):
            if ls in vowels:
                list_s[idx] = temp.pop()
        return ''.join(list_s)


s = Solution()
print(s.reverseVowels("hello"))
print(s.reverseVowels("aA"))
print(s.reverseVowels("leetcode"))
