class Solution:
    def asteroidCollision(self, asteroids: list[int]) -> list[int]:
        i = 0
        while i < len(asteroids) - 1:
            # 양수 , 음수
            if asteroids[i] > 0 > asteroids[i + 1] and i >= 0:
                if abs(asteroids[i]) > abs(asteroids[i + 1]):
                    del asteroids[i + 1]
                    i -= 1
                elif abs(asteroids[i]) < abs(asteroids[i + 1]):
                    del asteroids[i]
                    i -= 1
                else:
                    del asteroids[i + 1]
                    del asteroids[i]
                    i -= 1
            else:
                i += 1
                
        return asteroids
