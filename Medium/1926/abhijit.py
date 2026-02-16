from collections import deque
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        rows, cols = len(maze), len(maze[0])
        start_r, start_c = entrance[0], entrance[1]
        
        exit_set = set()
        for r in range(rows):
            if maze[r][0] == ".": exit_set.add((r, 0))
            if maze[r][cols - 1] == ".": exit_set.add((r, cols - 1))
        
        for c in range(cols):
            if maze[0][c] == ".": exit_set.add((0, c))
            if maze[rows - 1][c] == ".": exit_set.add((rows - 1, c))
        
        
        if (start_r, start_c) in exit_set:
            exit_set.remove((start_r, start_c))

        # 3. BFS logic
        q = deque([(start_r, start_c, 0)]) # Store (row, col, steps)
        visited = {(start_r, start_c)}
        
        while q:
            r, c, steps = q.popleft()
            
            # If we reached a boundary cell that isn't the entrance
            if (r, c) in exit_set:
                return steps
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc
                
                # Check boundaries and if it's an unvisited path
                if 0 <= nr < rows and 0 <= nc < cols and \
                   maze[nr][nc] == "." and (nr, nc) not in visited:
                    
                    visited.add((nr, nc))
                    q.append((nr, nc, steps + 1))
        
        return -1 