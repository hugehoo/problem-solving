class Solution:
    def hammingWeight(self, n: int) -> int:
        # Convert the integer to its binary representation as a string
        binary_representation = bin(n)[2:]

        # Return the count of '1's in the binary representation
        return binary_representation.count('1')