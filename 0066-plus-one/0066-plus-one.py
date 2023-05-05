class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        num = int(''.join(list(map(lambda x: str(x), digits)))) + 1
        return list(map(lambda x: int(x), list(str(num))))
