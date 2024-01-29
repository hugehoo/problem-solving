class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        trans_grid = []
        for n in range(len(grid)):
            trans_grid.append([grid[j][n] for j in range(len(grid))])
        print(trans_grid)
        total = 0
        for n in range(len(grid)):
            for m in range(len(grid)):
                if grid[n] == trans_grid[m]:
                    total += 1
        return total
