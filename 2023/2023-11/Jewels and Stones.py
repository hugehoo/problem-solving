class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        result = 0
        
        stone_list = list(stones)
        jewel_list = list(jewels)
        for j in jewel_list:
            result += stone_list.count(j)
        return result


s = Solution()
result = s.numJewelsInStones("aA", "AAbac")
print(result)
