class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        curr_pos = { i: 0 for i in range(0,len(matrix))}
        heap = [(a[0], i) for i, a in enumerate(matrix)]
        heapq.heapify(heap)
        min_val = float("inf")

        for _ in range(k):
            val, index = heapq.heappop(heap)
            min_val = val
            
            if curr_pos[index] + 1 >= len(matrix):
                continue
            else:
                heapq.heappush(heap,(matrix[index][curr_pos[index] + 1], index))
                curr_pos[index] += 1
            
        return min_val