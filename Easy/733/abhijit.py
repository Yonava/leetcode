class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        height = len(image)
        width = len(image[0])
        
        def bfs(coord, original):
            seen = set()
            q = deque()
            q.append(coord)
            seen.add(coord)
            directions = [(0,1),(0,-1),(1,0),(-1,0)]

            while q:
                curr_x, curr_y = q.popleft()
                
                image[curr_x][curr_y] = color

                for dx,dy in directions:
                    new_x, new_y = curr_x + dx, curr_y + dy
                    if new_x >= 0 and new_x < height and new_y >= 0 and new_y < width and (new_x,new_y) not in seen:
                        if image[new_x][new_y] == original:
                            q.append((new_x,new_y))
                            seen.add((new_x,new_y))
                    
        bfs((sr,sc),image[sr][sc])
        return image