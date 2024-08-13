class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heappush(heap,num)
                heapq.heappop(heap)
        
        return heap[0]
    
"""
The idea is that we maintain a window of a heap of size k and we move it through the remaining list
"""