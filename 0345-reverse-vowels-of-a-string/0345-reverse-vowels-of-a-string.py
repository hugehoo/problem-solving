class Solution(object):
    def reverseVowels(self, s):
        
        list_s = list(s)
        vowels = {'a', 'e', 'o', 'u', 'i', 'A', 'E', 'O', 'U', 'I'}
        temp = [ls for ls in list_s if ls in vowels]
        for idx, ls in enumerate(list_s):
            if ls in vowels:
                pop = temp.pop()
                list_s[idx] = pop
        return ''.join(list_s)
