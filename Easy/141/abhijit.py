# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tortise = head
        if head == None:
            return False
        while hare != None and hare.next != None:
            hare = hare.next.next
            tortise = tortise.next
            if hare == tortise:
                return True
        return False