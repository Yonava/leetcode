# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], p: int, q: int) -> Optional[ListNode]:
        if p == q:
            return head
        
        currPos = 1
        currNode = head
        prevNode = None
        
        # Move to node at position p
        while currNode and currPos < p:
            prevNode = currNode
            currNode = currNode.next
            currPos += 1

        # Now reverse from p to q
        lastNodeBeforeSublist = prevNode
        lastNodeOfSublist = currNode
        nextNode = None

        while currNode and currPos <= q:
            nextNode = currNode.next
            currNode.next = prevNode
            prevNode = currNode
            currNode = nextNode
            currPos += 1

        # Connect the reversed sublist back
        # this was the key part that was failing when start at the start (be careful with the pointer logic)
        if lastNodeBeforeSublist:
            lastNodeBeforeSublist.next = prevNode
        else:
            head = prevNode

        lastNodeOfSublist.next = currNode
        
        return head
