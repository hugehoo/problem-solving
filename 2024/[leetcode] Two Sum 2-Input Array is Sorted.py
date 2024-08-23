class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]
            


s = Solution()
print(s.twoSum([2, 7, 11, 15], 9))
print(s.twoSum([2, 3, 4], 6))
print(s.twoSum([-1, 0], -1))

# 오름차순. 0,1에서 시작 -> 더했을 때 타겟보다 작으면 오른쪽애를 증가. 왼쪽애도 같이 증가
# 타겟보다 크면 왼쪽애를 왼쪽으로.

# 양쪽에서 시작
# 합이 타겟보다 작으면, 왼쪽이 증가, 크면 오른쪽이 차감
