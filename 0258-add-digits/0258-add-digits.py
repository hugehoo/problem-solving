class Solution(object):
    def addDigits(self, num):
        string_num = str(num)
        while len(string_num) > 1:
            result = 0
            for s in string_num:
                result += int(s)
            string_num = str(result)
        return int(string_num)