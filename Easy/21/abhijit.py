# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None: 
            return None
        
        if list2 == None and list1 != None:
            return list1
        
        if list1 == None and list2 != None:
            return list2

        if list1.val < list2.val:
            next_val = self.mergeTwoLists(list2, list1.next)
            return ListNode(list1.val, next_val)
        else:
            
            next_val = self.mergeTwoLists(list1, list2.next)
            return ListNode(list2.val, next_val)