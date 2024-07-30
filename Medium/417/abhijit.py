class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # pacific ocean occurs whenver  x < -1 and y < -1 
        # atlantic ocean occurs whenver x > width + 1 and y > height + 1 
        if not heights:
            return 0
        width, height = len(heights[0]) , len(heights)
        def checkPacific(r,c):
            if r <= -1 or c <= -1:
                return True
            else:
                False

        def checkAtlantic(r,c):
            if r >= height or c >= width:
                return True
            else:
                False
        
        result = []
        
        def bfs(grid,r,c):
            print("starting at",(r,c))
            visited = set()
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            original = (r,c)
            
            reached_atlantic = 0
            reached_pacific = 0

            while q:
                r,c = q.popleft()
                directions = [[1,0], [-1,0], [0,1], [0,-1]]
                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc
                    
                    
                    if checkAtlantic(new_r,new_c):
                        # stop exploring anymore
                        reached_atlantic = 1
                        continue

                    if checkPacific(new_r, new_c):
                        # stop exploring anymore
                        reached_pacific = 1
                        continue

                    if grid[new_r][new_c] <= grid[r][c] and (r,c) not in visited:
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
                    else:
                        visited.add((new_r,new_c))

            if reached_atlantic == reached_pacific == 1:
                result.append(original)

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                bfs(heights,r,c)
        
        return result
                    