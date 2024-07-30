class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows , cols = len(grid), len(grid[0])
        islands = 0
        visited = set()

        def bfs(r,c):
            queue = collections.deque()
            visited.add((r,c))
            queue.append((r,c))
            while queue:
                row, col = queue.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    r,c = row + dr, col + dc
                    if r >= 0 and r <=rows -1  and c >= 0 and c <= cols - 1 and (r,c) not in visited and grid[r][c] == "1":
                        queue.append((r,c))
                        visited.add((r,c))


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited :
                    bfs(r,c)
                    islands +=1
        
        return islands