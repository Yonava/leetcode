# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists):
        if not lists or len(lists) == 0:
            return None
        
        # Define a min-heap
        heap = []
        
        # Add the first node of each list to the heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        # Dummy head for the merged list
        dummy = ListNode(0)
        current = dummy
        
        # Extract the smallest element from the heap and add its next node to the heap
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next   
                