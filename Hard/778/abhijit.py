import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        memo = {}
        arr = grid
        n = len(arr)

        def dfs(pos, min_time):
            # pruning: if we've already reached pos with a better/equal min_time, skip
            if pos in memo and memo[pos] <= min_time:
                return float("inf")

            # store best min_time seen for this cell
            memo[pos] = min_time

            # reached target
            if pos == (n - 1, n - 1):
                return max(min_time, arr[n - 1][n - 1])

            h = []
            steps = [(0,1), (1,0), (-1,0), (0,-1)]

            # collect all valid next moves
            for dx, dy in steps:
                new_x, new_y = pos[0] + dx, pos[1] + dy
                if 0 <= new_x < n and 0 <= new_y < n:
                    heapq.heappush(h, (arr[new_x][new_y], (new_x, new_y)))

            least_time = float("inf")

            while h:
                time_needed, next_pos = heapq.heappop(h)
                least_amount_of_time_waited = dfs(next_pos, max(time_needed, min_time))
                least_time = min(least_time, least_amount_of_time_waited)

            return least_time

        return dfs((0,0), arr[0][0])
