# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
def guess(num: int) -> int:
    return


class Solution:
    def myGuess(self, lower: int, upper: int) -> int:
        return (lower + upper) >> 1
    
    def guessNumber(self, n: int) -> int:
        lower_bound, upper_bound = 1, n
        my_guess = self.myGuess(lower_bound, upper_bound)
        while (res := guess(my_guess)) != 0:
            if res == 1:
                lower_bound = my_guess + 1
            else:
                upper_bound = my_guess - 1
            my_guess = self.myGuess(lower_bound, upper_bound)
        
        return my_guess


s = Solution()
print(s.guessNumber(10))


