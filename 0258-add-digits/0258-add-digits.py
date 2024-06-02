from functools import reduce


class Solution(object):
    def addDigits(self, num):
        string_num = str(num)
        while len(string_num) > 1:
            string_num = str(reduce(lambda x, y: int(x) + int(y), string_num))
        return int(string_num)