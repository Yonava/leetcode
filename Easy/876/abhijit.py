# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head

        if head == None:
            return None
        elif head.next == None:
            return head
        elif head.next.next == None:
            return head.next
        
        while fast.next != None:
            fast = fast.next
            if fast.next != None:
                fast = fast.next
            else:
                return slow.next
            slow = slow.next
        
        return slow