class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        return sum(stones.count(j) for j in set(jewels))


s = Solution()
result = s.numJewelsInStones("aA", "AAbac")
print(result)
