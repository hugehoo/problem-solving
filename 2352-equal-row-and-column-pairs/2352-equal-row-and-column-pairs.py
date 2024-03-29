class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        trans_grid = []
        for n in range(len(grid)):
            trans_grid.append([grid[j][n] for j in range(len(grid))])

        result = []
        for n in range(len(grid)):
            result.append(sum([1 for m in range(len(grid)) if grid[n] == trans_grid[m]]))
            
        return sum(result)