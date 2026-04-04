class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        new_grid = [( [0] * len(grid[0]) ) for _ in range(len(grid))]

        # print(new_grid)
        sum_col = 0
        for i in range(len(grid[0])):
            sum_col += grid[0][i]
            new_grid[0][i] = sum_col
        
        sum_row = 0
        for i in range(len(grid)):
            sum_row += grid[i][0]
            new_grid[i][0] = sum_row
        
        # print(new_grid)
        for x in range(1,len(grid)):
            for y in range(1, len(grid[0])):
                new_grid[x][y] = grid[x][y] + min(new_grid[x-1][y], new_grid[x][y-1])

        return new_grid[-1][-1]