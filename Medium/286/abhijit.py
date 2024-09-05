class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # find all the treassure coordinates first.
        treasure = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    treasure.add((i,j))

        def bfs(start):
            seen = set()
            q = deque()
            q.append(start)
            seen.add(start)

            steps = 0

            directions = [(0,1), (1,0), (-1,0), (0,-1)]

            while q:
                for _ in range(len(q)):  # Level by level BFS
                    curr = q.popleft()

                    # Update the grid value only if it's not an obstacle
                    if grid[curr[0]][curr[1]] != -1:
                        grid[curr[0]][curr[1]] = min(steps, grid[curr[0]][curr[1]])

                    # Explore neighbors
                    for dx, dy in directions:
                        nx, ny = curr[0] + dx, curr[1] + dy
                        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and (nx, ny) not in seen and grid[nx][ny] != -1:
                            q.append((nx, ny))
                            seen.add((nx, ny))

                steps += 1  # Increment step after each level
                        
        for t in treasure:
            bfs(t)
