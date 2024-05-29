from functools import reduce


class Solution(object):
    def addDigits(self, num):
        string_num = str(num)
        while len(string_num) > 1:
            result = reduce(lambda x, y: int(x) + int(y), string_num)
            string_num = str(result)
        return int(string_num)


s = Solution()
print(s.addDigits(28))
print(s.addDigits(38))
