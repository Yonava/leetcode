class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        visiting = set()
        rows, cols = len(maze), len(maze[0])
        
        def dfs(curr_x, curr_y):
            if [curr_x, curr_y] == destination:
                return True
            if (curr_x, curr_y) in visiting:
                return False
            
            visiting.add((curr_x, curr_y))
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)] 

            for dx, dy in directions:
                
                nx, ny = curr_x, curr_y
            
                while 0 <= nx + dx < rows and 0 <= ny + dy < cols and maze[nx + dx][ny + dy] == 0:
                    nx += dx
                    ny += dy
                
                if dfs(nx, ny):
                    return True
            
            return False
        
        return dfs(start[0], start[1])