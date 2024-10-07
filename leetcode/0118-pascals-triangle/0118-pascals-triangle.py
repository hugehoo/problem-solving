class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = [[1]]
        for i in range(1, numRows):
            temp = [1]
            for j in range(1, i + 1):
                if j == i:
                    temp.append(1)
                    result.append(temp)
                    break
                temp.append(result[i - 1][j - 1] + result[i - 1][j])

        return result
