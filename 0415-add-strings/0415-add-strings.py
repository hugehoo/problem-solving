import sys

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(0)
        
        return str(eval(num1 + "+" + num2))