class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = bin(a)
        b = bin(b)
        print(int(a, 2) + int(b, 2))
        return bin(a) + bin(b)
    

s = Solution()
print(s.addBinary(11, 1))

