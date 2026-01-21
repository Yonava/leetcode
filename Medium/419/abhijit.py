class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        
        def explore(x,y):
            q = deque()
            q.append((x,y))
            directions = [(-1,0), (1,0), (0,-1), (0,1)]
            
            while q:
                cx, cy = q.popleft()
                board[cx][cy] = "."
                for dx, dy in directions:
                    nx, ny = cx + dx, cy + dy
                    if nx >= 0 and nx < len(board) and ny >= 0 and ny < len(board[0]):
                        if board[nx][ny] == "X":
                            q.append((nx,ny))
        
        count = 0
        for x in range(len(board)):
            for y in range(len(board[0])):
                if board[x][y] == "X":
                    explore(x,y)
                    count += 1
        return count
    
# because battleship can only be vertical or horizontal, we can just count the heads. 
# the head is the only one that does not have another "X" above it or to the left of it.
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        
        for i, row in enumerate(board):
            for j, cell in enumerate(row):
                if cell == "X":
                    if (i == 0 or board[i - 1][j] == ".") and\
                       (j == 0 or board[i][j - 1] == "."):
                            count += 1
                            
        return count
        