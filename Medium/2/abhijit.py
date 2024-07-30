# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def recurSoln(self, l1, l2, carry):
        if l1 == None and l2 == None:
            if carry:
                return ListNode(carry, None)
            else:
                return None
        sum = 0
        if l1 == None:
            sum += 0
        else:
            sum += l1.val
        if l2 == None:
            sum += 0
        else:
            sum += l2.val

        sum += carry
        l1_next = 0
        l2_next = 0
        if l1 == None:
            l1_next = None
        else:
            l1_next = l1.next

        if l2 == None:
            l2_next = None
        else:
            l2_next = l2.next
        if sum >= 10:
            remainder = sum % 10
            return ListNode(remainder, self.recurSoln(l1_next, l2_next, 1))
        else:
            return ListNode(sum, self.recurSoln(l1_next,l2_next,0))

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        return self.recurSoln(l1,l2,0)
        