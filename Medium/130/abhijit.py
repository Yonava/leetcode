from collections import deque
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return

        height, width = len(board), len(board[0])
        save_o = set()

        # Function to perform BFS and mark all connected "O"s from a given start point
        def bfs(start):
            q = deque([start])
            save_o.add(start)

            while q:
                curr = q.popleft()
                directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for direction in directions:
                    new = (curr[0] + direction[0], curr[1] + direction[1])
                    if (
                        0 <= new[0] < height
                        and 0 <= new[1] < width
                        and board[new[0]][new[1]] == "O"
                        and new not in save_o
                    ):
                        q.append(new)
                        save_o.add(new)

        # Check the first and last row for 'O'
        for i in range(width):
            if board[0][i] == "O":
                bfs((0, i))
            if board[height - 1][i] == "O":
                bfs((height - 1, i))

        # Check the first and last column for 'O'
        for i in range(height):
            if board[i][0] == "O":
                bfs((i, 0))
            if board[i][width - 1] == "O":
                bfs((i, width - 1))

        # Modify the board in-place
        for i in range(height):
            for j in range(width):
                if (i, j) not in save_o:
                    board[i][j] = "X"
