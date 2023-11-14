class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = []
        for i in range(n + 1):
            b_ = bin(i).split("0b")[1]
            dp.append(list(b_).count('1'))
            
        return dp