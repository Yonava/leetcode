# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        p2 = head
        length = 0
        while p1 != None:
            length +=1
            p1 = p1.next
        
        
        offset = length - n
        if offset == 0:
            return head.next

        while offset > 1:
            p2 = p2.next
            offset -= 1
        
        p2.next = p2.next.next
        return head
    
'''
optimal solution adds a dumy node to the front.
Left pointer at dummy node
right pointer is shifted to n + 1
shift L and R until R is null
then just do the pointer manipulation for deletion
'''