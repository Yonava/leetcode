# my iterative solution
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        ROWS, COLS = len(grid), len(grid[0])
        res = 0

        visited = set()
        def bfs(grid,r,c):
            q = collections.deque()
            q.append((r,c))    
            cur_sum = 0 # this is maintain in one bfs cycle 
            while q:
                r,c = q.popleft()
                if (r, c) in visited or grid[r][c] == 0:
                    continue
                    
                visited.add((r, c))
                cur_sum += 1

                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    if (new_r, new_c) not in visited and 0 <= new_r < len(grid) and 0 <= new_c < len(grid[0]):
                        q.append((new_r, new_c))

            return cur_sum
        
        for r in range(ROWS):
            for c in range(COLS):
                # print(f"currently working on ({r,c}) -> {grid[r][c]}")
                area = bfs(grid,r,c)
                # print("visited", visited)
                # print("area", area)
                res = max(area,res)
        
        return res

# recursive way to do it
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != 1:
                return 0
            grid[i][j] = 0
            area = 1
            area += dfs(i + 1, j)
            area += dfs(i - 1, j)
            area += dfs(i, j + 1)
            area += dfs(i, j - 1)
            return area

        max_area = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area