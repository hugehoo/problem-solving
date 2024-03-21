class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1 if i == 0 or j == 0 else 0 for j in range(n)] for i in range(m)]
        
        # 아래 / 오른쪽
        for r in range(1, m):
            for c in range(1, n):
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
        return dp[-1][-1]


s = Solution()
print(s.uniquePaths(3, 7))
print(s.uniquePaths(3, 2))
