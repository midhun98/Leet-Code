class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        sorted_grid = []
        for i in grid:
            i.sort()
            sorted_grid.append(i)
        result = 0
        for i in range(len(sorted_grid[0])):
            prev_max = 0
            for j in range(len(grid)):
                prev_max = max(grid[j][i], prev_max)
            result += prev_max
        return result
