class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        horizontal = {i: set() for i in range(9) }
        vertical = {i: set() for i in range(9) }

        for i in range(9):
            for j in range(9):
                if board[i][j] in horizontal[i] or board[i][j] in vertical[j]:
                    print(i,j, board[i][j])
                    return False
                else:
                    if board[i][j] != ".":
                        horizontal[i].add(board[i][j])
                        vertical[j].add(board[i][j])

        subgrid = {
            (0,0): set(),
            (0,3):  set(),
            (0,6):  set(),
            (3,0):  set(),
            (3,3):  set(), 
            (3,6):  set(),
            (6,0):  set(),
            (6,3):  set(),
            (6,6):  set(),
        }

        for key in subgrid:
            start, end = key
            for i in range(3):
                for j in range(3):
                    if board[start + i][end + j] in subgrid[key]:
                        return False
                    elif  board[start + i][end + j] != ".":
                        subgrid[key].add(board[start + i][end + j] )

        

        return True
