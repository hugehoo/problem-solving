class Solution(object):
    def reverseVowels(self, s):

        list_s = list(s)
        vowels = {'a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I'}
        temp = [ls for ls in list_s if ls in vowels]
        temp.reverse()
        for idx, ls in enumerate(list_s):
            if ls in vowels:
                list_s[idx] = temp[0]
                temp = temp[1:]
        return ''.join(list_s)
