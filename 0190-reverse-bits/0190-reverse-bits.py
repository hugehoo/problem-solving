class Solution:
    def reverseBits(self, n: int) -> int:
        binary = bin(n)[2:][::-1]
        
        res = binary + '0' * (32 - len(binary))
        
        return int(res, 2)