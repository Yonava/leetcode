# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        end = head
        length = 0
        while end.next != None:
            end = end.next
            length += 1

        endTracker = end
        end.next = head

        start = head
        while start != endTracker:
            if start.val != end.val:
                endTracker.next = None
                return False
            start = start.next
            for c in range(length):
                end = end.next
        
        endTracker.next = None
        return True
