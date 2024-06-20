# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def myGuess(self, lower: int, upper: int) -> int:
        return (lower + upper) >> 1
    def guessNumber(self, n: int) -> int:
        lowerBound, upperBound = 1, n
        # myGuess = (lowerBound+upperBound) >> 1
        myGuess = self.myGuess(lowerBound, upperBound)
        while (res := guess(myGuess)) != 0:
            if res == 1:
                lowerBound = myGuess+1
            else:
                upperBound = myGuess-1
            # myGuess = (lowerBound+upperBound) >> 1
            myGuess = self.myGuess(lowerBound, upperBound)
    
        return myGuess
