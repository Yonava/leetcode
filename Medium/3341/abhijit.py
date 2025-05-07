import heapq
from typing import List
class Solution:
    def minTimeToReach(self, moveTime: List[List[int]]) -> int:
        n = len(moveTime)
        m = len(moveTime[0])
        min_time = [[float("inf")] * m for _ in range(n)]
        min_time[0][0] = 0
        heap = [(0, 0, 0)]  # (time, row, col)
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        while heap:
            current_time, r, c = heapq.heappop(heap)

            if current_time > min_time[r][c]:
                continue

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m:
                    arrival_time = current_time + 1
                    start_move_time_to_next = max(arrival_time, moveTime[nr][nc] + 1)

                    if start_move_time_to_next < min_time[nr][nc]:
                        min_time[nr][nc] = start_move_time_to_next
                        heapq.heappush(heap, (start_move_time_to_next, nr, nc))

        return min_time[n - 1][m - 1]