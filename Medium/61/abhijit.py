# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not k: return head

        last, length =  head, 1
        while last.next:
            last = last.next
            length += 1
        
        last.next = head # create a circular linked list

        # k % length gives us the number of rotations.(the mod accounts for changes that are)
        # length
        for _ in range(length - k % length):
            last = last.next
        dummy = last.next
        last.next = None
        return dummy