class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []

        # O(n)
        for stone in stones:
            heap.append(-1 * stone)

        #O(nlog(n))
        heapq.heapify(heap)
        while len(heap) > 1:
            l1 = heapq.heappop(heap)
            l2 = heapq.heappop(heap)
            difference = abs((-1 * l1) - (-1 * l2))
            if difference > 0:
                heapq.heappush(heap, (-1 * difference))
        
        if len(heap) == 0:
            return 0
        else:
            return -1 * heap[0]
        

