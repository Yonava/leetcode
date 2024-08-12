class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        # create a min heap of size k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        
        return self.heap[0]
        
'''
create a max heap and then
'''


# Your KthLargest object will be instantiated and called as such:
k = 3
nums = [4, 5, 8, 2]
obj = KthLargest(k, nums)
# print("internal heap",obj.heap)
val = 3
param_1 = obj.add(val)
print("new heap", obj.heap)
print(param_1)