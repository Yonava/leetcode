class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # simple breadth first search
        q = deque()

        # find all the rotten oranges
        for h in range(len(grid)):
            for w in range(len(grid[0])):
                if grid[h][w] == 2:
                    q.append((h,w))
        
        # If there are no rotten oranges to begin with
        if not q:
            return -1 if any(1 in row for row in grid) else 0

        print("all rotten oranges", q)
        minutes = -1
        #  carry out bfs on all the oranges with the same set to mark as visited
        while q:
                minutes += 1
                # Process all rotten oranges at the current minute
                for _ in range(len(q)):
                    curr_h, curr_w = q.popleft()
                    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                        new_h, new_w = curr_h + dx, curr_w + dy
                        if 0 <= new_h < len(grid) and 0 <= new_w < len(grid[0]) and grid[new_h][new_w] == 1:
                            grid[new_h][new_w] = 2
                            q.append((new_h, new_w))

        # check to see if all the oranges are rotten
        for h in range(len(grid)):
            for w in range(len(grid[0])):
                if grid[h][w] == 1:
                    return -1

        return minutes