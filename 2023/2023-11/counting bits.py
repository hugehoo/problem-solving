class Solution:
    def countBits(self, n: int) -> list[int]:
        dp = [0]
        for i in range(1, n + 1):
            if i % 2 == 1:
                dp.append(dp[i - 1] + 1)
            else:
                dp.append(dp[i // 2])
        return dp


s = Solution()
print(s.countBits(2))
print(s.countBits(5))
print(s.countBits(10))
print(s.countBits(11))
"""
0
1
1 2
1 2 2 3
1 2 2 3 2 3 3 4
1 2 2 3 2 3 3 4 2 3 2 4 3 4 4 5

0
1
10
11
100
101
110
111
1000
1001
1010
1011
1100
1101
1110
1111
10000
10001
10010
10011
10100
10101
10110
10111
11000
11001
11010
11011
11100
11101
11110
11111

[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2,  3,   2, 3,  3,  4,   1]
0
1
1 2
1 2 2 3
1 2 2 3 2 3 3 4
1 2 2 3 2 3 3 4 2 3 2 4 3 4 4 5
"""
