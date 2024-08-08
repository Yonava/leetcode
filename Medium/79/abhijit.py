from collections import deque
from typing import List

class Solution:

    def bfs(self, curr_pos, curr_index, word, board, seen):
        if curr_index == len(word):
            return True
        q = deque([curr_pos])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while q:
            pos = q.popleft()
            for d in directions:
                new_pos = (pos[0] + d[0], pos[1] + d[1])
                if (0 <= new_pos[0] < len(board) and 0 <= new_pos[1] < len(board[0]) and
                        new_pos not in seen and board[new_pos[0]][new_pos[1]] == word[curr_index]):
                    seen.add(new_pos)
                    if self.bfs(new_pos, curr_index + 1, word, board, seen):
                        return True
                    seen.remove(new_pos)
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        height, width = len(board), len(board[0])
        for h in range(height):
            for w in range(width):
                if board[h][w] == word[0]:
                    print("entering with", board[h][w])
                    seen = set()
                    seen.add((h, w))
                    if self.bfs((h, w), 1, word, board, seen):
                        return True
        return False
