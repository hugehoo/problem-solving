class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        altitude = [0]
        for idx, value in enumerate(gain):
            altitude.append(altitude[idx] + value)
        return max(altitude)
