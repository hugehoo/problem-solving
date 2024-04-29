class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = [0]
        for idx, value in enumerate(gain):
            altitude.append(altitude[idx] + value)
        return max(altitude)


s = Solution()
print(s.largestAltitude([-5, 1, 5, 0, -7]))
print(s.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
